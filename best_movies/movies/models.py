from django.db import models


class Movie(models.Model):
    """Модель для фильмов, вклюячающая картинку"""
    poster = models.ImageField(upload_to='')
    name = models.CharField(max_length=500)
    director = models.CharField(max_length=300, blank=True)
    year = models.CharField(max_length=4, blank=True)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()


class LastRefresh(models.Model):
    """Модель для даты последнего обновления списка фильмов"""
    time = models.DateTimeField(auto_now_add=True)

    def text(self):
        """Возврат строкового представления времени с +3 часовым поясом чтобы не заморачиваться с локалями"""
        # если часовой пояс по умолчанию правильный
        # return self.time.strftime('(%H:%M:%S, %d.%m.%y г.)')
        hour = int(self.time.strftime('%H'))
        msk_timezone_hour = ((list(range(3, 24)) + [0, 1, 2])[hour])
        tmp = self.time.strftime(':%M:%S, %d.%m.%y г.')
        return '(обновлено ' + str(msk_timezone_hour) + tmp + ')'
