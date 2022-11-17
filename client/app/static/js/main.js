let viewLoginPwd = false;
let viewLoginPwd2 = false;

function changePwdView() {
  let getPwdView = $("#password");

  if (viewLoginPwd === false) {
    getPwdView.attr("type","text");
    viewLoginPwd = true;
  }
  else if (viewLoginPwd === true) {
    getPwdView.attr("type","password");
    viewLoginPwd = false;
  }
}

function changePwdView2() {
  let getPwdView = $("#password2");

  if (viewLoginPwd2 === false) {
    getPwdView.attr("type","text");
    viewLoginPwd2 = true;
  }
  else if (viewLoginPwd2 === true) {
    getPwdView.attr("type","password");
    viewLoginPwd2 = false;
  }
}
