from router.userRouter import userRouter
from router.authRouter import authRouter
from router.ClotheRouter import clotheRouter

def setRoutes(app):
    app.include_router(userRouter)
    app.include_router(authRouter)
    app.include_router(clotheRouter)