# dbmsminorproject
full stack website for shopping cart system 

#index.html file 
 <!DOCTYPE html> 
<html lang="en"> 
<head> 
    <meta charset="UTF-8"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Homepage</title> 
    <link rel="stylesheet" href="styles.css">
   
</head> 
<body> 
    <header> 
        <nav> 
            <a href="index.html">Home</a> 
            <a href="cartpage.html">Cart</a> 
            <a href="loginsignuppage.html">Login/Signup</a> 
        </nav> 
    </header> 
    <main> 
        <h1>Products</h1> 
        <section class="product-grid"> 
            <div class="product-item"> 
                <img src="product1.jpeg" alt="Product Image" width="300" height="200"> 
                <h2><br>LAPTOP </h2> 
                <p><br>Price: 70,000</p> 
                <a href="cartpage.html"><button>Add to Cart</button> </a>
            </div> 
            <div class="product-item"> 
                <img src="product2.jpeg" alt="Product Image" width="200" height="100"> 
                <h2>LAPTOP BAG</h2> 
                <p><br>Price: 1,000</p> 
                <a href="cartpage.html"><button>Add to Cart</button> </a>
            </div> 
            <div class="product-item"> 
                <img src="product3.jpeg" alt="Product Image" width="300" height="200"> 
                <h2>MOUSE</h2> 
                <p><br>Price: 500</p> 
                <a href="cartpage.html"><button>Add to Cart</button> </a>
            </div> 
            <div class="product-item"> 
                <img src="product4.jpeg" alt="Product Image" width="300" height="200"> 
                <h2>LAPTOP CAMERA</h2> 
                <p>Price: 2,000</p> 
                <a href="cartpage.html"><button>Add to Cart</button> </a>
            </div> 
            <div class="product-item"> 
                <img src="product5.jpeg" alt="Product Image" width="300" height="200"> 
                <h2>KEYBOARD</h2> 
                <p><br><br>Price: 3,000</p> 
                <a href="cartpage.html"><button>Add to Cart</button> </a>
            </div> 
            <div class="product-item"> 
                <img src="product6.jpeg" alt="Product Image" width="300" height="200"> 
                <h2>PENDRIVE</h2> 
                <p><br>Price: 800</p> 
                <a href="cartpage.html"><button>Add to Cart</button> </a>
            </div> 
            <div class="product-item"> 
                <img src="product7.jpeg" alt="Product Image" width="300" height="200"> 
                <h2>LAPTOP CHARGER</h2> 
                <p>Price: 5,000</p> 
                <a href="cartpage.html"><button>Add to Cart</button> </a>
            </div> 
            <div class="product-item"> 
                <img src="product8.jpeg" alt="Product Image" width="300" height="200"> 
                <h2>POWERBANK</h2> 
                <p><br>Price: 1,500</p> 
                <a href="cartpage.html"><button>Add to Cart</button> </a>
            </div> 
            <div class="product-item"> 
                <img src="product9.jpeg" alt="Product Image" width="300" height="200"> 
                <h2>HEADPHONES</h2> 
                <p>Price: 1,799</p> 
                <a href="cartpage.html"><button>Add to Cart</button> </a>
            </div> 
            <div class="product-item"> 
                <img src="product10.jpeg" alt="Product Image" width="300" height="200"> 
                <h2>LAPTOP STAND</h2> 
                <p>Price: 399</p> 
                <a href="cartpage.html"><button>Add to Cart</button> </a>
            </div> 
            
            <!-- Repeat product items --> 
        </section> 
    </main> 
    <script src="script.js"></script>
</body> 
</html> 
