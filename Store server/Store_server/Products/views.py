from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'title':'Title`s store',
        'user_name':'qwerty',
        'promo': True,
    }
    
    return render(request, 'Product\index.html', context)

def products(request):
    context = {
        'title':'Store - Каталог товаров',
        'user_name':'qwerty',
        'products_item': [
            {
                'name' : 'Худи черного цвета с монограммами adidas Originals',
                'desc' : 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 
                'image' : "/static/vendor/img/products/Adidas-hoodie.png",
                'price' : '6 090,00'
            },
            {
                'name' : 'Синяя куртка The North Face',
                'desc' : 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.', 
                'image' : "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
                'price' : '23 725,00',
            },
             {
                'name' : 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'desc' : 'Материал с плюшевой текстурой. Удобный и мягкий..', 
                'image' : "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
                'price' : '3 390,00 руб.',
            },
             {
                'name' : 'Черный рюкзак Nike Heritage',
                'desc' : 'Плотная ткань. Легкий материал.', 
                'image' : "/static/vendor/img/products/Black-Nike-Heritage-backpack.png",
                'price' : '2 340,00',
            }
        ]
    }
    return render(request, 'Product\products.html', context)
