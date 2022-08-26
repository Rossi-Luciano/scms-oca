from django.utils.translation import gettext as _

classification = (
    ('', ''),
    ('promoção', _('promoção')),
    ('posicionamento', _('posicionamento')),
    ('mandato', _('mandato')),
    ('geral', _('geral')),
)

status = (
    ('', ''),
    ('WIP', 'WIP'),
    ('TO_MODERATE', 'TO_MODERATE'),
    ('PUBLISHED', 'PUBLISHED'),
)
