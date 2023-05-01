(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-03b63e09"], {
        "698d": function(e, n, t) {},
        "9c17": function(e, n, t) {
            "use strict";
            t("698d")
        },
        a55b: function(e, n, t) {
            "use strict";
            t.r(n);
            var r = t("7a23"),
                o = {
                    class: "login"
                },
                a = {
                    class: "login-icon"
                },
                i = Object(r["h"])("div", {
                    class: "login-header"
                }, [Object(r["h"])("h2", null, "Log in to Twitter")], -1),
                s = {
                    class: "login-form"
                },
                c = {
                    class: "login-form-item"
                },
                u = Object(r["h"])("label", {
                    for: "username"
                }, "Username", -1),
                l = {
                    class: "login-form-item"
                },
                d = Object(r["h"])("label", {
                    for: "password"
                }, "Password", -1),
                p = Object(r["h"])("div", {
                    class: "login-footer"
                }, [Object(r["h"])("p", null, [Object(r["h"])("span", null, "Forgot password?"), Object(r["h"])("span", {
                    class: "dot"
                }, "·"), Object(r["h"])("span", null, "Sign up for Twitter")])], -1);

            function h(e, n, t, h, f, b) {
                var m = Object(r["C"])("base-icon");
                return Object(r["u"])(), Object(r["g"])("div", o, [Object(r["h"])("div", a, [Object(r["k"])(m, {
                    icon: "twitter"
                })]), i, Object(r["h"])("div", s, [Object(r["h"])("div", c, [Object(r["K"])(Object(r["h"])("input", {
                    id: "username",
                    "onUpdate:modelValue": n[0] || (n[0] = function(n) {
                        return e.userInfo.username = n
                    }),
                    type: "text",
                    required: "",
                    autocomplete: "off",
                    onKeypress: n[1] || (n[1] = Object(r["L"])((function() {
                        return b.handleLogin && b.handleLogin.apply(b, arguments)
                    }), ["enter"]))
                }, null, 544), [
                    [r["H"], e.userInfo.username]
                ]), u]), Object(r["h"])("div", l, [Object(r["K"])(Object(r["h"])("input", {
                    id: "password",
                    "onUpdate:modelValue": n[2] || (n[2] = function(n) {
                        return e.userInfo.password = n
                    }),
                    type: "password",
                    required: "",
                    autocomplete: "off",
                    onKeypress: n[3] || (n[3] = Object(r["L"])((function() {
                        return b.handleLogin && b.handleLogin.apply(b, arguments)
                    }), ["enter"]))
                }, null, 544), [
                    [r["H"], e.userInfo.password]
                ]), d]), Object(r["h"])("div", {
                    class: "login-submit",
                    onClick: n[4] || (n[4] = function() {
                        return b.handleLogin && b.handleLogin.apply(b, arguments)
                    })
                }, " Log in "), p])])
            }
            var f = t("1da1"),
                b = t("5530"),
                m = (t("96cf"), t("b0c0"), t("7424")),
                g = t("8bac"),
                w = t("7f56"),
                v = t("5502"),
                j = {
                    name: "LoginView",
                    components: {
                        BaseIcon: g["a"]
                    },
                    data: function() {
                        return {
                            userInfo: {
                                username: "kaanersoy",
                                password: "password"
                            },
                            validationError: {
                                username: !1,
                                password: !1
                            }
                        }
                    },
                    computed: Object(b["a"])({}, Object(v["c"])(["currentUserApiKey"])),
                    mounted: function() {
                        this.handleLogin()
                    },
                    methods: {
                        handleLogin: function() {
                            var e = Object(f["a"])(regeneratorRuntime.mark((function e() {
                                var n, t, r, o, a, i;
                                return regeneratorRuntime.wrap((function(e) {
                                    while (1) switch (e.prev = e.next) {
                                        case 0:
                                            return e.prev = 0, e.next = 3, Object(m["i"])(this.userInfo, this.currentUserApiKey);
                                        case 3:
                                            if (r = e.sent, r.data.user) {
                                                e.next = 6;
                                                break
                                            }
                                            return e.abrupt("return");
                                        case 6:
                                            return o = r.data.user, a = new w["AvatarGenerator"], i = a.generateRandomAvatar(o.id), this.$store.dispatch("setLoginInfo", {
                                                id: o.id,
                                                username: o.name,
                                                profile: {
                                                    pic: i,
                                                    pic_full: i,
                                                    pic_cover: "https://pbs.twimg.com/profile_banners/1142171408916762624/1605471218/1500x500",
                                                    description: "😎😎",
                                                    nickname: o.name,
                                                    name: o.name,
                                                    website: "https://cooldev.com"
                                                },
                                                account: {
                                                    followingCount: null === o || void 0 === o || null === (n = o.following) || void 0 === n ? void 0 : n.length,
                                                    followerCount: null === o || void 0 === o || null === (t = o.followers) || void 0 === t ? void 0 : t.length
                                                }
                                            }), e.abrupt("return", this.$router.push("/"));
                                        case 13:
                                            e.prev = 13, e.t0 = e["catch"](0), this.$notification({
                                                type: "error",
                                                message: "Failed when authentication"
                                            });
                                        case 16:
                                        case "end":
                                            return e.stop()
                                    }
                                }), e, this, [
                                    [0, 13]
                                ])
                            })));

                            function n() {
                                return e.apply(this, arguments)
                            }
                            return n
                        }(),
                        validateForm: function() {
                            this.validationError.username = !1, this.validationError.password = !1, this.userInfo.username.length < 5 && (this.validationError.username = !0), this.userInfo.password.length < 5 && (this.validationError.password = !0)
                        }
                    }
                };
            t("9c17");
            j.render = h;
            n["default"] = j
        }
    }
]);
//# sourceMappingURL=chunk-03b63e09.9d805846.js.map