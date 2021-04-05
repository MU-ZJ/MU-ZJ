const articles = news.articles;
const colWrapper = document.getElementById("colWrapper");

let newsPrint = articles.map(function (article) {
  return ` 
                <div class="card is-mobile">
                    <div class="card-image">
                            <img id='mainImage' src="${article.urlToImage}" onerror="this.style.display='none'">
                    </div>
                    <header class="card-header">
                        <p class="card-header-title">
                            ${article.source.name} -
                            <small>${article.author}</small>
                        </p>
                    </header>
                    <div class="card-content">
                        <div class="media">
                            <div class="media-content">
                                <p class="title is-4">${article.title}</p>
                                <p class="subtitle is-6">${article.description}</p>                       
                            </div>
                        </div>
                        <div class="content">
                            <p>
                            ${article.content}
                            </p>
                            <a href='${article.url}'>Full article</a>
                        </div>
                    </div>
                    <div class="card">
                        <footer class="card-footer">
                            <time>${article.publishedAt}</time>
                        </footer>
                    </div>
                </div> 
    `;
});

colWrapper.innerHTML = newsPrint.join("");