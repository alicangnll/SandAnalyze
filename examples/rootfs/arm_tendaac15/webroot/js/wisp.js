var initScanObj = {},
	initObj = {};

$(function () {
	$.ajaxSetup({
		cache: false
	});
	initEvent();

	//initCustomSelect(obj);

	getValue();
	top.loginOut();

	top.$(".main-dailog").removeClass("none");
	top.$(".save-msg").addClass("none");
});

function initEvent() {
	$("#submit").on("click", preSubmit);
	$("#apSsid").on("change", changeSsid);
	$("#clientApEn").on("click", changeBridge);
	$("#scan").on("click", scanSsid);

	$(".self-select-wrapper").on("click", ".self-select-option", function() {
		changeValue($(this).find(".self-select-data").attr("data-val"));
	});

	$(document).on("click", hideOption);

	$(".self-select-wrapper").on("click", showOption);
	$("#wpapsk_type").on("change", changeWpapskType);
}

function getValue() {
	$.getJSON("goform/WifiExtraGet?" + Math.random(), initValue);
}


function scanSsid() {
	$("#apSsid").html("");
	$(".main-loadding").removeClass("none");
	$("#pwd_set").addClass("none");
	$("#apSsid2").addClass("hidden");
	$("#wifiHandset").addClass("none");
	$("#scan").off("click", scanSsid);
	getScanValue();
}

function changeBridge() {
	var className = $("#clientApEn").attr("class");

	if (typeof initObj.wl_enable == "undefined") {
		showErrMsg("msg-err", _("Requesting data...please wait..."));
		return;
	}

	if (initObj.wl_enable != "1") {
		showErrMsg("msg-err", _("WiFi is disabled. Please enable WiFi first."));
		return;
	}

	if (initObj.iptvEn == "1") {
		showErrMsg("msg-err", _("The IPTV feature is enabled. Please go to Advanced Settings to disable IPTV feature first."));
		return;
	}

	if (className == "btn-off") {
		$("#clientApEn").attr("class", "btn-on");
		$("#clientApEn").val(1);
		$("#wisp_set").removeClass("none");
		$("[name='wifiWorkMode'][value='wisp']")[0].checked = true;
		scanSsid();
	} else {
		$("#clientApEn").attr("class", "btn-off");
		$("#clientApEn").val(0);
		$("#wisp_set").addClass("none");
	}
	top.initIframeHeight();
}

function changeSsid() {
	var ssid = $("#apSsid").val(),
		security;
	if (ssid == "-2") {
		$("#pwd_set").addClass("none");
		$("#wifiHandset").addClass("none");
		return;
	}
	$("#apPassword").val("");
	if (ssid == "-1") {
		security = initObj.security;
	} else if (ssid == -3) {//手动设置
		security = $("#sec_type").val();
	} else {
		security = initScanObj[ssid].security;
	}

	if (security == "none" || security == "wep") {
		$("#pwd_set").addClass("none");
	} else {
		$("#pwd_set").removeClass("none");
	}

	//手动设置
	if (ssid == "-3") {
		$("#wifiHandset").removeClass("none");
		changeWpapskType();
	} else {
		$("#wifiHandset").addClass("none");
	}

	top.initIframeHeight();
}

function changeWpapskType() {
	if ($("#wpapsk_type").val() == "none") {
		$("#pwd_set, #wpapsk_crypto_wrap").addClass("none");
	} else {
		$("#pwd_set, #wpapsk_crypto_wrap").removeClass("none");
		var wpapsk_crypto_html = "",
			wpapsk_crypto_val = $("#wpapsk_crypto").val();
		if ($("#wpapsk_type").val() != "wpa") {
			wpapsk_crypto_html = '<option value="aes">AES</option><option value="tkip">TKIP</option><option value="tkip&aes">TKIP&AES</option>';
		} else {
			wpapsk_crypto_html = '<option value="aes">AES</option><option value="tkip">TKIP</option>';
		}
		$("#wpapsk_crypto").html(wpapsk_crypto_html);
		$("#wpapsk_crypto").val(wpapsk_crypto_val);
		if ($("#wpapsk_crypto").val() != wpapsk_crypto_val) {
			$("#wpapsk_crypto").val("aes");
		}
	}

	top.initIframeHeight();
}


function initValue(obj) {
	var apSsid = obj.ssid || "",
		apPwd = obj.wpapsk_key || "",
		str;

	if (obj.handset == "1") {//手动
		initScan([]);
		changeValue("-3");
		$(".self-select-ul").html("");
		$("#handset_ssid").val(obj.ssid);
		$("#wifi_chkHz").val(obj.wifi_chkHz);
		$("#wpapsk_type").val((obj.wpapsk_type||"none"));
		$("#wpapsk_crypto").val((obj.wpapsk_crypto||"aes"));
		changeWpapskType();
	} else {
		str = "<option value='-1'>" + apSsid + "</option>";
		$("#apSsid2 .self-select-text").html(apSsid).attr("data-val", "-1");
		$("#apSsid").html(str);
	}

	$("#apPassword").val(apPwd);

	initObj = obj;

	top.$(".main-dailog").removeClass("none");
	top.$("iframe").removeClass("none");
	top.$(".loadding-page").addClass("none");

	if (obj.security == "none") {
		$("#pwd_set").addClass("none");
	} else {
		$("#pwd_set").removeClass("none");
	}
	if (obj.wl_enable == "1") {
		if (obj.wl_mode == "ap") {
			$("#clientApEn").attr("class", "btn-off");
			$("#clientApEn").val(0);
			$("#wisp_set").addClass("none");
		} else {
			$("#clientApEn").attr("class", "btn-on");
			$("#clientApEn").val(1);
			$("#wisp_set").removeClass("none");
			//getScanValue();
			$(".main-loadding").addClass("none");
			//$("#apPassword").attr("disabled",true);
			//$("#pwd_set").addClass("hidden");
			$("#apSsid2").removeClass("hidden");

			$("[name='wifiWorkMode'][value='" + obj.wl_mode + "']")[0].checked = true;
		}
	} else {
		$("#clientApEn").attr("class", "btn-off");
		$("#clientApEn").val(0);
		$("#wisp_set").addClass("none");
	}

	top.initIframeHeight();

}

function getScanValue() {
	//var scan_str = $("#apSsid").text();
	$.getJSON("goform/WifiApScan?" + Math.random(), initScan);
}

function initScan(obj) {
	//var obj = $.parseJSON(str);
	if (obj.errCode == "999") {
		top.location.reload(true);
		return;
	} else {
		obj = reCreateObj(obj);//排序
		initScanObj = obj;

		var scan_str,
			len = obj.length,
			i = 0;
		$("#apSsid").html(""); //清空ssid
		scan_str = "<option value='-2'>--" + _("Please select") +  "--</option>";
		scan_str += "<option value='-3'>--" + _("Enter the WiFi name manually") +  "--</option>";
		for (i = 0; i < len; i++) {
			scan_str += "<option value='" + i + "'>" + obj[i].ssid + "</option>";
		}
		$("#apSsid").html(scan_str);

		//排序过后的，signal为负数，数值越大
		initCustomSelect(obj);
	}

	$(".main-loadding").addClass("none");
	$("#apSsid2").removeClass("hidden");
	$("#scan").on("click", scanSsid); //重新绑定事件
}

function initCustomSelect(obj) {
	var scan_str,
		len = obj.length,
		i = 0;
	$("#apSsid2 .self-select-ul").html(""); //清空ssid

	/*
		<li class="self-select-option">
        <span class="self-select-data" data-val="0">你好</span>
        <span style="float:right;">Singal</span>
        </li>
	*/
	$("#apSsid2 .self-select-text").html("--" + _("Please select") + "--").attr("data-val", "-2");

	scan_str = '<li class="self-select-option current"><span style="float:right;"></span>' + '<span class="self-select-data" data-val="-2">--' + _("Please select") + '--</span></li>';

	scan_str += '<li class="self-select-option current"><span style="float:right;"></span>' + '<span class="self-select-data" data-val="-3">--' + _("Enter the WiFi name manually") + '--</span></li>';
	var signal = "";

	for (i = 0; i < len; i++) {
		signal = +obj[i].signal;

		if (signal > -60) {
			signal = "signal_4";
		} else if (signal <= -60 && signal > -70) {
			signal = "signal_3";
		} else if (signal <= -70 && signal > -80) {
			signal = "signal_2"
		} else {
			signal = "signal_1"
		}
		scan_str += '<li class="self-select-option wifi-ssid-txt" title="' + $("<div/>").text(obj[i].ssid).html() + '"><span class="signal ' + signal + '">&nbsp;</span><span class="self-select-data" data-val="' + i + '">' + $("<div/>").text(obj[i].ssid).html() + '</span></li>';
	}
	$("#apSsid2 .self-select-ul").html(scan_str).find(".wifi-ssid-txt").each(function(i) {
		$(this).attr("title", obj[i].ssid);
	});
	top.initIframeHeight();
}

function preSubmit() {
	var ssid = $("#apSsid").val(),
		secType = "",
		security = "",
		wpapsk_type = "",
		wpapsk_crypto = "",
		wpapsk_key = "",
		wifi_chkHz = "",
		subObj = {},
		rel = /^[0-9a-fA-F]+$/,
		subData,
		password,
		length,
		workMode;

	if ($("#clientApEn").val() == "0") {
		workMode = "ap";
	} else {
		workMode = $("[name='wifiWorkMode']:checked").val();
	}
	if ($("#clientApEn").val() == "1") {
		if (ssid == "-2") {
			showErrMsg("msg-err", _("Please select a remote SSID."));
			return;
		}
		if (ssid == -1) {//保存上次选的ssid
			if (initScanObj.security == "wep") {
				showErrMsg("msg-err", _("WEP encryption is not safe. The router does not support WEP encryption. Please change the remote router's WiFi cipher type."));
				return;
			}
			subObj = {
				"wl_mode": workMode,
				"ssid": initObj.ssid,
				"security": initObj.security == "none" ? "none" : "wpapsk",
				"wpapsk_type": initObj.wpapsk_type,
				"wpapsk_crypto": initObj.wpapsk_crypto,
				"wpapsk_key": $("#apPassword").val(),
				"wifi_chkHz": initObj.wifi_chkHz,
				"mac": initObj.mac,
				"handset":"0"//1手动 2 非手动
			}

		} else if (ssid == -3) {//手动设置
			subObj = {
				"wl_mode": workMode,
				"ssid": $("#handset_ssid").val(),
				"security": $("#wpapsk_type").val() == "none" ? "none" : "wpapsk",
				"wpapsk_type": $("#wpapsk_type").val(),
				"wpapsk_crypto":  $("#wpapsk_type").val() == "none" ? "none" : $("#wpapsk_crypto").val(),
				"wpapsk_key": $("#apPassword").val(),
				"wifi_chkHz": $("#wifi_chkHz").val(),
				"mac": "",
				"handset":"1"//1手动 2 非手动
			}
		} else  {
			if (initScanObj[ssid].security == "wep") {
				showErrMsg("msg-err", _("WEP encryption is not safe. The router does not support WEP encryption. Please change the remote router's WiFi cipher type."));
				return;
			}
			subObj = {
				"wl_mode": workMode,
				"ssid": initScanObj[ssid].ssid, //ssid
				"security": initScanObj[ssid].security == "none" ? "none" : "wpapsk", //加密类型 none || wpapsk
				"wpapsk_type": initScanObj[ssid].security.split("/")[0] || "", //加密方式 wpa wpa2 wpa&wpa2
				"wpapsk_crypto": initScanObj[ssid].security.split("/")[1] || "", //加密规则 tkip aes tkip&aes
				"wpapsk_key": $("#apPassword").val(), //密钥
				"wifi_chkHz": initScanObj[ssid].wifi_chkHz, //2.4G 5G
				"mac": initScanObj[ssid].mac,
				"handset":"0"//1手动 2 非手动
			}
		}
		
		if (subObj.handset == "1") {//手动设置验证ssid有效性
			var hansetSsid = $("#handset_ssid").val(),
				error = $.validate.valid.ssid.all(hansetSsid);
			if (hansetSsid == "") {
				showErrMsg("msg-err", _("Please specify a WiFi Name. "));
				return;	
			}	

			if (error) {
				showErrMsg("msg-err", error);
				return;				
			}
		}

		if (subObj.security == "wpapsk") {
			password = $("#apPassword").val();
			length = password.length;
			if (password == "") {
				showErrMsg("msg-err", _("Please enter the Password of selected SSID."));
				return;
			}
			if (rel.test(password)) {
				if (length < 8) {
					showErrMsg("msg-err", _("The remote router's WiFi password must be made of 8~63ASCII, or 64 hexadecimal codes."));
					return;
				}
			} else {
				if (length < 8 || length > 63) {
					showErrMsg("msg-err", _("The remote router's WiFi password must be made of 8~63ASCII, or 64 hexadecimal codes."));
					return;
				}
			}

		}
	} else {
		subObj = {
			"wl_mode": workMode
		}
	}


	//如果开启万能桥接，将提示会关闭 wps，访客网络。add by zzc
	var conflictFuns = ["WPS", _("Guest Network"), _("WiFi Timing"), _("Smart Power-save")],
		conflict = [];
	if (subObj.wl_mode != "ap") {
		if (initObj.wpsEn == "1") {
			conflict.push(conflictFuns[0]);
		}
		if (initObj.guestEn == "1") {
			conflict.push(conflictFuns[1]);
		}
		if (initObj.wifiTimerEn == "1") {
			conflict.push(conflictFuns[2]);
		}
		if (initObj.smartSaveEn == "1") {
			conflict.push(conflictFuns[3]);
		}
		if (conflict.length !== 0) {
			if (!window.confirm(_("%s feature will be disabled if the Wireless Repeating is enabled. Are you sure to save it?", [conflict.join(_("/"))]))) {
				return false;
			}
		}
	}


	//除非两次都是ap 设置不变，其他情况重启
	var reboot = false;
	if (subObj.wl_mode != "ap" || (initObj.wl_mode != "ap")) {
		reboot = true;
	}

	if (reboot&&!confirm(_("The router will reboot automatically to activate your settings. Are you sure to reboot the router?"))) {
		return false;
	} else {
		subData = objTostring(subObj);
		$.post("goform/WifiExtraSet", subData, function(str) {
			callback(str, reboot, subObj.wl_mode);
		});
	}
}

function callback(str, reboot, wlMode) {
	if (!top.isTimeout(str)) {
		return;
	}
	var num = $.parseJSON(str).errCode;
	
	if (num == 0) {
		//getValue();
		if (reboot) {

			//window.location.href = "redirect.html?3";	
			top.$.progress.showPro((wlMode == "apclient" || wlMode == "wisp"? "apclient": "reboot"), "", (wlMode == "apclient"? "tendawifi.com": ""));
			$.get("goform/SysToolReboot?"+Math.random(), function(str) {
				//top.closeIframe(num);
				if (!top.isTimeout(str)) {
					return;
				}
			});					
		} else {
			top.showSaveMsg(num);
			top.wrlInfo.initValue();
		}
	}
}

function reCreateObj(obj) {
	var newObj = [];
	var len = obj.length || 0;
	var i = 0;
	var j = 0;
	var newArry = [];

	var arry_prop = [];
	for (; i < len; i++) {
		arry_prop[i] = obj[i]["signal"]; //将需要排序的元素放在一个数组里；
	}
	newArry = arry_prop.sort();
	for (i = 0; i < len; i++) {
		for (j = 0; j < obj.length; j++) {
			if (newArry[i] == obj[j]["signal"]) { // 排序好的元素中寻找原obj元素
				newObj.push(obj[j]); //重新排序后的obj
				obj.splice(j, 1); //去掉已经找到的；
				break;
			}
		}
	}
	return newObj;
}

function changeValue(val) {
	var value = val,
		$spanEle = $("#apSsid2 .self-select-ul").find("[data-val="+val+"]"),
		html_str = $spanEle.html(),
		parent_text = $spanEle.parents(".self-select-wrapper").find(".self-select-text");

	parent_text.html(html_str);
	$(this).parents(".self-select-wrapper").find("li").removeClass("current");
	$spanEle.addClass("current");

	$("#apSsid").val(value).trigger("change", value);
	$(this).parents(".self-select-ul").css("display", "none");

	//top.initIframeHeight();

	//event.stopPropagation();
}

function showOption(event) {
	if ($(".self-select-wrapper .self-select-ul").css("display") == "block") {
		$(".self-select-ul").css("display", "none");
	} else {
		$(".self-select-wrapper .self-select-ul").css("display", "block");
	}

	event.stopPropagation();
}

function hideOption() {
	$(".self-select-ul").css("display", "none");
}