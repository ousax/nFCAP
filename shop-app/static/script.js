document.getElementById("mode-toggle").addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    const icon = document.getElementById("mode-toggle");
    icon.textContent = document.body.classList.contains("dark-mode") ? "🌞" : "🌙";
});

// Fetch products from the backend and display them
fetch("/products/")
    .then(response => response.json())
    .then(products => {
        const productList = document.getElementById("product-list");
        products.forEach(product => {
            const productCard = document.createElement("div");
            productCard.classList.add("product-card");

            productCard.innerHTML = `
                <img src="${product.image_url}" class="product-image" alt="${product.name}">
                <div class="product-name">${product.name}</div>
                <div class="product-price">${product.price} ${product.currency}</div>
                <div class="product-rating">⭐ ${product.rating}</div>
            `;
            productList.appendChild(productCard);
        });
    });

