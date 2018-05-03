from django.db import models

from crim.models.person import CRIMPerson
from crim.models.piece import CRIMPiece


class CRIMObservation(models.Model):
    class Meta:
        app_label = 'crim'
        verbose_name = 'Observation'
        verbose_name_plural = 'Observations'

    observer = models.ForeignKey(
        CRIMPerson,
        on_delete=models.SET_NULL,
        to_field='person_id',
        null=True,
        db_index=True,
        related_name='observations',
    )

    piece = models.ForeignKey(
        CRIMPiece,
        on_delete=models.CASCADE,
        to_field='piece_id',
        db_index=True,
        related_name='observations',
    )
    ema = models.TextField('EMA expression', blank=True)

    mt_cf_voices = models.TextField('voices (one per line)', blank=True)
    mt_cf_dur = models.BooleanField('durations only', default=False)
    mt_cf_mel = models.BooleanField('intervals only', default=False)
    mt_sog_voices = models.TextField('voices (one per line)', blank=True)
    mt_sog_dur = models.BooleanField('durations only', default=False)
    mt_sog_mel = models.BooleanField('intervals only', default=False)
    mt_sog_ostinato = models.BooleanField('ostinato', default=False)
    mt_sog_periodic = models.BooleanField('periodic', default=False)
    mt_csog_voices = models.TextField('voices (one per line)', blank=True)
    mt_csog_dur = models.BooleanField('durations only', default=False)
    mt_csog_mel = models.BooleanField('intervals only', default=False)
    mt_cd_voices = models.TextField('voices (one per line)', blank=True)
    mt_fg_voices = models.TextField('voices (one per line)', blank=True)
    mt_fg_periodic = models.BooleanField('periodic', default=False)
    mt_fg_strict = models.BooleanField('strict', default=False)
    mt_fg_flexed = models.BooleanField('flexed', default=False)
    mt_fg_sequential = models.BooleanField('sequential', default=False)
    mt_fg_inverted = models.BooleanField('inverted', default=False)
    mt_fg_retrograde = models.BooleanField('retrograde', default=False)
    mt_fg_int = models.CharField('intervals', max_length=32, blank=True)  # better name?
    mt_fg_tint = models.CharField('tint', max_length=32, blank=True)  # needs better name
    mt_id_voices = models.TextField('voices (one per line)', blank=True)
    mt_id_strict = models.BooleanField('strict', default=False)
    mt_id_flexed = models.BooleanField('flexed', default=False)
    mt_id_flt = models.BooleanField('flexed tonal', default=False)
    mt_id_invertible = models.BooleanField('invertible', default=False)
    mt_id_int = models.CharField('intervals', max_length=32, blank=True)  # better name?
    mt_id_tint = models.CharField('tint', max_length=32, blank=True)  # needs better name
    mt_pe_voices = models.TextField('voices (one per line)', blank=True)
    mt_pe_strict = models.BooleanField('strict', default=False)
    mt_pe_flexed = models.BooleanField('flexed', default=False)
    mt_pe_flt = models.BooleanField('flexed tonal', default=False)
    mt_pe_sequential = models.BooleanField('sequential', default=False)
    mt_pe_added = models.BooleanField('added', default=False)
    mt_pe_invertible = models.BooleanField('invertible', default=False)
    mt_pe_int = models.CharField('intervals', max_length=32, blank=True)  # better name?
    mt_pe_tint = models.CharField('tint', max_length=32, blank=True)  # needs better name
    mt_nid_voices = models.TextField('voices (one per line)', blank=True)
    mt_nid_strict = models.BooleanField('strict', default=False)
    mt_nid_flexed = models.BooleanField('flexed', default=False)
    mt_nid_flt = models.BooleanField('flexed tonal', default=False)
    mt_nid_sequential = models.BooleanField('sequential', default=False)
    mt_nid_invertible = models.BooleanField('invertible', default=False)
    mt_nid_int = models.CharField('intervals', max_length=32, blank=True)  # better name?
    mt_nid_tint = models.CharField('tint', max_length=32, blank=True)  # needs better name
    mt_hr_voices = models.TextField('voices (one per line)', blank=True)
    mt_hr_simple = models.BooleanField('simple', default=False)
    mt_hr_staggered = models.BooleanField('staggered', default=False)
    mt_hr_sequential = models.BooleanField('sequential', default=False)
    mt_hr_fauxbourdon = models.BooleanField('fauxbourdon', default=False)
    mt_cad_cantizans = models.TextField('cantizans', blank=True)
    mt_cad_tenorizans = models.TextField('tenorizans', blank=True)
    mt_cad_authentic = models.BooleanField('authentic', default=False)
    mt_cad_phrygian = models.BooleanField('phrygian', default=False)
    mt_cad_plagal = models.BooleanField('plagal', default=False)
    mt_cad_tone = models.CharField('tone', max_length=4, blank=True)
    mt_cad_dtv = models.CharField('dovetail voice', max_length=32, blank=True)
    mt_cad_dti = models.CharField('interval', max_length=32, blank=True)
    mt_int_voices = models.TextField('voices (one per line)', blank=True)
    mt_int_p6 = models.BooleanField('parallel 6', default=False)
    mt_int_p3 = models.BooleanField('parallel 3 (or 10)', default=False)
    mt_int_c35 = models.BooleanField('chained 3 and 5', default=False)
    mt_int_c83 = models.BooleanField('chained 8 and 3', default=False)
    mt_int_c65 = models.BooleanField('chained 6 and 5', default=False)
    mt_fp_comment = models.TextField('comment', blank=True)
    mt_fp_ir = models.BooleanField('internal repetition', default=False)
    mt_fp_range = models.CharField('range', max_length=16, blank=True)

    remarks = models.TextField('remarks (supports Markdown)', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    needs_review = models.BooleanField(default=False)

    def __str__(self):
        return '<{0}> {1}'.format(self.id, self.piece_id)
