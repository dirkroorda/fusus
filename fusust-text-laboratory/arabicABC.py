QURANCLOSE = '﴾'
QURANOPEN = '﴿'
COMMA = '\u060C'
SEMICOLON = '\u061B'
QUESTION = '\u061F'
HAMZA = '\u0621'
ALEF_MADDA = '\u0622'
ALEF_HAMZA_ABOVE = '\u0623'
WAW_HAMZA = '\u0624'
ALEF_HAMZA_BELOW = '\u0625'
YEH_HAMZA = '\u0626'
ALEF = '\u0627'
BEH = '\u0628'
TEH_MARBUTA = '\u0629'
TEH = '\u062a'
THEH = '\u062b'
JEEM = '\u062c'
HAH = '\u062d'
KHAH = '\u062e'
DAL = '\u062f'
THAL = '\u0630'
REH = '\u0631'
ZAIN = '\u0632'
SEEN = '\u0633'
SHEEN = '\u0634'
SAD = '\u0635'
DAD = '\u0636'
TAH = '\u0637'
ZAH = '\u0638'
AIN = '\u0639'
GHAIN = '\u063a'
TATWEEL = '\u0640'
FEH = '\u0641'
QAF = '\u0642'
KAF = '\u0643'
LAM = '\u0644'
MEEM = '\u0645'
NOON = '\u0646'
HEH = '\u0647'
WAW = '\u0648'
ALEF_MAKSURA = '\u0649'
YEH = '\u064a'
MADDA_ABOVE = '\u0653'
HAMZA_ABOVE = '\u0654'
HAMZA_BELOW = '\u0655'
ZERO = '\u0660'
ONE = '\u0661'
TWO = '\u0662'
THREE = '\u0663'
FOUR = '\u0664'
FIVE = '\u0665'
SIX = '\u0666'
SEVEN = '\u0667'
EIGHT = '\u0668'
NINE = '\u0669'
PERCENT = '\u066a'
DECIMAL = '\u066b'
THOUSANDS = '\u066c'
STAR = '\u066d'
MINI_ALEF = '\u0670'
ALEF_WASLA = '\u0671'
FULL_STOP = '\u06d4'
BYTE_ORDER_MARK = '\ufeff'

# Diacritics
FATHATAN = '\u064b'
DAMMATAN = '\u064c'
KASRATAN = '\u064d'
FATHA = '\u064e'
DAMMA = '\u064f'
KASRA = '\u0650'
SHADDA = '\u0651'
SUKUN = '\u0652'

# Small Letters
SMALL_ALEF = "\u0670"
SMALL_WAW = "\u06E5"
SMALL_YEH = "\u06E6"
# Ligatures
LAM_ALEF = '\ufefb'
LAM_ALEF_HAMZA_ABOVE = '\ufef7'
LAM_ALEF_HAMZA_BELOW = '\ufef9'
LAM_ALEF_MADDA_ABOVE = '\ufef5'
SIMPLE_LAM_ALEF = '\u0644\u0627'
SIMPLE_LAM_ALEF_HAMZA_ABOVE = '\u0644\u0623'
SIMPLE_LAM_ALEF_HAMZA_BELOW = '\u0644\u0625'
SIMPLE_LAM_ALEF_MADDA_ABOVE = '\u0644\u0622'
# groups
LETTERS = (
    ALEF, BEH, TEH, TEH_MARBUTA, THEH, JEEM, HAH, KHAH,
    DAL, THAL, REH, ZAIN, SEEN, SHEEN, SAD, DAD, TAH, ZAH,
    AIN, GHAIN, FEH, QAF, KAF, LAM, MEEM, NOON, HEH, WAW, YEH,
    HAMZA, ALEF_MADDA, ALEF_HAMZA_ABOVE, WAW_HAMZA, ALEF_HAMZA_BELOW,
    YEH_HAMZA, ALEF_MAKSURA, ALEF_WASLA, HAMZA_ABOVE, HAMZA_BELOW
    )
NUMBERS = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)

TASHKEEL = (FATHATAN, DAMMATAN, KASRATAN,
            FATHA, DAMMA, KASRA,
            SUKUN,
            SHADDA)
HARAKAT = (FATHATAN, DAMMATAN, KASRATAN,
           FATHA, DAMMA, KASRA,
           SUKUN
           )
SHORTHARAKAT = (FATHA, DAMMA, KASRA, SUKUN)

TANWIN = (FATHATAN, DAMMATAN, KASRATAN)

NOT_DEF_HARAKA = TATWEEL
LIGUATURES = (
    LAM_ALEF,
    LAM_ALEF_HAMZA_ABOVE,
    LAM_ALEF_HAMZA_BELOW,
    LAM_ALEF_MADDA_ABOVE,
)
HAMZAT = (HAMZA, WAW_HAMZA, YEH_HAMZA, HAMZA_ABOVE, HAMZA_BELOW,
          ALEF_HAMZA_BELOW, ALEF_HAMZA_ABOVE,
          )
ALEFAT = (ALEF, ALEF_MADDA, ALEF_HAMZA_ABOVE,
          ALEF_HAMZA_BELOW, ALEF_WASLA, ALEF_MAKSURA, SMALL_ALEF,
          )


WEAK = (ALEF, WAW, YEH, ALEF_MAKSURA)


YEHLIKE = (YEH, YEH_HAMZA, ALEF_MAKSURA, SMALL_YEH)
WAWLIKE = (WAW, WAW_HAMZA, SMALL_WAW)
TEHLIKE = (TEH, TEH_MARBUTA)

BEHLIKE = (BEH, TEH, THEH, NOON)
JEEMLIKE = (JEEM, HAH, KHAH)
DALLIKE = (DAL, THAL)
REHLIKE = (REH, ZAIN)
SEENLIKE = (SEEN, SHEEN)
SADLIKE = (SAD, DAD)
TAHLIKE = (TAH, ZAH)
AINLIKE = (AIN, GHAIN)
FEHLIKE = (FEH, QAF)

SMALL = (SMALL_ALEF, SMALL_WAW, SMALL_YEH)
MOON = (HAMZA, ALEF_MADDA, ALEF_HAMZA_ABOVE, ALEF_HAMZA_BELOW,
        ALEF, BEH, JEEM, HAH, KHAH, AIN, GHAIN,
        FEH, QAF, KAF, MEEM, HEH, WAW, YEH)

SUN = (TEH, THEH, DAL, THAL, REH, ZAIN, SEEN, SHEEN,
       SAD, DAD, TAH, ZAH, LAM, NOON,)

ALPHABETIC_ORDER = {
    ALEF: 1,
    BEH: 2,
    TEH: 3,
    TEH_MARBUTA: 3,
    THEH: 4,
    JEEM: 5,
    HAH: 6,
    KHAH: 7,
    DAL: 8,
    THAL: 9,
    REH: 10,
    ZAIN: 11,
    SEEN: 12,
    SHEEN: 13,
    SAD: 14,
    DAD: 15,
    TAH: 16,
    ZAH: 17,
    AIN: 18,
    GHAIN: 19,
    FEH: 20,
    QAF: 21,
    KAF: 22,
    LAM: 23,
    MEEM: 24,
    NOON: 25,
    HEH: 26,
    WAW: 27,
    YEH: 28,
    HAMZA: 29,

    ALEF_MADDA: 29,
    ALEF_HAMZA_ABOVE: 29,
    WAW_HAMZA: 29,
    ALEF_HAMZA_BELOW: 29,
    YEH_HAMZA: 29,
}
NAMES = {
    ALEF: "ألف",
    BEH: "باء",
    TEH: 'تاء',
    TEH_MARBUTA: 'تاء مربوطة',
    THEH: 'ثاء',
    JEEM: 'جيم',
    HAH: 'حاء',
    KHAH: 'خاء',
    DAL: 'دال',
    THAL: 'ذال',
    REH: 'راء',
    ZAIN: 'زاي',
    SEEN: 'سين',
    SHEEN: 'شين',
    SAD: 'صاد',
    DAD: 'ضاد',
    TAH: 'طاء',
    ZAH: 'ظاء',
    AIN: 'عين',
    GHAIN: 'غين',
    FEH: 'فاء',
    QAF: 'قاف',
    KAF: 'كاف',
    LAM: 'لام',
    MEEM: 'ميم',
    NOON: 'نون',
    HEH: 'هاء',
    WAW: 'واو',
    YEH: 'ياء',
    HAMZA: 'همزة',

    TATWEEL: 'تطويل',
    ALEF_MADDA: 'ألف ممدودة',
    ALEF_MAKSURA: 'ألف مقصورة',
    ALEF_HAMZA_ABOVE: 'همزة على الألف',
    WAW_HAMZA: 'همزة على الواو',
    ALEF_HAMZA_BELOW: 'همزة تحت الألف',
    YEH_HAMZA: 'همزة على الياء',
    FATHATAN: 'فتحتان',
    DAMMATAN: 'ضمتان',
    KASRATAN: 'كسرتان',
    FATHA: 'فتحة',
    DAMMA: 'ضمة',
    KASRA: 'كسرة',
    SHADDA: 'شدة',
    SUKUN: 'سكون',
}

QURAN_SURAS = {
'آلعمران'
:3
    ,
 'غافر'
:40
    ,
 'الروم'
:30
    ,
 'يونس'
:10
    ,
 'مريم'
:19
    ,
 'فصلت'
:41
    ,
 'العراف'
:7
    ,
 'القيامة'
:75
    ,
 'الواقعة'
:56
    ,
 'الصافات'
:37
    ,
 'الكهف'
:18
    ,
 'الأنبياء'
:21
    ,
 'البقرة'
:2
    ,
 'الأحزاب'
:33
    ,
 'الأحقاف'
:46
    ,
 'المائدة'
:5
    ,
 'التحريم'
:66
    ,
 'البينة'
:98
    ,
 'الجاثية'
:45
    ,
 'الحجر'
:15
    ,
 'السجدة'
:32
    ,
 'التكوير'
:81
    ,
 'الفاتحة'
:1
    ,
 'النحل'
:16
    ,
 'النور'
:24
    ,
 'ق'
:50
    ,
 'الأنفال'
:8
    ,
 'الزلزال'
:99
    ,
 'الإسراء'
:17
    ,
 'الزخرف'
:43
    ,
 'الرعد'
:13
    ,
 'الرحمن'
:55
    ,
 'القصص'
:28
    ,
 'التوبة'
:9
    ,
 'العنكبوت'
:29
    ,
 'النمل'
:27
    ,
 'فاطر'
:35
    ,
 'الحديد'
:57
    ,
 'الفتح'
:48
    ,
 'الفرقان'
:25
    ,
 'لقمان'
:31
    ,
 'نوح'
:71
    ,
 'يس'
:36
    ,
 'ص'
:38
    ,
 'الحشر'
:59
    ,
 'القلم'
:68
    ,
 'يوسف'
:12
    ,
 'المزمل'
:73
    ,
 'الشورى'
:42
    ,
 'الأنعام'
:6
    ,
 'الزمر'
:39
    ,
 'عبس'
:80
    ,
 'الحج'
:22
    ,
 'الفجر'
:89
    ,
 'محمد'
:47
    ,
 'سبأ'
:34
    ,
 'النازعات'
:79
    ,
 'الشعراء'
:26
    ,
 'طه'
:20
    ,
 'النساء'
:4
    ,
 'الإخلاص'
:112
    ,
 'هود'
:11
    ,
 'ابراهيم'
:14
    ,
 'الإسرى'
:17
    ,
'الأعراف'
:7
    ,
'اقتباسيونس'
:10
    ,
'اقتباسيوسف'
:12
    ,
'الأنبيا'
:21
}

def normalize(word):
    sanitized = word
    tobedeleted = [TATWEEL]
    for letter in tobedeleted:
        sanitized = sanitized.replace(letter,"")
    for diacritic in TASHKEEL:
        sanitized = sanitized.replace(diacritic,"")
    foreign = "0123456789,./?;:-_=+"
    for character in foreign:
        sanitized = sanitized.replace(character,"")
    sanitized= sanitized.replace(ALEF+HAMZA_BELOW,ALEF_HAMZA_BELOW)
    sanitized= sanitized.replace(ALEF+HAMZA_ABOVE,ALEF_HAMZA_ABOVE)
    sanitized= sanitized.replace(WAW+HAMZA_ABOVE,WAW_HAMZA)
    sanitized= sanitized.replace(YEH+HAMZA_ABOVE,YEH_HAMZA)
    sanitized= sanitized.replace(ALEF+MADDA_ABOVE,ALEF_MADDA)
    return sanitized

def rasm(word):
    sanitized = word
    for a in ALEFAT:
        # alef_maksura occurs here, and also in 'yehlike'
        sanitized = sanitized.replace(a,ALEF)
    for a in BEHLIKE:
        sanitized = sanitized.replace(a,BEH)
    for a in JEEMLIKE:
        sanitized = sanitized.replace(a,HAH)
    for a in DALLIKE:
        sanitized = sanitized.replace(a,DAL)
    for a in REHLIKE:
        sanitized = sanitized.replace(a,REH)
    for a in SEENLIKE:
        sanitized = sanitized.replace(a,SEEN)
    for a in SADLIKE:
        sanitized = sanitized.replace(a,SAD)
    for a in TAHLIKE:
        sanitized = sanitized.replace(a,TAH)
    for a in AINLIKE:
        sanitized = sanitized.replace(a,AIN)
    for a in FEHLIKE:
        sanitized = sanitized.replace(a,FEH)
    for a in WAWLIKE:
        sanitized = sanitized.replace(a,WAW)
    for a in YEHLIKE:
        sanitized = sanitized.replace(a,YEH)
    if len(sanitized) > 2 and (sanitized[0] == WAW or sanitized[0] == BEH):
        sanitized = sanitized[1:]
    return sanitized
        