function signIn(word) {
    word.textContent = "Logout"
}

var count = 0;
function moreLikes(button) {
    count++;
    console.log(count);
    if (count === 0) {
        button.textContent = " 0 Likes"
    }
    else if (count === 1) {
        button.innerText = `${count} Like`
    }
    else if (count >= 2) {
        button.innerText = `${count} Likes`
    }

    alert("Ninja was Liked")
}

var diffCount = 0
function differentLikes(button) {
    diffCount++;
    console.log(diffCount);
    if (diffCount === 0) {
        button.textContent = " 0 Likes"
    }
    else if (diffCount === 1) {
        button.innerText = `${diffCount} Like`
    }
    else if (diffCount >= 2) {
        button.innerText = `${diffCount} Likes`
    }

    alert("Ninja was Liked")
}

var button = document.querySelector("#remove")
function remove() {
    button.remove();
}