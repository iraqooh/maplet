const openModalLink = document.getElementById('openModal');
const modal = document.getElementById('modal');

openModalLink.addEventListener('click', function(event) {
    event.preventDefault();
    modal.style.display = 'block'
});

const closeModalButton = document.getElementById("closeModal")
closeModalButton.addEventListener('click', function() {
    modal.style.display = 'none'
});

document.getElementById("deleteAccount").addEventListener('click', function(){
    document.getElementById("deletePrompt").style.display = 'block'
})

document.getElementById("cancel").addEventListener('click', function(){
    document.getElementById("deletePrompt").style.display = 'none'
})

document.getElementById("confirm").addEventListener('click', function(){
    window.location.href('/delete_account')
})

