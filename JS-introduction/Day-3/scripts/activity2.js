const postWrapper = document.getElementById('postWrapper')

for(let index = 0; index < posts.length; index++) {
    let post = posts[index]
    let postItem = `
    <article class="media">
        <div class="media-content">
          <div class="content">
            <p>
              <strong>UserID:</strong> ${post.userId} <strong>PostID:</strong> ${post.id}
              <br>
              <strong>Subject:</strong> "${post.title}"
              <br>
              ${post.body}
            </p>
          </div>
        </div>
    </article>
    `
    postWrapper.insertAdjacentHTML('beforeend', postItem)
}