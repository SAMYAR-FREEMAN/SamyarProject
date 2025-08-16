from models.roleModel import Role
from models.userModel import user
def init_base_data():
    roles = list(Role.objects().as_pymongo())
    if len(roles) == 0:
        owner_role =  Role(name="Owner").save()
        Role(name="Admin").save()
        Role(name="Buyer").save()
        Role(name="Seller").save()
        print(owner_role.to_mongo().to_dict())

        owner_data = {
            "full_name": "Samyar naeimi",
            "email": "samyar.n2010@gmail.com",
            "password": "password",
            "role": owner_role
        }
        owner_user = user(**owner_data).save()
