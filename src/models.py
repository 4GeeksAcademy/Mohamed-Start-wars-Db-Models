from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    user_name: Mapped[str] = mapped_column(String(25), nullable= False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name,
            # do not serialize the password, its a security breach
        }



class Character(db.Model):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(String(100),nullable =False)
    eye_color: Mapped[str] = mapped_column(String(40), nullable= False)
    height: Mapped[float] = mapped_column(nullable=True)
    birth_year: Mapped[str] = mapped_column(String(20), nullable=True)
    homeworld_id: Mapped[int] = mapped_column(db.ForeignKey("planet.id"))
    # vehicle_id: Mapped[int] = mapped_column(db.ForeignKey("vehicle.id"))

    # Relationship
    homeworld = db.relationship("Planet", backref="characters")
    favorites = db.relationship("Favorite", backref="character")


class Planet(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    population: Mapped[int] = mapped_column(nullable=True)
    terrain: Mapped[str] = mapped_column(String(100), nullable=True)
    diameter: Mapped[float] = mapped_column(nullable=True)
    rotation_period: Mapped[int] = mapped_column(nullable=True)
    orbital_period: Mapped[int] = mapped_column(nullable=True)
    climate: Mapped[str] = mapped_column(String(100), nullable=True)
    
     # Relatinships
    characters = db.relationship("Character", backref="homeworld")
    favorites = db.relationship("Favorite", backref="planet")
    

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    model: Mapped[str] = mapped_column(String(100), nullable = False)
    vehicle_class: Mapped[str] = mapped_column(String(50), nullable=False)
    pilot_id: Mapped[int] = mapped_column(db.ForeignKey("character.id"), nullable=True)
  
    # Relationship
    # manufacturer = db.relationship("Planet", backref="vehicles")
    pilot = db.relationship("Character", backref="vehicles")
    favorites = db.relationship("Favorite", backref="vehicle")



class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"), nullable=False)
    character_id: Mapped[int] = mapped_column(db.ForeignKey("character.id"), nullable=True)
    planet_id: Mapped[int] = mapped_column(db.ForeignKey("planet.id"), nullable=True)
    vehicle_id: Mapped[int] = mapped_column(db.ForeignKey("vehicle_id"), nullable =True)
    # created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship("User", backref="favorites")
    character = db.relationship("Character", backref="favorites")
    planet = db.relationship("Planet", backref="favorites")
    vehicle = db.relationship("vehicle", backref="vehicle")












    

   