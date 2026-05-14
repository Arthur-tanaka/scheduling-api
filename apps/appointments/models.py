from django.db import models

class Appointment(models.Model):
    
    class Status(models.TextChoices):
    
        SCHEDULED = 'scheduled', 'Agendado'
        COMPLETED = 'completed', 'Concluído'
        CANCELED = 'canceled', 'Cancelado'
        
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED)

    def __str__(self):
        return f'{self.user.name} - {self.service.name} - {self.appointment_date}'