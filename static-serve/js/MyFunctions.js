// JavaScript Document

function hide_div() { document.getElementById("alert_box").style.visibility = "hidden"; }

// for drop down menu which adds item on select

function add_button(my_name, my_value, my_input_name, my_prefix, my_target) {
    my_prefix = my_prefix || "";
    my_target = my_target || "";

    var my_div = document.createElement('div');
    my_div.id = my_prefix + '_' + my_target + '_' + my_value;
    my_div.className = 'js_item';
    my_div.innerHTML = my_name;

    var my_input = document.createElement('input');
    my_input.value = my_value;
    my_input.name = my_input_name;
    my_input.type = 'hidden';

    var my_remove_box = document.createElement('div');
    my_remove_box.className = 'remove';
    my_remove_box.title = 'Ų­Ų°Ł';
    my_remove_box.innerHTML = 'X';
    my_remove_box.onclick = function () { this.parentElement.remove(this) };

    document.getElementById('js_parent' + my_prefix + my_target).appendChild(my_div);
    my_div.appendChild(my_input);
    my_div.appendChild(my_remove_box);

    var x = my_div.clientHeight;
    my_div.className += ' fadeIn';

    document.getElementById('select_list' + my_prefix + my_target).selectedIndex = 0; // resets the select list

    return false;
}

function my_remove(my_id) {
    var x = document.getElementById(my_id);
    x.className = 'js_item';
    setTimeout(function () { x.parentNode.removeChild(x) }, 0);
};

// Make iframe height fit the content

function resizeIframe(obj) {
    obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
}

// Add hidden input fields to any form

function addHiddenInput(formName, key, value) {
    // Form reference:
    var theForm = document.forms[formName];
    // Remove the input if already exists
    var element = document.getElementById(formName);
    var child = document.getElementById(key);
    if (child) { element.removeChild(child); }
    // Create a hidden input element, and append it to the form:
    var input = document.createElement('input');
    input.value = value;
    input.name = key;
    input.id = key;
    input.type = 'hidden';
    theForm.appendChild(input);
}

// Add quote text for quick reply

function addQuoteText(sender, text) {
    xoopsGetElementById('com_text').value += '[quote][quoter]' + sender + '[/quoter]\n\n' + text + '[/quote]\n';
}

// Add quote as a table row

function addQuote2Table(tableName, rowID, position, value1, value2, class1, class2, id1, id2) {
    deleteTableRow(rowID);
    var table = document.getElementById(tableName).getElementsByTagName('tbody')[0];
    var row = table.insertRow(position);
    row.id = rowID;
    var cell1 = row.insertCell(0);
    cell1.innerHTML = value1;
    cell1.className = class1;
    cell1.id = id1;
    var cell2 = row.insertCell(1);
    cell2.innerHTML = value2;
    cell2.className = class2;
    cell2.id = id2;
}

// Delete a table row

function deleteTableRow(id) {
    var tr = document.getElementById(id);
    if (tr) {
        if (tr.nodeName == 'TR') {
            var tbl = tr; // Look up the hierarchy for TABLE
            while (tbl != document && tbl.nodeName != 'TABLE') {
                tbl = tbl.parentNode;
            }

            if (tbl && tbl.nodeName == 'TABLE') {
                while (tr.hasChildNodes()) {
                    tr.removeChild(tr.lastChild);
                }
                tr.parentNode.removeChild(tr);
            }
        } else {
            /*alert( 'Specified document element is not a TR. id=' + id );*/
        }
    } else {
        /*alert( 'Specified document element is not found. id=' + id );*/
    }
}

function write_mobile_cookie(name, value, days) {
    var date = new Date();
    date.setTime(+ date + (1000 * 60 * 60 * 24 * days)); // 60 * 60 * 1000 = 1 hour
    document.cookie = name + "=" + value + "; expires=" + date.toGMTString() + "; path=/;";
}

// News Functions

function add_height(lead_id) {
    var div = document.getElementById(lead_id);
    var height = div.scrollHeight;
    document.getElementById(lead_id).style.height = height + "px";
}

function remove_height(lead_id) {
    document.getElementById(lead_id).style.height = 0 + "px";
}