var listROM = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
var listRAM = [2, 4, 3, 8, 12, 16, 32]
var numberPage = 0

if (!String.prototype.format) {
    String.prototype.format = function() {
        var args = arguments;
        return this.replace(/{(\d+)}/g, function(match, number) {
            return typeof args[number] != 'undefined' ?
                args[number] :
                match;
        });
    };
}

$(document).ready(function() {
    loadData(0);
    bindingDataRom()
    bindingDataRam()

});

$("#input0").on('keypress', function(e) {
    if (e.which == 13) {
        loadData(0)
    }
});

/**--------------------------
 * Gọi API lấy dữ liệu
 */
function loadData(page) {
    var nameS = document.getElementById("input0").value;
    var romS = document.getElementById("content-selected0").value;
    var ramS = document.getElementById("content-selected1").value;

    nameS = !nameS ? "" : nameS
    romS = !romS ? "" : romS.substring(0, romS.length - 2)
    ramS = !ramS ? "" : ramS.substring(0, ramS.length - 2)

    $.get('http://127.0.0.1:5000/api/phone', { name: nameS, rom: romS, ram: ramS, currentPage: page })
        .done(function(res) {
            bindingData(res, page)
        })
        .fail(function() {
            toast({
                title: "Tải dữ liệu thất bại",
                type: "error",
                duration: 3000
            });
        });
}


/**
 * Vẽ mấy cái điện thoại ra
 * @param {object} data 
 */
function bindingData(res, page) {
    var totalRecord = res.totalRecord
    var lstData = res.data
    var grid = $(".grid")
    grid.html(null)
    var div = ""
    var formDiv = `
        <div class="phone d-flex flex-column relative">
            <div>
                <div class="img" style="background-image: url('{0}')">
                </div>
            </div>
            
            <div class="name">{1}</div>
            <div class="price">{2}</div>
            <div class="info d-flex flex-column">
                <div>Màu: {3}</div>
                <div>Bộ nhớ: {4}GB</div>
                <div>Ram: {5}GB</div>
                <div>Hãng điện thoại: {6}</div>
                <div>Camera trước: {7}</div>
                <div>Camera sau: {8}</div>
                <div>Chip: {9}</div>
                <div>Hệ điều hành: {10}</div>
                <div>Màn hình: {11}</div>
            </div>

            <div class="from {12}">{12}</div>
            </div>
        </div>
    `
    lstData.forEach(e => {
        color = e.Color ? e.Color : ""
        memory = e.Memory ? e.Memory : ""
        ram = e.Ram ? e.Ram : ""
        producer = e.Producer ? e.Producer : ""
        frontCam = e.FrontCamera ? e.FrontCamera : ""
        behindCam = e.BehindCamera ? e.BehindCamera : ""
        chip = e.Chip ? e.Chip : ""
        os = e.OperationSystem ? e.OperationSystem : ""
        screen = e.Screen ? e.Screen : ""
        price = formatMoney(e.Price)
        var content = formDiv.format(e.Image, e.PhoneName, price, color, memory, ram, producer, frontCam, behindCam, chip, os, screen, e.IdPhone)
        div += content
    })

    grid.html(div)
    bindNavigationPage(totalRecord, page + 1)
}

function bindNavigationPage(total, cur) {
    numberPage = Number.parseInt(((total / 10).toFixed()))
    divNumberPage = $(".navigations");
    divNumberPage.html(null);
    var page = ""
    page += `<div class="move first" onclick="chooseFirstPage()"></div>
            <div class="move pre" onclick="choosePrePage()"></div>`
    if (numberPage == 0) {
        page = ""
    } else if (numberPage < 6) {
        for (var i = 0; i < numberPage; i++) {
            if (i == cur - 1) {
                page += `<div class="page page-active" page="${i}" onclick="choosePage(${i})">${i+1}</div>`
            } else {
                page += `<div class="page" page="${i}" onclick="choosePage(${i})">${i+1}</div>`
            }
        }

    } else if (cur <= 3) {
        for (var i = 0; i < 5; i++) {
            if (i == cur - 1) {
                page += `<div class="page page-active" page="${i}" onclick="choosePage(${i})">${i+1}</div>`
            } else {
                page += `<div class="page" page="${i}" onclick="choosePage(${i})">${i+1}</div>`
            }
        }
    } else if (cur >= numberPage - 2) {
        for (var i = numberPage - 5; i < numberPage; i++) {
            if (i == cur - 1) {
                page += `<div class="page page-active" page="${i}" onclick="choosePage(${i})">${i+1}</div>`
            } else {
                page += `<div class="page" page="${i}" onclick="choosePage(${i})">${i+1}</div>`
            }
        }
    } else {
        for (var i = cur - 3; i < cur + 2; i++) {
            if (i == cur - 1) {
                page += `<div class="page page-active" page="${i}" onclick="choosePage(${i})">${i+1}</div>`
            } else {
                page += `<div class="page" page="${i}" onclick="choosePage(${i})">${i+1}</div>`
            }
        }
    }

    page += `<div class="move next" onclick="chooseNextPage()"></div>
                <div class="move last" onclick="chooseLastPage()"></div>`

    divNumberPage.html(page)
}

function chooseFirstPage() {
    loadData(0)
}

function chooseLastPage() {
    loadData(numberPage - 1)
}

function choosePrePage() {
    page = Number.parseInt($(".page-active").attr("page"))
    if (page > 0) {
        loadData(page - 1)
    } else {
        loadData(0)
    }
}

function chooseNextPage() {
    page = Number.parseInt($(".page-active").attr("page"))
    if (page < numberPage - 1) {
        loadData(page + 1)
    } else {
        loadData(numberPage - 1)
    }
}

function choosePage(page) {
    loadData(page)
}

/**----------------------------------------------
 * Định dạng tiền theo chuẩn 000.000.000
 * @param {*} salary 
 * @returns tiền lương được định dạng
 */
function formatMoney(salary) {
    if (salary == "") {
        return "";
    }
    salary = salary.toFixed(0).replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1.");
    return salary;
}

/**-----------------------------------------------
 * Kiểm tra biến đầu vào có dữ liệu hay không?
 * @param {*} item 
 * @returns nếu null, undefined thì trả lại rỗng, ngược lại dữ nguyên
 */
function checkInvalid(item) {
    if (!item) {
        item = "";
    }
    return item;
}


function refesh() {
    loadData(0);
}

/**
 * Bind danh sách ROM
 */
function bindingDataRom() {
    var main = document.getElementById("options-container0");

    for (var k = 0; k < listROM.length; k++) {

        var div = document.createElement("div");
        div.classList.add("option");
        div.innerHTML = `
        
          <input type="radio" class="radio" id="rom-${k + 1}"/>
          <label for="rom-${k + 1}" onclick="chooseOptionROM(${listROM[k]})">${listROM[k]}GB</label>
        
        `;
        main.appendChild(div);

    }
}

/**
 * Bind danh sách ROM
 */
function bindingDataRam() {
    var main = document.getElementById("options-container1");

    for (var k = 0; k < listRAM.length; k++) {

        var div = document.createElement("div");
        div.classList.add("option");
        div.innerHTML = `
        
          <input type="radio" class="radio" id="rom-${k + 1}"/>
          <label for="rom-${k + 1}" onclick="chooseOptionRAM(${listRAM[k]})">${listRAM[k]}GB</label>
        
        `;
        main.appendChild(div);

    }
}

function chooseOptionROM(value) {
    input = document.getElementById("content-selected0");
    input.value = value + "GB";
    document.getElementById("delete-icon0").style.visibility = "visible";
    loadData(0)
}

function chooseOptionRAM(value) {
    input = document.getElementById("content-selected1");
    input.value = value + "GB";
    document.getElementById("delete-icon1").style.visibility = "visible";
    loadData(0)
}

function deleleContentInput(i) {
    input = document.getElementById("content-selected" + i);
    input.value = ""
    document.getElementById("delete-icon" + i).style.visibility = "hidden";
    var option = document.querySelectorAll("#options-container" + i + " .option");
    option.forEach(e => {
        e.classList.remove("option-selected");
    })
    loadData(0)
}

/** ------------------------------
 * Thu nhỏ kích thước menu
 */
function resizeMenu() {
    if (document.getElementById("1").style.display == "none") {
        document.getElementById("header-top").style.borderRight = "1px solid #e5e5e5";
        document.getElementById("nav").style.width = "226px";
        document.getElementById("content").style.width = "calc(100% - 227px)";
        a = document.getElementsByClassName("nav-content-text");
        for (i = 0; i < a.length; i++) {
            a[i].style.display = "block";
        }
    } else {
        document.getElementById("header-top").style.borderRight = "none";
        document.getElementById("nav").style.width = "60px";
        document.getElementById("content").style.width = "calc(100% - 61px)";
        a = document.getElementsByClassName("nav-content-text");
        for (i = 0; i < a.length; i++) {
            a[i].style.display = "none";
        }
    }

}