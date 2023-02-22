from fastapi_mail import ConnectionConfig, MessageSchema, MessageType, FastMail
from pydantic import EmailStr
import asyncio

from app.config import settings


class EmailServices:

    conf = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_STARTTLS=False,
        MAIL_SSL_TLS=False,
        MAIL_DEBUG=1
    )

    @staticmethod
    def send_email(email: EmailStr, subject: str, body: str):
        message = MessageSchema(
            subject=subject,
            recipients=[email],
            body=body,
            subtype=MessageType.plain,
        )

        fm = FastMail(EmailServices.conf)
        asyncio.run(fm.send_message(message))

        return


