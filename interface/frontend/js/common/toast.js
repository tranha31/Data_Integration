
/**
 * Hiển thị toast
 * @param {Object} param0 nội dung toast, kiểu toast, thời gian 
 */
function toast({ title = '', type = 'info', duration = 3000 }) {
    const main = document.getElementById("toast");
    if (main) {
        const toast = document.createElement("div");
        //auto remove toast
        const autoRemove = setTimeout(function () {
            main.removeChild(toast);
        }, duration + 1000);

        toast.onclick = function (e) {
            if (e.target.closest('.delete-toast')) {
                main.removeChild(toast);
                clearTimeout(autoRemove);
            }
        }
        const delay = (duration / 1000).toFixed(2);
        const icons = {
            success: 'fas fa-check-circle',
            info: 'fas fa-info-circle',
            warning: 'fas fa-exclamation-circle',
            error: 'fas fa-exclamation-triangle',

        }
        toast.classList.add("toast-message");
        toast.style.animation = `slideInLeft ease .5s, fadeOut linear 1s ${delay}s forwards`;
        toast.innerHTML = `
            <div class="icon-toast toast-${type}" id="icon-toast">
                <i class="${icons[type]}"></i>
            </div>
            <div class="content-toast" id="content-toast">${title}</div>
            <div class="delete-toast toast-${type}" id="delete-toast">
                <i class="fas fa-times"></i>
            </div>`;
        main.appendChild(toast);

    }
}
