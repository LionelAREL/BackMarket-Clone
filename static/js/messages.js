console.log("messages moment")

const TIME_LIVE_TOAST = 3000

const deleteAllMessages = (messages) => {
    if(messages){
        Array.from(messages?.children).forEach(message => {
            message.remove()
        });
    }
}

function deleteMessage(){
    this.parentElement.remove()
}

setTimeout(() => {
    const messages = document.querySelector(".messages");
    deleteAllMessages(messages)
},TIME_LIVE_TOAST)


const messages = document.querySelector(".messages");

if(messages){
    Array.from(messages?.children).forEach(message => {
        message.onclick = deleteMessage
    });
}