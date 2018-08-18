from crim.models.comment import CRIMComment
from crim.models.mass import CRIMMass
from crim.models.person import CRIMPerson
from crim.models.piece import CRIMPiece
from crim.models.user import CRIMUserProfile
from rest_framework import serializers


class CRIMPersonCommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimperson-detail-data', lookup_field='person_id')

    class Meta:
        model = CRIMPerson
        fields = (
            'url',
            'name',
        )


class CRIMUserProfileCommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimuserprofile-detail-data', lookup_field='username')
    person = CRIMPersonCommentSerializer(read_only=True)

    class Meta:
        model = CRIMUserProfile
        fields = (
            'url',
            'person',
            'name',
            'name_sort',
        )


class CRIMMassCommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimmass-detail-data', lookup_field='mass_id')

    class Meta:
        model = CRIMMass
        fields = (
            'url',
            'mass_id',
            'title',
        )


class CRIMPieceCommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimpiece-detail-data', lookup_field='piece_id')
    mass = CRIMMassCommentSerializer(read_only=True)

    class Meta:
        model = CRIMPiece
        fields = (
            'url',
            'piece_id',
            'mass',
            'title',
        )


class CRIMCommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crimcomment-detail-data', lookup_field='comment_id')
    author = CRIMUserProfileCommentSerializer(read_only=True)
    piece = CRIMPieceCommentSerializer(read_only=True)  # change with generic foreign key

    class Meta:
        model = CRIMComment
        fields = (
            'url',
            'author',
            'piece',
            'text',
            'created',
            'updated',
        )
