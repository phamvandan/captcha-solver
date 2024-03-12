DELAY = 0.1
usernames = ['123','456','789']
passwords = ['123','456','789']

# "https://supportthietbi.uneti.edu.vn:443"
login_url = "https://supportthietbi.uneti.edu.vn:443/DangNhap.aspx"
captcha_failure_text = "Mã capcha chưa đúng. Vui lòng kiểm tra lại"
user_pass_wrong_text = "Tài khoản hoặc mật khẩu chưa chính xác. Vui lòng kiểm tra lại"
captcha_img_id = "ASPxCaptcha_Login_IMG"
key_username = "txt_TaiKhoan"
key_password = "txt_MatKhau"
key_captcha = "ASPxCaptcha_Login$TB"
post_data = {"__EVENTTARGET": "btnDangNhap", "__EVENTARGUMENT": '', "__VIEWSTATE": "/wEPDwUKMTgzNzg4MzU3MWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFC2NrYlBhc3N3b3JkBRFBU1B4Q2FwdGNoYV9Mb2dpbuwjy0+R8H9U3+Vwu882DwCzYQItcfITLMIKvw5zi5an", "__VIEWSTATEGENERATOR": "02DB6A77", "__EVENTVALIDATION": "/wEdAAZlHCvYdQKeQsAV8t5xccxJM68v12REWTZGEpPbPES30YZv4StDkPFX7JPVIKIlgdrC08Cep51QGTde/IoECTiiuHcma49BWMSe6vXMyYabTFjjLXCu2UEjaIRwWjA74JM5PlMdUsoYnX2bHcO4IcdiITqX85dVux95tFja/GrUTQ==", "txt_TaiKhoan": "123", "txt_MatKhau": "456", "ASPxCaptcha_Login$TB$State": "{&quot;validationState&quot;:&quot;&quot;}", "ASPxCaptcha_Login$TB": "9nzCq", "DXScript": "1_232,1_169,1_134,1_158,1_167,1_175", "DXCss": "0_1910,1_33,1_35,0_1912,1_17,1_18,1_16,../assets/images/icon/Logo_Uneti_01.ico,assets/css/bootstrap.min.css,css/all.min.css,css/grid.css,css/style.css"}


# "http://tveir.tcol.vn"
login_url = "http://tveir.tcol.vn/Login.aspx"
captcha_failure_text = "Capcha không đúng !"
user_pass_wrong_text = "Tên hoặc mật khẩu không đúng !"
captcha_img_id = "edtIMG"
key_username = "edtUSERCODE"
key_password = "edtPASSWORD"
key_captcha = "edtCaptcha"
post_data = {"__EVENTTARGET": '', "__EVENTARGUMENT": '', "__VIEWSTATE": "/wEPDwUJODYxNTg2MjQ4D2QWAgIBD2QWBgIBDw8WAh4EVGV4dAUENTQ0NGRkAgkPDxYCHghJbWFnZVVybAW+EWRhdGE6aW1hZ2UvcG5nO2Jhc2U2NCwvOWovNEFBUVNrWkpSZ0FCQVFFQVlBQmdBQUQvMndCREFBZ0dCZ2NHQlFnSEJ3Y0pDUWdLREJRTkRBc0xEQmtTRXc4VUhSb2ZIaDBhSEJ3Z0pDNG5JQ0lzSXh3Y0tEY3BMREF4TkRRMEh5YzVQVGd5UEM0ek5ETC8yd0JEQVFrSkNRd0xEQmdORFJneUlSd2hNakl5TWpJeU1qSXlNakl5TWpJeU1qSXlNakl5TWpJeU1qSXlNakl5TWpJeU1qSXlNakl5TWpJeU1qSXlNakl5TWpML3dBQVJDQUFlQUdRREFTSUFBaEVCQXhFQi84UUFId0FBQVFVQkFRRUJBUUVBQUFBQUFBQUFBQUVDQXdRRkJnY0lDUW9MLzhRQXRSQUFBZ0VEQXdJRUF3VUZCQVFBQUFGOUFRSURBQVFSQlJJaE1VRUdFMUZoQnlKeEZES0JrYUVJSTBLeHdSVlMwZkFrTTJKeWdna0tGaGNZR1JvbEppY29LU28wTlRZM09EazZRMFJGUmtkSVNVcFRWRlZXVjFoWldtTmtaV1puYUdscWMzUjFkbmQ0ZVhxRGhJV0doNGlKaXBLVGxKV1dsNWlabXFLanBLV21wNmlwcXJLenRMVzJ0N2k1dXNMRHhNWEd4OGpKeXRMVDFOWFcxOWpaMnVIaTQrVGw1dWZvNmVyeDh2UDA5ZmIzK1BuNi84UUFId0VBQXdFQkFRRUJBUUVCQVFBQUFBQUFBQUVDQXdRRkJnY0lDUW9MLzhRQXRSRUFBZ0VDQkFRREJBY0ZCQVFBQVFKM0FBRUNBeEVFQlNFeEJoSkJVUWRoY1JNaU1vRUlGRUtSb2JIQkNTTXpVdkFWWW5MUkNoWWtOT0VsOFJjWUdSb21KeWdwS2pVMk56ZzVPa05FUlVaSFNFbEtVMVJWVmxkWVdWcGpaR1ZtWjJocGFuTjBkWFozZUhsNmdvT0VoWWFIaUltS2twT1VsWmFYbUptYW9xT2twYWFucUttcXNyTzB0YmEzdUxtNndzUEV4Y2JIeU1uSzB0UFUxZGJYMk5uYTR1UGs1ZWJuNk9ucTh2UDA5ZmIzK1BuNi85b0FEQU1CQUFJUkF4RUFQd0RvYjYrdHRNc3BydTZsOG0xaEc1MzJrN1J4MEFITllFUHhEOEt6VFJ3UmFybG5ZS29GdktPZUFCOXlwUEhjTnpQNE52N2F6dDVwNUpOaWlPR01zMk42NXdCMUdNMVZmeGJmYVM4WjFqdzdjNmZwaGNScmRpZEpkblFMdlZmdWoxNU9Pbk5mSDBhTVowK2ExM2ZhNlhidW5mZm9admIrdnY4QTYvWFhyZW5BeUZCQTRIVHB3T09sVTlPMVd4MVdPWnRQdUJOSEJNWVhaRklDdU1aQTQ1SFBVY1ZqK0liMmErdVkvRGVtT1ZtdWszWE02ZjhBTHRCd0NSN3QwSDRtczc0Y3d4V09tNjFCSDhrRUdxekl1VG5DcUZBL1R2VXFndll1Y3Q5TEw5Zjh2NnVOYmVmOWZmOEExcmZYcWRUMVN5MFd5YTd2N2dXOXNqQlN4VW5uakFBQXlmdy8vVmNIVDVjaGVPZzZkT0J4MHJ5anhvWmZFV2dYMnVuZW1tV3JyRHA4ZWNDUTcxRFM0OUNNZ2ZqWG9PdDZ1TkYweFhoaU0xMUt5dzJ0dU9ESkljWVVlM2Nuc0txZUc1WVJ0ckp0cC9oL25xTnBYUy9yK3Y2MTYyVjFheE9zTnBDWEFONmtRbWFGVlB5cGtEcmpIZjF6elYzcHdNaFFRT0IwNmNEanBYbmZoelNaTkgrSlVrVnhjTlBkeTZWNTF6TDJhUnBSbkhvdkFBOWhYb25UZ1pDZ2djRHAwNEhIU3M4UlNqVGFVWGU2dURTdnAvVzM5ZjFxZE9Ca0tDQndPblRnY2RLT25BeUZCQTRIVHB3T09sSFRnWkNnZ2NEcDA0SEhTanB3TWhRUU9CMDZjRGpwV0F0LzYvcit2eE9uQXlGQkE0SFRwd09PbEhUZ1pDZ2djRHAwNEhIU2pwd01oUVFPQjA2Y0RqcFIwNEdRb0lIQTZkT0J4MG9EZit2Ni9yOFhLQU1nZEJ3QmpwOUtLRkFHUU9nNEF4MCtsRlN6R1c1a2VJRjFjYVdXME53THVLUldFYkJjU0tNWlRrWUdSMzR4Nml1WTFmVTlTOFdhVWREcy9EMnBXYlhKUVR6MzBHeUtCUVJrcWY0dWVuUTk2NzNhUndPRjl1M3RSdEk0SEMrM2IycnBwVmxDM3VwdGFwLzF1Yko5Vi9YbjYvMXIxNU9Ud0hhSFVMaTh0OVkxcTBrbjJpUVd0eUl3ZG9BVVlDOGdEMzRyRzhLK0RwSHROY2d2N3JXSVlacnFhM0VieUZSS2gyNGx3Vitaano4M1N2UmRwSEE0WDI3ZTFHMGpnY0w3ZHZhcVdNcThyamZlMzRBbnQ5LzlmMS93Zk5mRmZnZVd6OExTcHAybzYvZkdMeTBqczNuTWlFYmgwUUwwQTU0NllyZW04Q1cxd3RpWk5aMXNUV1laWXB4Y2p6QnV4a2J0dWNkdU8zRmRadEk0SEMrM2IybzJrY0RoZmJ0N1UzaktyaWxmdS92MEMreS9yK3Y2OWZPcmJ3aGNXL3hCWC9pWTY4MXJIWks0dkhtSkxNSkIrNkw3Y0ZjYzdhOUU2Y0RJVUVEZ2RPbkE0NlV1MGpnY0w3ZHZhamFSd09GOXUzdFdkYXZLcmJtNklXN3YzL3IvQUQvcmRPbkF5RkJBNEhUcHdPT2xIVGdaQ2dnY0RwMDRISFNsMmtjRGhmYnQ3VWJTT0J3dnQyOXF4RFQrdjYvcjgwNmNESVVFRGdkT25BNDZVZE9Ca0tDQndPblRnY2RLWGFSd09GOXUzdFJ0STRIQyszYjJvRFQrdjYvcjgxVUFaQTZEZ0RIVDZVVUFiUmdkT3c5S0tsbVVuZG4vMlE9PWRkAhEPFgIeB1Zpc2libGVnZGRQNMz+03IpCNp7t8rfzOlg6VQGVHGkt9o7k9WdC9w2jA==", "__VIEWSTATEGENERATOR": "C2EE9ABB", "__EVENTVALIDATION": "/wEdAAY53SaxugbSeRhOYyyxNtcLu+Pmrj2ZYHQ4gWaRNpchb0p3TjBJcdGdSiA7kumb88AUYrwcrFtyYNGLfknH+Lj0Tdq8fZR5gq0ZN+Tws6CdQJZYgDymPir0Zp4mFYzbkIgZEsphCLlj/40e4OBS4BE8ck+QHyxvSxdNaPxPbjVE7A==", "edtUSERCODE": "123", "edtPASSWORD": "345", "txtXenang": '', "edtCaptcha": "5444", "btnSave": "\xc4\x90\xc4\x83ng nh\xe1\xba\xadp"}


# "https://cps.sitv.com.vn/"
login_url = "https://cps.sitv.com.vn/Account/Login"
captcha_failure_text = "The code is incorrect!"
user_pass_wrong_text = "Tài khoản không tồn tài"
captcha_img_id = "Captcha_IMG"
key_username = "Username"
key_password = "Password"
key_captcha = "Captcha_TB_I"
post_data = {"Username": "admin", "Password": "123", "Captcha$TB$State": "{&quot;validationState&quot;:&quot;-The code is incorrect!&quot;}", "Captcha$TB": "7094", "DXScript": "1_10,1_62,1_11,1_12,1_13,1_14,1_15,1_19,1_64,1_47,1_16,1_8,17_0,17_7,1_26,1_38,1_30,17_35,1_22,1_54,17_34,1_40,1_53,1_52,17_33,1_257,1_258,1_23,1_32,1_45,1_287,1_285,1_314,1_46,1_51,17_6,1_50,17_14,1_20,1_21,1_39,1_33,1_18,1_298,1_299,1_286,1_292,1_290,1_293,1_294,1_291,1_295,1_288,1_296,1_297,1_301,1_310,1_312,1_313,1_300,1_305,1_306,1_307,1_289,1_302,1_303,1_304,1_308,1_309,1_311,17_47,17_2,1_58,1_56,17_37,1_55,17_38,1_57,17_39,17_40,1_59,17_3,1_48,17_8,17_9,1_34,17_10,1_61,17_11,1_49,1_37,17_42,1_42,17_12,17_13,1_65,1_259,1_256,17_23,1_279,17_24,1_268,17_17,1_277,17_19,1_262,1_264,1_272,1_273,1_274,1_278,1_260,1_267,17_16,17_21,1_266,17_18,1_60,1_269,1_263,17_15,1_271,1_265,17_41,1_276,1_270,17_20", "DXCss": "../Fonts/font-awesome/css/font-awesome.css,../Content/style_login.css,../Content/Site.css,1_72,1_66,1_67,1_68,1_71,1_284,1_281,1_283,1_280,1_327,1_326,1_118", "DXMVCEditorsValues": "{\"Captcha_TB\":\"7094\"}"}


# "https://cps.sitv.com.vn/"
login_url = "http://tcivietnam.com.vn/vn/login/"
form_class = "modal-content"
key_username = "email"
key_password = "passwordsign"
key_captcha = "ct_captcha"
captcha_img_id = "siimage"

captcha_failure_text = "Mã xác nhận không đúng"
user_pass_wrong_text = "Email hoặc mật khẩu không đúng!"

post_data = {"email": "admin", "passwordsign": "123", "ct_captcha": "946443", "action": "doLogin"}