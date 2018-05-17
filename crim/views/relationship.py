from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions

from crim.renderers.custom_html_renderer import CustomHTMLRenderer
from crim.serializers.relationship import CRIMRelationshipDetailSerializer, CRIMRelationshipListSerializer
from crim.models.relationship import CRIMRelationship

COMPOSER = 'Composer'


class RelationshipListHTMLRenderer(CustomHTMLRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        template_names = ['relationship/relationship_list.html']
        template = self.resolve_template(template_names)
        context = self.get_template_context({'content': data}, renderer_context)
        return template.render(context)


class RelationshipDetailHTMLRenderer(CustomHTMLRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # - Add `composer` field to content: only look at roles with
        # the role type with name "Composer", and add all such names
        # to the list, along with the url of the composer
        model_composers = []
        for role in data['model_observation']['piece']['roles']:
            if role['role_type'] and role['role_type']['name'] == COMPOSER:
                model_composer_html = ('<a href="' + role['person']['url'].replace('/data/', '/') +
                                       '">' + role['person']['name'] + '</a>')
                model_composers.append(model_composer_html)
        if data['model_observation']['piece']['mass']:
            for role in data['model_observation']['piece']['mass']['roles']:
                if role['role_type'] and role['role_type']['name'] == COMPOSER:
                    model_composer_html = ('<a href="' + role['person']['url'].replace('/data/', '/') +
                                           '">' + role['person']['name'] + '</a>')
                    model_composers.append(model_composer_html)
        data['model_composers_with_urls'] = ', '.join(model_composers) if model_composers else None

        # Do the same for the derivative
        derivative_composers = []
        for role in data['derivative_observation']['piece']['roles']:
            if role['role_type'] and role['role_type']['name'] == COMPOSER:
                derivative_composer_html = ('<a href="' + role['person']['url'].replace('/data/', '/') +
                                            '">' + role['person']['name'] + '</a>')
                derivative_composers.append(derivative_composer_html)
        if data['derivative_observation']['piece']['mass']:
            for role in data['derivative_observation']['piece']['mass']['roles']:
                if role['role_type'] and role['role_type']['name'] == COMPOSER:
                    derivative_composer_html = ('<a href="' + role['person']['url'].replace('/data/', '/') +
                                                '">' + role['person']['name'] + '</a>')
                    derivative_composers.append(derivative_composer_html)
        data['derivative_composers_with_urls'] = ', '.join(derivative_composers) if derivative_composers else None

        template_names = ['relationship/relationship_detail.html']
        template = self.resolve_template(template_names)
        context = self.get_template_context({'content': data}, renderer_context)
        return template.render(context)


class RelationshipList(generics.ListAPIView):
    model = CRIMRelationship
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CRIMRelationshipListSerializer
    renderer_classes = (RelationshipListHTMLRenderer,)

    def get_queryset(self):
        order_by = self.request.GET.get('order_by', 'model_observation__piece_id')
        return CRIMRelationship.objects.all().order_by(order_by)


class RelationshipDetail(generics.RetrieveAPIView):
    model = CRIMRelationship
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CRIMRelationshipDetailSerializer
    renderer_classes = (JSONRenderer, RelationshipDetailHTMLRenderer)  # add html later
    queryset = CRIMRelationship.objects.all()

    def get_object(self):
        url_arg = self.kwargs['pk']
        relationship = CRIMRelationship.objects.filter(pk=url_arg)
        obj = get_object_or_404(relationship)
        self.check_object_permissions(self.request, obj)
        return obj


class RelationshipListData(generics.ListAPIView):
    model = CRIMRelationship
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CRIMRelationshipListSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        order_by = self.request.GET.get('order_by', 'model_observation__piece_id')
        return CRIMRelationship.objects.all().order_by(order_by)


class RelationshipDetailData(generics.RetrieveAPIView):
    model = CRIMRelationship
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CRIMRelationshipDetailSerializer
    renderer_classes = (JSONRenderer,)
    queryset = CRIMRelationship.objects.all()

    def get_object(self):
        url_arg = self.kwargs['pk']
        relationship = CRIMRelationship.objects.filter(pk=url_arg)
        obj = get_object_or_404(relationship)
        self.check_object_permissions(self.request, obj)
        return obj
