from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Uuid, Text, DateTime, Enum, Boolean
import uuid
from sqlalchemy import Enum as SQLAlchemyEnum


# lazy='select': Load dữ liệu khi truy cập (mặc định).
# lazy='dynamic': Trả về query object, phù hợp khi cần lọc thêm.
# lazy='joined': Thực hiện JOIN để load dữ liệu liên quan ngay lập tức.
# lazy='subquery': Tương tự joined nhưng dùng subquery.

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(String(38), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    create_at = Column(DateTime, default=db.func.now())
    update_at = Column(DateTime, default=db.func.now(), onupdate=db.func.now())


response_tags = db.Table('response_tags',
                         Column("response_id", String(38),
                                ForeignKey("responses.id", onupdate="cascade", ondelete="cascade"),
                                primary_key=True),
                         Column("tag_id", String(38), ForeignKey("tags.id", onupdate="cascade", ondelete="cascade"),
                                primary_key=True))


class User(BaseModel):
    __tablename__ = 'users'
    username = Column(String(80))
    email = Column(String(80), unique=True)
    avatar = Column(String(255), nullable=True)
    google_id = Column(String(255))
    gender = Column(SQLAlchemyEnum('male', 'female', 'other', name='gender_enum', native_enum=False), default='other')
    status = Column(SQLAlchemyEnum('active', 'banned', name='user_status_enum', native_enum=False), default='active')
    admin = Column(Boolean, default=False)
    response = db.relationship("Response", backref="user", lazy="dynamic", cascade="all, delete-orphan")


def __str__(self):
    return self.username or self.email or str(self.id)


class Response(BaseModel):
    __tablename__ = 'responses'
    title = Column(String(255))
    content = Column(Text)
    status = Column(Enum('public', 'private'), default='private')
    user_id = Column(String(38), ForeignKey('users.id', onupdate="cascade", ondelete="cascade"), nullable=False,
                     index=True)
    vote = Column(Integer, default=0)
    tags = db.relationship("Tag", secondary=response_tags, backref=db.backref("responses", lazy="joined"))
    user = db.relationship("User", backref="responses", lazy="joined")


class Tag(BaseModel):
    __tablename__ = 'tags'
    name = Column(String(80), unique=True, index=True)
