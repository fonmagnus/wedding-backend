from django.contrib.postgres.fields import JSONField
from django.db import models
from root.modules.generic.models import BaseModel
import random, string

# Create your models here.
class Invitee(BaseModel):
  name = models.CharField(max_length=512, db_index=True)
  code = models.CharField(max_length=256, db_index=True, editable=False)
  quota = models.IntegerField(default=1)
  is_attended = models.BooleanField(default=False)
  message_from_bride = models.TextField(null=True, blank=True)

  def random_alphanumeric_string(self, length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))
  
  def __str__(self):
    return f'{self.name} - {self.code}'

  def save(self):
    if self.code == None or len(self.code) == 0:
      self.code = self.random_alphanumeric_string(9)

    super().save()


class MessageToBride(BaseModel):
  invitee = models.ForeignKey(Invitee, on_delete=models.CASCADE)
  message = models.TextField()

  def __str__(self):
    return f'Message from {self.invitee.name}'
  

class Activity(BaseModel):
  class ActivityChoices(models.TextChoices):
    BLACK = 'black'
    RED = 'red'
    ORANGE = 'orange'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'
    VIOLET = 'violet'
    PINK = 'pink'
    WHITE = 'white'
  
  type = models.CharField(max_length=256, choices=ActivityChoices.choices)
  content = models.JSONField(null=True, blank=True, default=dict)
  
  def __str__(self):
    return self.type

  class PropertyOrange:
    questions = [
      {
        'slug': 'who-is-the-more-responsible',
        'EN_text': 'Who is the more responsible one?',
        'ID_text': 'Siapa yang lebih bertanggung jawab?',
        'EN_adj': 'Responsible',
        'ID_adj': 'Tanggung Jawab'
      }, 
      {
        'slug': 'who-is-the-more-caring-one',
        'EN_text': 'Who is the more caring one?',
        'ID_text': 'Siapa yang lebih perhatian?',
        'EN_adj': 'Caring',
        'ID_adj': 'Perhatian'
      },
      {
        'slug': 'who-is-the-more-sarcastic',
        'EN_text': 'Who is the more sarcastic one?',
        'ID_text': 'Siapa yang lebih sarkas (suka menyindir)?',
        'EN_adj': 'Sarcastic',
        'ID_adj': 'Sarkas'
      },
      {
        'slug': 'who-is-the-more-romantic',
        'EN_text': 'Who is the more romantic one?',
        'ID_text': 'Siapa yang lebih romantis?',
        'EN_adj': 'Romantic',
        'ID_adj': 'Romantis'
      },
      {
        'slug': 'who-is-more-likely-to-fall-asleep',
        'EN_text': 'Who is more likely to fall asleep?',
        'ID_text': 'Siapa yang lebih mungkin ketiduran duluan?',
        'EN_adj': 'Fall Asleep Faster',
        'ID_adj': 'Tertidur Cepat'
      },
      {
        'slug': 'who-is-the-more-consumptive',
        'EN_text': 'Who is the more consumptive one?',
        'ID_text': 'Siapa yang lebih boros?',
        'EN_adj': 'Consumptive',
        'ID_adj': 'Boros'
      },
      {
        'slug': 'who-is-the-more-organized',
        'EN_text': 'Who is the more organized one?',
        'ID_text': 'Siapa yang lebih terstruktur?',
        'EN_adj': 'Organized',
        'ID_adj': 'Terstruktur'
      },
      {
        'slug': 'who-is-the-more-simp',
        'EN_text': 'Who is the more simp one?',
        'ID_text': 'Siapa yang lebih bucin?',
        'EN_adj': 'Simp',
        'ID_adj': 'Bucin'
      },
      {
        'slug': 'who-is-the-more-adventurous',
        'EN_text': 'Who is the more adventurous one?',
        'ID_text': 'Siapa yang lebih berjiwa petualang?',
        'EN_adj': 'Adventurous',
        'ID_adj': 'Petualang'
      },
      {
        'slug': 'who-is-the-more-rubber-time',
        'EN_text': 'Who is the more \'rubber time\' one?',
        'ID_text': 'Siapa yang lebih ngaret?',
        'EN_adj': 'Rubber time',
        'ID_adj': 'Ngaret'
      },
      {
        'slug': 'who-is-the-more-k-drama-lovers',
        'EN_text': 'Who is the more K-Drama Lovers?',
        'ID_text': 'Siapa yang lebih suka Drakor (Drama Korea)?',
        'EN_adj': 'K-Drama',
        'ID_adj': 'Drakor'
      },
      {
        'slug': 'who-is-the-more-creative',
        'EN_text': 'Who is the more creative one?',
        'ID_text': 'Siapa yang lebih kreatif?',
        'EN_adj': 'Creative',
        'ID_adj': 'Kreatif'
      },
      {
        'slug': 'who-is-the-more-likely-to-be-loved-by-animals',
        'EN_text': 'Who is more likely to be loved by animals?',
        'ID_text': 'Siapa yang lebih mungkin dicintai binatang?',
        'EN_adj': 'Animal Fans',
        'ID_adj': 'Dicintai Binatang'
      },
      {
        'slug': 'who-is-the-more-mature',
        'EN_text': 'Who is the more mature one?',
        'ID_text': 'Siapa yang lebih dewasa?',
        'EN_adj': 'Mature',
        'ID_adj': 'Dewasa'
      },
      {
        'slug': 'who-is-the-more-cool',
        'EN_text': 'Who is the more \'stay cool\' one?',
        'ID_text': 'Siapa yang lebih jaim?',
        'EN_adj': 'Stay Cool',
        'ID_adj': 'Jaim'
      },
      {
        'slug': 'who-is-the-more-picky',
        'EN_text': 'Who is the more food picky one?',
        'ID_text': 'Siapa yang lebih suka pilih pilih makanan?',
        'EN_adj': 'Picky',
        'ID_adj': 'Pemilih'
      },
      {
        'slug': 'who-is-the-more-forgetful',
        'EN_text': 'Who is the more forgetful one?',
        'ID_text': 'Siapa yang lebih pelupa?',
        'EN_adj': 'Forgetful',
        'ID_adj': 'Pelupa'
      },
      {
        'slug': 'who-is-the-more-loyal-friend',
        'EN_text': 'Who is the more loyal friend?',
        'ID_text': 'Siapa yang lebih setiakawan?',
        'EN_adj': 'Loyal Friend',
        'ID_adj': 'Setiakawan'
      },
      {
        'slug': 'who-is-the-more-likely-to-lead-a-prayer',
        'EN_text': 'Who is the more likely to lead a prayer?',
        'ID_text': 'Siapa yang lebih sering memimpin doa?',
        'EN_adj': 'Prayful',
        'ID_adj': 'Suka mimpin doa'
      },
      {
        'slug': 'who-is-the-more-mysterious',
        'EN_text': 'Who is the more mysterious one?',
        'ID_text': 'Siapa yang lebih misterius?',
        'EN_adj': 'Mysterious',
        'ID_adj': 'Misterius'
      },
    ]
  
  class PropertyYellow:
    questions = [
      {
        'slug': 'meet-up',
        'EN': {
          'text': 'Where did Arnold and Gaby first interact?',
          'options': [
            'Church event',
            'Dating apps',
            'Instagram',
            'Linkedin'
          ],
          'fact': "Arnold first sent a message to Gaby on Instagram. Seeing the long, deep message, and knowing Arnold likes to write on Instagram, made Gaby think Arnold is someone thoughtful and smart, so she wanted to reply to him.",
          'correct_answer': 'Instagram'
        },
        'ID': {
          'text': 'Dimana pertama kali Arnold dan Gaby berinteraksi?',
          'options': [
            'Acara Gereja',
            'Dating apps',
            'Instagram',
            'Linkedin'
          ],
          'fact': 'Arnold pertama kali mengirimkan pesan ke Instagram Gaby. Melihat pesan yang panjang, dalam, serta Arnold yang suka menulis di Instagram, membuat Gaby berpikir Arnold adalah seseorang yang thoughtful & smart sehingga ia mau membalasnya.',
          'correct_answer': 'Instagram'
        }
      },

      {
        'slug': 'impression',
        'EN': {
          'text': 'What is Arnold\'s First Impression towards Gaby?',
          'options': [
            '"She has a Jaksel (southern Jakarta) vibes"',
            '"She is really shyful"',
            '"Wow.. she looks like a Korean Girl"',
            '"She sure has a lot of appetites"'
          ],
          'fact': "When they first met, Arnold thought Gaby was someone extroverted (because she was quite talkative) and looked like an indie person (maybe because she was wearing a hat).",
          'correct_answer': '"She has a Jaksel (southern Jakarta) vibes"'
        },
        'ID': {
          'text': 'Apa kesan pertama Arnold pada Gaby?',
          'options': [
            '"Vibes anak indie jaksel nih"',
            '"Pemalu dan pendiam ya anaknya"',
            '"Wow.. kayak cewek korea"',
            '"Kecil-kecil makannya banyak juga ya.."'
          ],
          'fact': 'Ketika mereka pertama kali bertemu, Arnold berpikir Gaby adalah seseorang yang extrovert (karena cukup bawel) dan terllihat seperti anak indie (karena memakai topi).',
          'correct_answer': '"Vibes anak indie jaksel nih"'
        }
      },

      {
        'slug': 'first-date-movie',
        'EN': {
          'text': 'What is the genre of the first movie they watch together during the date?',
          'options': [
            'Horror',
            'Romance',
            'Comedy',
            'Biography'
          ],
          'fact': "They first watched a movie together at the 'Subtitles' film studio in Dharmawangsa (which is now permanently closed). Arnold chose the movie 'Dark Water' (2002). The movie was bad, the food was more interesting.",
          'correct_answer': 'Horror'
        },
        'ID': {
          'text': 'Genre film apa yang pertama kali mereka tonton saat PDKT',
          'options': [
            'Horor',
            'Romantis',
            'Komedi',
            'Biografi'
          ],
          'fact': 'Mereka pertama kali menonton berdua di studio film “Subtitles” Dharmawangsa (sekarang sudah tutup permanen). Arnold memilih film “Dark Water” (2002). Film-nya jelek, makanannya lebih menarik.',
          'correct_answer': 'Horor'
        }
      },

      {
        'slug': 'favorite-character',
        'EN': {
          'text': 'What is Arnold\'s favorite character?',
          'options': [
            'Naruto',
            'Rilakkuma',
            'Pepe the Frog',
            'Batman'
          ],
          'fact': "Although he appears cold, Arnold really likes the character Rilakkuma, a chubby bear who lives life in a relaxed manner. He collects many Rilakkuma pillows and plushies, along with his friends like Korilakkuma, Kiroiitori, and Koguma.",
          'correct_answer': 'Rilakkuma'
        },
        'ID': {
          'text': 'Apa karakter kesukaan Arnold?',
          'options': [
            'Naruto',
            'Rilakkuma',
            'Pepe the Frog',
            'Batman'
          ],
          'fact': 'Walau terlihat dingin, Arnold sangat menyukai karakter Rilakkuma, beruang gendut yang menjalani hidupnya dengan santai. Ia mengoleksi banyak bantal dan boneka Rilakkuma beserta teman-temannya seperti Korilakkuma, Kiroiitori, dan Koguma.',
          'correct_answer': 'Rilakkuma'
        }
      },

      {
        'slug': 'relationship',
        'EN': {
          'text': 'How long Arnold and Gaby have been in a relationship until the wedding day?',
          'options': [
            '0 - 1 years',
            '1 - 2 years',
            '2 - 3 years',
            '3 - 4 years'
          ],
          'correct_answer': '2 - 3 years',
          'fact': 'As mentioned in the red section, they started dating on May 7, 2021. Thus, they got married after dating for 2 years and 362 days.'
        },
        'ID': {
          'text': 'Berapa lama Arnold dan Gaby berpacaran sebelum hari pernikahan kami?',
          'options': [
            '0 - 1 tahun',
            '1 - 2 tahun',
            '2 - 3 tahun',
            '3 - 4 tahun'
          ],
          'correct_answer': '2 - 3 tahun',
          'fact': 'Seperti yang sudah disebutkan pada bagian warna merah, mereka berpacaran pada 07 Mei 2021. Sehingga mereka menikah setelah 2 tahun dan 362 hari berpacaran.'
        }
      },

      {
        'slug': 'confession',
        'EN': {
          'text': "Where is the firsst time Arnold confessed his feeling to Gaby?",
          'options': [
            'Ferris Wheel',
            'Top of a Skyscraper',
            'Saint Mary Chapel',
            'Car'
          ],
          'fact': "Arnold confessed his feelings at a rooftop bar located in the tower where Gaby works, while they were looking at the city lights at night.",
          'correct_answer': 'Top of a Skyscraper'
        },
        'ID': {
          'text': 'Dimana Arnold pertama kali menyatakan perasaannya?',
          'options': [
            'Di dalam bianglala',
            'Di lantai atas gedung tinggi',
            'Di Gua Maria',
            'Di mobil'
          ],
          'fact': 'Arnold menyatakan perasaannya di sebuah rooftop bar yang terletak di menara tempat Gaby bekerja, saat mereka sedang melihat lampu-lampu kota di malam hari.',
          'correct_answer': 'Di lantai atas gedung tinggi'
        }
      },

      {
        'slug': 'retirement',
        'EN': {
          'text': "What is Arnold's retirement dream?",
          'options': [
            'Nurturing a lot of children',
            'Becoming a NASA volunteer',
            'Enjoying the rich life with enormous wealth',
            'Becoming a shepherd to play with sheep'
          ],
          'fact': "Arnold aspires to live in a serene place far from the hustle and bustle. Spending his retirement stroking soft sheep's wool while sitting on a spread of green grass would feel very satisfying.",
          'correct_answer': 'Becoming a shepherd to play with sheep'
        },
        'ID': {
          'text': 'Jika pensiun, apa cita-cita Arnold?',
          'options': [
            'Mengangkat banyak anak asuh',
            'Menjadi relawan dalam misi NASA',
            'Menikmati hidup mewah dan berlimpah harta',
            'Menjadi penggembala domba untuk bermain'
          ],
          'fact': 'Arnold bercita-cita tinggal di tempat yang asri dan jauh dari keramaian. Menghabiskan masa pensiun dengan memegang bulu domba yang halus sambil duduk di hamparan rumput hijau akan terasa sangat satisfying.',
          'correct_answer': 'Menjadi penggembala domba untuk bermain'
        }
      },

      {
        'slug': 'korean-drama',
        'EN': {
          'text': 'Arnold often persuade Gaby to watch a Korean Drama that he thinks wonderful. What K-Drama is that?',
          'options': [
            'Reply 1988',
            'Hi, Bye Mama!',
            'Sky Castle',
            'Extraordinary Attorney Woo'
          ],
          'correct_answer': 'Hi, Bye Mama!',
          'fact': 'Arnold enjoys several Korean dramas, but the one that touched him the most is "Hi Bye, Mama!". He often persuades Gaby, who is less interested in Korean dramas, to watch it with him.'
        },
        'ID': {
          'text': 'Arnold sering membujuk Gaby untuk menonton Drakor yang menurutnya bagus. Drakor apakah itu?',
          'options': [
            'Reply 1988',
            'Hi, Bye Mama!',
            'Sky Castle',
            'Extraordinary Attorney Woo'
          ],
          'correct_answer': 'Hi, Bye Mama!',
          'fact': 'Arnold menyukai beberapa drama Korea, tetapi yang paling menyentuhnya adalah drakor “Hi Bye, Mama!”. Ia sering membujuk Gaby yang kurang tertarik dengan drakor untuk menontonnya.'
        }
      },

      {
        'slug': 'restaurant',
        'EN': {
          'text': 'Which of these restaurants is visited the least often?',
          'options': [
            'Dewata by Monsieur Spoon',
            'Steak 21',
            'Sushi Tei',
            'Sentosa Seafood'
          ],
          'correct_answer': 'Sushi Tei',
          'fact': 'Arnold likes chicken steak, while Gaby prefers sushi. Both of them enjoy Chinese food and seafood. However, the sushi place they often visit is Sushi Hiro, not Sushi Tei.'
        },
        'ID': {
          'text': 'Di antara restoran-restoran ini, mana yang paling jarang mereka datangi',
          'options': [
            'Dewata by Monsieur Spoon',
            'Steak 21',
            'Sushi Tei',
            'Sentosa Seafood'
          ],
          'correct_answer': 'Sushi Tei',
          'fact': 'Arnold menyukai steak ayam, Gaby menyukai sushi. Keduanya menyukai Chinese food dan Seafood. Walau begitu, sushi yang mereka sering datangi adalah Sushi Hiro, bukan  Sushi Tei.'
        }
      },

      
      {
        'slug': 'character',
        'EN': {
          'text': 'Of which traits of Gaby that Arnold mostly liked?',
          'options': [
            'Kind-hearted',
            'Creative',
            'Good Listener and understanding',
            'Random and weird'
          ],
          'correct_answer': 'Random and weird',
          'fact': 'We kinda share the same randomness and weirdness'
        },
        'ID': {
          'text': 'Apa karakter dari Gaby yang paling disukai Arnold?',
          'options': [
            'Baik hati',
            'Kreatif',
            'Pendengar yang baik dan memahami',
            'Random dan aneh'
          ],
          'correct_answer': 'Random dan aneh',
          'fact': 'Kita cukup memiliki tingkat kerandoman yang mirip'
        }
      },

      {
        'slug': 'moments',
        'EN': {
          'text': 'Arnold and Gaby have been in all of these moments EXCEPT : ',
          'options': [
            'Getting lost in an unknown road at midnight',
            'Missed the last train',
            'Riding a bajaj',
            'Dating in museum'
          ],
          'correct_answer': 'Dating in museum',
          'fact': 'They once got stuck in PIK2 during its construction phase, so they had to detour through truck routes and dirt roads to get home. They also missed the last train and, with their phone batteries drained, had to walk in search of a way back to their hotel while on a family trip in Singapore. Additionally, they have ridden a bajaj in Jakarta. However, they have never had a date at a museum.'
        },
        'ID': {
          'text': 'Momen momen ini pernah dilalui mereka berdua KECUALI?',
          'options': [
            'Tersesat di tengah malam',
            'Ketinggalan kereta terakhir',
            'Naik bajaj di Jakarta',
            'Kencan di museum'
          ],
          'correct_answer': 'Kencan di museum',
          'fact': 'Mereka pernah terjebak di PIK2 saat masih pembangunan sehingga harus memutar lewat jalur truk dan jalanan bertanah merah untuk pulang. Mereka pernah melewatkan kereta terakhir dan dengan kehabisan baterai, berjalan kaki mencari jalan pulang menuju hotel saat sedang jalan-jalan keluarga di Singapura. Mereka juga pernah naik bajaj di Jakarta. Namun, mereka belum pernah kencan ke museum.'
        }
      },

      {
        'slug': 'sad',
        'EN': {
          'text': 'Which one of these made Arnold discouraged the most?',
          'options': [
            'If Gaby is being clumsy',
            'If Gaby getting too closed with other boys',
            'If Gaby went back home after staying in Arnold\'s parent\'s home',
            'If Gaby is being cranky'
          ],
          'correct_answer': 'If Gaby went back home after staying in Arnold\'s parent\'s home',
          'fact': "Arnold prefers meeting and communicating in person, so when Gaby has to return home, he feels sad and as if he's lost a kindred spirit."
        },
        'ID': {
          'text': 'Di antara hal di bawah ini, mana hal yang membuat Arnold sebal?',
          'options': [
            'Kalau Gaby berbuat hal ceroboh',
            'Kalau Gaby terlalu dekat dengan lawan jenis',
            'Kalau Gaby pulang ke rumah',
            'Kalau Gaby mulai merajuk dan ngambek'
          ],
          'correct_answer': 'Kalau Gaby pulang ke rumah',
          'fact': 'Arnold lebih suka bertemu dan berkomunikasi secara langsung sehingga jika Gaby harus pulang ke rumah, ia sedih dan merasa teman sefrekuensinya hilang.'
        }
      },

      {
        'slug': 'fruits-fruits',
        'EN': {
          'text': "Gaby suka dan hampir setiap hari makan buah.",
          'options': [
            'True',
            'False'
          ],
          'correct_answer': 'True',
          'fact': 'If she skips eating fruits, Gaby tends to easily suffer from inflammation and mouth ulcers. Therefore, she almost daily buys fruits, or her mother always brings her some.'
        },
        'ID': {
          'text': 'Gaby suka dan hampir setiap hari makan buah.',
          'options': [
            'Benar',
            'Salah'
          ],
          'correct_answer': 'Benar',
          'fact': 'Jika absen memakan buah, Gaby akan mudah terserang radang dan sariawan sehingga hampir setiap hari ia beli/ sang mama selalu membawakannya buah-buahan.'
        }
      },

      
      {
        'slug': 'no-gay',
        'EN': {
          'text': "Arnold once dated a classmate during his high school years.",
          'options': [
            'True',
            'False'
          ],
          'correct_answer': 'False',
          'fact': 'During his high school years, Arnold attended an all-boys school, so there was no one at school who caught his interest for dating.'
        },
        'ID': {
          'text': 'Arnold pernah berpacaran dengan teman sekelasnya saat SMA.',
          'options': [
            'Benar',
            'Salah'
          ],
          'correct_answer': 'Salah',
          'fact': 'Sewaktu SMA, Arnold bersekolah di sekolah khusus laki-laki, sehingga tidak ada yang menarik baginya di sekolah untuk dipacari.'
        }
      },

      
      {
        'slug': 'fear',
        'EN': {
          'text': "Gaby is more afraid of heights than she is of cockroaches.",
          'options': [
            'True',
            'False'
          ],
          'correct_answer': 'True',
          'fact': 'Gaby is not afraid of insects. However, she feels faint when looking down from a certain height. She also dislikes extreme rides at amusement parks.'
        },
        'ID': {
          'text': 'Gaby lebih takut ketinggian dibanding dengan kecoak.',
          'options': [
            'Benar',
            'Salah'
          ],
          'correct_answer': 'Benar',
          'fact': 'Gaby tidak takut serangga. Akan tetapi, ia lemas jika melihat ke bawah dari ketinggian tertentu. Ia juga tidak suka dengan wahana ekstrem di taman hiburan.'
        }
      },

      {
        'slug': 'morning',
        'EN': {
          'text': "Arnold is a morning person, someone who wakes up early.",
          'options': [
            'True',
            'False'
          ],
          'correct_answer': 'True',
          'fact': 'Arnold is the earliest riser in his family and enjoys attending morning mass.'
        },
        'ID': {
          'text': 'Arnold adalah orang yang bangunnya pagi/ morning person',
          'options': [
            'Benar',
            'Salah'
          ],
          'correct_answer': 'Benar',
          'fact': 'Arnold menjadi orang yang bangun terpagi di keluarganya, ia suka ikut misa pagi.'
        }
      },

      {
        'slug': 'mbti',
        'EN': {
          'text': "Gaby is a woman who is more dominated by logic than emotion.",
          'options': [
            'True',
            'False'
          ],
          'correct_answer': 'False',
          'fact': 'Gaby is an INFJ in the MBTI personality. She is someone with sensitive feelings and enjoys understanding others and the situations around her.'
        },
        'ID': {
          'text': 'Gaby termasuk cewek yang didominasi logika ketimbang perasaan',
          'options': [
            'Benar',
            'Salah'
          ],
          'correct_answer': 'Salah',
          'fact': 'Gaby adalah seorang INFJ pada kepribadian MBTI. Ia orang dengan perasaan peka dan senang membaca orang lain ataupun situasi di sekitarnya.'
        }
      },

      {
        'slug': 'chindo',
        'EN': {
          'text': "Arnold can speak the Hakka (Khek) language.",
          'options': [
            'True',
            'False'
          ],
          'correct_answer': 'False',
          'fact': 'As a Chinese Indonesian (Chindo), Arnold cannot speak Mandarin or any regional Chinese language. He only sometimes pretends to have an accent and teases Chinese people.'
        },
        'ID': {
          'text': 'Arnold bisa berbicara bahasa Hakka/ Khek.',
          'options': [
            'Benar',
            'Salah'
          ],
          'correct_answer': 'Salah',
          'fact': 'Sebagai seorang Chindo, Arnold tidak bisa berbicara bahasa mandarin/ bahasa Chinese daerah apapun. Hanya terkadang ia berpura-pura berlogat dan meledek orang China.'
        }
      },

      {
        'slug': 'coffee',
        'EN': {
          'text': "When extremely sleepy, Gaby copes with it by drinking coffee.",
          'options': [
            'True',
            'False'
          ],
          'correct_answer': 'False',
          'fact': 'Gaby does not like and cannot drink coffee because she finds the aftereffects unpleasant.'
        },
        'ID': {
          'text': 'Kalau lagi ngantuk banget, Gaby mengatasinya dengan kopi.',
          'options': [
            'Benar',
            'Salah'
          ],
          'correct_answer': 'Salah',
          'fact': 'Gaby tidak suka dan tidak bisa minum kopi karena sensasi setelahnya yang tidak mengenakkan baginya.'
        }
      },

      {
        'slug': 'college',
        'EN': {
          'text': "Arnold spent 10 years in his undergraduate studies.",
          'options': [
            'True',
            'False'
          ],
          'correct_answer': 'True',
          'fact': 'Like other intelligent individuals who struggle with administrative tasks and academic rules, so do Arnold'
        },
        'ID': {
          'text': 'Arnold menghabiskan waktu selama 10 tahun di S1.',
          'options': [
            'Benar',
            'Salah'
          ],
          'correct_answer': 'Benar',
          'fact': 'Seperti orang pintar lainnya yang kurang cocok dengan berbagai administrasi dan aturan-aturan akademis, begitulah Arnold'
        }
      },
    ]

class ActivityResponse(BaseModel):
  invitee = models.ForeignKey(Invitee, on_delete=models.CASCADE)
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  response = models.JSONField(null=True, blank=True, default=dict)

  def __str__(self):
    return f'{self.activity} - {self.invitee}'