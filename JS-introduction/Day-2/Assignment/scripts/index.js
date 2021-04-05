let newTaskInput = document.getElementById("newTaskInput");
let newTaskButton = document.getElementById("newTaskButton");
let taskWrapperIncomp = document.getElementById("taskWrapperIncomp");
let taskWrapperComp = document.getElementById("taskWrapperComp");

newTaskButton.addEventListener("click", function () {
  let task = newTaskInput.value;
  let taskText = document.createElement("p");
  taskText.className = "title";
  taskText.innerHTML = task;
  let taskArticle = document.createElement("article");
  taskArticle.className = "tile is-parent notification is-info is-flex";
  let taskComplete = document.createElement("input");
  taskComplete.type = "checkbox";
  taskRemove = document.createElement("button");
  taskRemove.className = "delete";
  taskArticle.appendChild(taskRemove);
  taskArticle.appendChild(taskComplete);
  taskArticle.appendChild(taskText);
  taskWrapperIncomp.appendChild(taskArticle);
  newTaskInput.value = ""


  taskComplete.addEventListener("change", function(){
    if(taskArticle.parentElement == taskWrapperComp){
        taskWrapperIncomp.appendChild(this.parentElement)
    }else if(taskArticle.parentElement == taskWrapperIncomp){
        taskWrapperComp.appendChild(this.parentElement)
    }
  })

  taskRemove.addEventListener("click", function () {
    if (taskArticle.parentElement == taskWrapperComp) {
      taskWrapperComp.removeChild(this.parentElement);
    } else if (taskArticle.parentElement == taskWrapperIncomp) {
      taskWrapperIncomp.removeChild(this.parentElement);
    }
  });
});

newTaskInput.addEventListener("keyup", function (event) {
  event.preventDefault();
  if (event.key === "Enter") {
    newTaskButton.click();
  }
});
