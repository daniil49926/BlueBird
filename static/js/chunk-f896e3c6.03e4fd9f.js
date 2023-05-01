(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-f896e3c6"], {
        "8ebc": function(e, t, r) {},
        "9ec7": function(e, t, r) {},
        af03: function(e, t, r) {
            "use strict";
            r("f557")
        },
        b633: function(e, t, r) {
            "use strict";
            r("fb73")
        },
        c428: function(e, t, r) {
            "use strict";
            r("8ebc")
        },
        c66d: function(e, t, r) {
            "use strict";
            r.r(t);
            r("b0c0");
            var n = r("7a23"),
                i = {
                    class: "profile"
                };

            function c(e, t, r, c, o, a) {
                var s = Object(n["C"])("profile-header"),
                    l = Object(n["C"])("profile-body"),
                    u = Object(n["C"])("EditProfilePopup");
                return Object(n["u"])(), Object(n["g"])("div", i, [Object(n["k"])(s, {
                    id: o.userId,
                    following: o.following,
                    followers: o.followers,
                    name: o.name
                }, null, 8, ["id", "following", "followers", "name"]), Object(n["k"])(l), e.getEditProfileStatus ? (Object(n["u"])(), Object(n["e"])(u, {
                    key: 0
                })) : Object(n["f"])("", !0)])
            }
            var o = r("1da1"),
                a = r("5530"),
                s = (r("96cf"), {
                    class: "profile-body"
                }),
                l = Object(n["i"])('<div class="sections"><div class="sections-item active"> Твиты </div><div class="sections-item"> Твиты и ответы </div><div class="sections-item"> Медиа </div><div class="sections-item"> Нравится </div></div>', 1),
                u = {
                    key: 0,
                    class: "tweets-wrapper"
                };

            function d(e, t, r, i, c, o) {
                var a = Object(n["C"])("tweet");
                return Object(n["u"])(), Object(n["g"])("div", s, [l, c.userTweets ? (Object(n["u"])(), Object(n["g"])("div", u, [(Object(n["u"])(!0), Object(n["g"])(n["a"], null, Object(n["A"])(c.userTweets, (function(e) {
                    return Object(n["u"])(), Object(n["e"])(a, {
                        key: e.id,
                        "tweet-data": e,
                        onDeleteTweet: o.getTweets,
                        onGetTweets: o.getTweets
                    }, null, 8, ["tweet-data", "onDeleteTweet", "onGetTweets"])
                })), 128))])) : Object(n["f"])("", !0)])
            }
            var f = r("7424"),
                b = r("9257"),
                p = r("5502"),
                j = {
                    name: "ProfileBody",
                    components: {
                        Tweet: b["a"]
                    },
                    data: function() {
                        return {
                            userTweets: []
                        }
                    },
                    computed: Object(a["a"])({}, Object(p["b"])(["getMyProfileId"])),
                    mounted: function() {
                        this.getTweets()
                    },
                    methods: {
                        handleTweetDelete: function() {
                            this.getTweets()
                        },
                        getTweets: function() {
                            var e = this;
                            return Object(o["a"])(regeneratorRuntime.mark((function t() {
                                var r;
                                return regeneratorRuntime.wrap((function(t) {
                                    while (1) switch (t.prev = t.next) {
                                        case 0:
                                            return t.prev = 0, t.next = 3, Object(f["g"])({
                                                id: e.getMyProfileId
                                            });
                                        case 3:
                                            r = t.sent, e.userTweets = r.data.tweets, e.$store.commit("setProfileTweetCount", r.data.tweets.length), t.next = 11;
                                            break;
                                        case 8:
                                            t.prev = 8, t.t0 = t["catch"](0), e.$notification({
                                                type: "error",
                                                message: "Error when fetching tweets"
                                            });
                                        case 11:
                                        case "end":
                                            return t.stop()
                                    }
                                }), t, null, [
                                    [0, 8]
                                ])
                            })))()
                        }
                    }
                };
            r("af03");
            j.render = d;
            var O = j,
                m = (r("a4d3"), r("e01a"), {
                    key: 0
                }),
                h = {
                    class: "profile-cover-pic"
                },
                v = ["src"],
                w = {
                    class: "profile-header"
                },
                g = {
                    class: "profile-actions"
                },
                y = {
                    class: "profile-actions-image"
                },
                k = ["src"],
                P = {
                    class: "profile-actions-edit"
                },
                I = {
                    class: "profile-info"
                },
                D = {
                    class: "profile-info-name"
                },
                M = {
                    class: "profile-info-username"
                },
                T = {
                    class: "profile-description"
                },
                C = {
                    class: "profile-created-at"
                },
                R = ["href"],
                x = Object(n["j"])(" Регистрация: май 2011 г. "),
                E = {
                    class: "profile-follower-counts"
                },
                $ = Object(n["h"])("span", null, "в читаемых", -1),
                S = Object(n["h"])("span", null, "читателя", -1);

            function H(e, t, r, i, c, o) {
                var a, s, l = Object(n["C"])("base-icon");
                return e.me.id ? (Object(n["u"])(), Object(n["g"])("header", m, [Object(n["h"])("div", h, [Object(n["h"])("img", {
                    src: e.me.profile.pic_cover
                }, null, 8, v)]), Object(n["h"])("div", w, [Object(n["h"])("div", g, [Object(n["h"])("div", y, [Object(n["h"])("img", {
                    src: o.avatar
                }, null, 8, k)]), Object(n["h"])("div", P, [Object(n["h"])("div", {
                    class: "edit-button",
                    onClick: t[0] || (t[0] = function(t) {
                        return e.$store.commit("setEditProfileStatus", !0)
                    })
                }, " Редактировать ")])]), Object(n["h"])("div", I, [Object(n["h"])("p", D, Object(n["F"])(r.name), 1), Object(n["h"])("span", M, Object(n["F"])(r.name), 1)]), Object(n["h"])("div", T, Object(n["F"])(e.me.profile.description), 1), Object(n["h"])("div", C, [Object(n["h"])("span", null, [Object(n["k"])(l, {
                    icon: "link"
                }), Object(n["h"])("a", {
                    href: o.profileWebsite.full_website
                }, Object(n["F"])(o.profileWebsite.website), 9, R)]), Object(n["h"])("span", null, [Object(n["k"])(l, {
                    icon: "calendar"
                }), x])]), Object(n["h"])("div", E, [Object(n["h"])("p", null, [Object(n["j"])(Object(n["F"])(null === (a = r.following) || void 0 === a ? void 0 : a.length) + " ", 1), $]), Object(n["h"])("p", null, [Object(n["j"])(Object(n["F"])(null === (s = r.followers) || void 0 === s ? void 0 : s.length) + " ", 1), S])])])])) : Object(n["f"])("", !0)
            }
            r("a9e3"), r("d3b7"), r("3ca3"), r("ddb0"), r("2b3d");
            var U = r("c1df"),
                V = r.n(U),
                A = r("8bac"),
                F = r("7f56"),
                L = new F["AvatarGenerator"],
                B = {
                    name: "ProfileHeader",
                    components: {
                        BaseIcon: A["a"]
                    },
                    props: {
                        id: Number,
                        following: Array,
                        followers: Array,
                        name: String
                    },
                    computed: Object(a["a"])(Object(a["a"])({}, Object(p["b"])({
                        getMyProfileId: "getMyProfileId",
                        me: "getMe"
                    })), {}, {
                        avatar: function() {
                            return L.generateRandomAvatar(Number(this.id))
                        },
                        profileWebsite: function() {
                            return {
                                website: new URL(new URL(this.me.profile.website)).host,
                                full_website: this.me.profile.website
                            }
                        },
                        joinedAtDate: function() {
                            return "".concat(V()(this.me.createdAt).format("MMM YYYY"))
                        }
                    }),
                    mounted: function() {
                        var e = this;
                        return Object(o["a"])(regeneratorRuntime.mark((function t() {
                            var r;
                            return regeneratorRuntime.wrap((function(t) {
                                while (1) switch (t.prev = t.next) {
                                    case 0:
                                        return t.prev = 0, t.next = 3, Object(f["c"])({
                                            id: e.getMyProfileId
                                        });
                                    case 3:
                                        return r = t.sent, e.$store.commit("setMe", r.data), t.abrupt("return");
                                    case 8:
                                        t.prev = 8, t.t0 = t["catch"](0), e.$notification({
                                            type: "error",
                                            message: "Error when fetching user data"
                                        });
                                    case 11:
                                    case "end":
                                        return t.stop()
                                }
                            }), t, null, [
                                [0, 8]
                            ])
                        })))()
                    },
                    methods: {
                        moment: V.a
                    }
                };
            r("c428");
            B.render = H;
            var W = B,
                _ = function(e) {
                    return Object(n["x"])("data-v-52dcc2ce"), e = e(), Object(n["v"])(), e
                },
                K = {
                    class: "edit-profile-wrapper"
                },
                Y = {
                    class: "edit-profile-popup-header"
                },
                q = _((function() {
                    return Object(n["h"])("div", {
                        class: "heading"
                    }, [Object(n["h"])("h3", null, "Изменить профиль")], -1)
                })),
                G = {
                    class: "submit-button"
                },
                J = ["disabled"],
                N = {
                    class: "edit-form"
                },
                z = {
                    class: "edit-form-item"
                },
                Q = _((function() {
                    return Object(n["h"])("label", {
                        for: "name"
                    }, "Имя", -1)
                })),
                X = {
                    class: "edit-form-item"
                },
                Z = _((function() {
                    return Object(n["h"])("label", {
                        for: "description"
                    }, "Описание", -1)
                })),
                ee = {
                    class: "edit-form-item"
                },
                te = _((function() {
                    return Object(n["h"])("label", {
                        for: "website"
                    }, "Сайт", -1)
                }));

            function re(e, t, r, i, c, o) {
                var a = Object(n["C"])("BaseIcon");
                return Object(n["u"])(), Object(n["g"])("div", {
                    ref: "popupWrapper",
                    class: "edit-profile-popup",
                    onClick: t[5] || (t[5] = function() {
                        return o.handleClickOutside && o.handleClickOutside.apply(o, arguments)
                    }),
                    onKeydown: t[6] || (t[6] = Object(n["L"])((function(t) {
                        return e.$store.commit("setEditProfileStatus", !1)
                    }), ["esc"]))
                }, [Object(n["h"])("div", K, [Object(n["h"])("div", Y, [Object(n["h"])("div", {
                    class: "close-button",
                    onClick: t[0] || (t[0] = function(t) {
                        return e.$store.commit("setEditProfileStatus", !1)
                    })
                }, [Object(n["k"])(a, {
                    icon: "close"
                })]), q, Object(n["h"])("div", G, [Object(n["h"])("button", {
                    disabled: !o.IsStringsValid || !o.IsURLValid,
                    onClick: t[1] || (t[1] = function() {
                        return o.submitHandler && o.submitHandler.apply(o, arguments)
                    })
                }, " Сохранить ", 8, J)])]), Object(n["h"])("div", N, [Object(n["h"])("div", z, [Q, Object(n["K"])(Object(n["h"])("input", {
                    id: "name",
                    "onUpdate:modelValue": t[2] || (t[2] = function(e) {
                        return c.userData.name = e
                    }),
                    type: "text",
                    required: ""
                }, null, 512), [
                    [n["H"], c.userData.name]
                ])]), Object(n["h"])("div", X, [Z, Object(n["K"])(Object(n["h"])("input", {
                    id: "description",
                    "onUpdate:modelValue": t[3] || (t[3] = function(e) {
                        return c.userData.description = e
                    }),
                    type: "text",
                    required: ""
                }, null, 512), [
                    [n["H"], c.userData.description]
                ])]), Object(n["h"])("div", ee, [te, Object(n["K"])(Object(n["h"])("input", {
                    id: "website",
                    "onUpdate:modelValue": t[4] || (t[4] = function(e) {
                        return c.userData.website = e
                    }),
                    type: "url",
                    required: ""
                }, null, 512), [
                    [n["H"], c.userData.website]
                ])])])])], 544)
            }
            var ne = {
                name: "EditProfilePopup",
                components: {
                    BaseIcon: A["a"]
                },
                data: function() {
                    return {
                        userData: {
                            name: "",
                            description: "",
                            website: ""
                        }
                    }
                },
                computed: Object(a["a"])(Object(a["a"])({}, Object(p["b"])(["getMe"])), {}, {
                    IsStringsValid: function() {
                        return this.userData.name.length > 1 && this.userData.description.length > 2
                    },
                    IsURLValid: function() {
                        try {
                            return new URL(this.userData.website), !0
                        } catch (e) {
                            return !1
                        }
                    }
                }),
                created: function() {
                    this.userData = {
                        name: this.getMe.profile.name,
                        description: this.getMe.profile.description,
                        website: this.getMe.profile.website
                    }
                },
                methods: {
                    submitHandler: function() {
                        var e = this;
                        return Object(o["a"])(regeneratorRuntime.mark((function t() {
                            return regeneratorRuntime.wrap((function(t) {
                                while (1) switch (t.prev = t.next) {
                                    case 0:
                                        return t.prev = 0, t.next = 3, e.$store.dispatch("setMyInfo", Object(a["a"])({}, e.userData));
                                    case 3:
                                        t.next = 8;
                                        break;
                                    case 5:
                                        t.prev = 5, t.t0 = t["catch"](0), e.$notification({
                                            type: "error",
                                            message: "Error when editing profile"
                                        });
                                    case 8:
                                    case "end":
                                        return t.stop()
                                }
                            }), t, null, [
                                [0, 5]
                            ])
                        })))()
                    },
                    handleClickOutside: function(e) {
                        var t = {
                            target: e.target,
                            ref: this.$refs.popupWrapper
                        };
                        t.target === t.ref && this.$store.commit("setEditProfileStatus", !1)
                    }
                }
            };
            r("b633");
            ne.render = re, ne.__scopeId = "data-v-52dcc2ce";
            var ie = ne,
                ce = {
                    name: "ProfileView",
                    components: {
                        ProfileBody: O,
                        ProfileHeader: W,
                        EditProfilePopup: ie
                    },
                    data: function() {
                        return {
                            userId: null,
                            following: 0,
                            followers: 0,
                            name: ""
                        }
                    },
                    computed: Object(a["a"])({}, Object(p["b"])(["getMyProfileId", "getEditProfileStatus"])),
                    mounted: function() {
                        var e = this;
                        return Object(o["a"])(regeneratorRuntime.mark((function t() {
                            var r, n, i, c, o;
                            return regeneratorRuntime.wrap((function(t) {
                                while (1) switch (t.prev = t.next) {
                                    case 0:
                                        return n = null === (r = e.$route) || void 0 === r ? void 0 : r.params, i = n.profileId, t.next = 3, Object(f["f"])(i);
                                    case 3:
                                        c = t.sent, o = c.data, e.userId = null === o || void 0 === o ? void 0 : o.user.id, e.following = null === o || void 0 === o ? void 0 : o.user.following, e.followers = null === o || void 0 === o ? void 0 : o.user.followers, e.name = null === o || void 0 === o ? void 0 : o.user.name;
                                    case 9:
                                    case "end":
                                        return t.stop()
                                }
                            }), t)
                        })))()
                    }
                };
            r("fc23");
            ce.render = c;
            t["default"] = ce
        },
        f557: function(e, t, r) {},
        fb73: function(e, t, r) {},
        fc23: function(e, t, r) {
            "use strict";
            r("9ec7")
        }
    }
]);
//# sourceMappingURL=chunk-f896e3c6.03e4fd9f.js.map