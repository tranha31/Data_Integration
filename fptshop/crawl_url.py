from requests import get

def get_product_list(): # dùng api của fptshop lấy danh sách toàn bộ product
    resp = get('https://fptshop.com.vn/apiFPTShop/Product/GetProductList?brandAscii=&url=https:%2F%2Ffptshop.com.vn%2Fdien-thoai%3Ftrang%3D200%26pagetype%3D1&s=a21fa1e188e7467235231b625e6ac27f68019e300cf0e9ae354a70692726e2ea').json()
    return resp['datas']['filterModel']['listDefault']['list']

from js2py.evaljs import eval_js
## hàm get_s bẻ khóa api của fptshop, tìm được trong mã nguồn của web
get_s = eval_js("""
function ke(e) {
    var t = function(e) {
        var t = {
            hash: function(e, n) {
                (n = void 0 === n || n) && (e = r.encode(e));
                for (var a = [1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298], o = [1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225], i = (e += String.fromCharCode(128)).length / 4 + 2, l = Math.ceil(i / 16), c = new Array(l), s = 0; s < l; s++) {
                    c[s] = new Array(16);
                    for (var u = 0; u < 16; u++)
                        c[s][u] = e.charCodeAt(64 * s + 4 * u) << 24 | e.charCodeAt(64 * s + 4 * u + 1) << 16 | e.charCodeAt(64 * s + 4 * u + 2) << 8 | e.charCodeAt(64 * s + 4 * u + 3)
                }
                c[l - 1][14] = 8 * (e.length - 1) / Math.pow(2, 32),
                c[l - 1][14] = Math.floor(c[l - 1][14]),
                c[l - 1][15] = 8 * (e.length - 1) & 4294967295;
                var d, m, p, f, y, v, h, g, b = new Array(64);
                for (s = 0; s < l; s++) {
                    for (var S = 0; S < 16; S++)
                        b[S] = c[s][S];
                    for (S = 16; S < 64; S++)
                        b[S] = t.sigma1(b[S - 2]) + b[S - 7] + t.sigma0(b[S - 15]) + b[S - 16] & 4294967295;
                    for (d = o[0],
                    m = o[1],
                    p = o[2],
                    f = o[3],
                    y = o[4],
                    v = o[5],
                    h = o[6],
                    g = o[7],
                    S = 0; S < 64; S++) {
                        var E = g + t.Sigma1(y) + t.Ch(y, v, h) + a[S] + b[S]
                            , A = t.Sigma0(d) + t.Maj(d, m, p);
                        g = h,
                        h = v,
                        v = y,
                        y = f + E & 4294967295,
                        f = p,
                        p = m,
                        m = d,
                        d = E + A & 4294967295
                    }
                    o[0] = o[0] + d & 4294967295,
                    o[1] = o[1] + m & 4294967295,
                    o[2] = o[2] + p & 4294967295,
                    o[3] = o[3] + f & 4294967295,
                    o[4] = o[4] + y & 4294967295,
                    o[5] = o[5] + v & 4294967295,
                    o[6] = o[6] + h & 4294967295,
                    o[7] = o[7] + g & 4294967295
                }
                return t.toHexStr(o[0]) + t.toHexStr(o[1]) + t.toHexStr(o[2]) + t.toHexStr(o[3]) + t.toHexStr(o[4]) + t.toHexStr(o[5]) + t.toHexStr(o[6]) + t.toHexStr(o[7])
            },
            ROTR: function(e, t) {
                return t >>> e | t << 32 - e
            },
            Sigma0: function(e) {
                return t.ROTR(2, e) ^ t.ROTR(13, e) ^ t.ROTR(22, e)
            },
            Sigma1: function(e) {
                return t.ROTR(6, e) ^ t.ROTR(11, e) ^ t.ROTR(25, e)
            },
            sigma0: function(e) {
                return t.ROTR(7, e) ^ t.ROTR(18, e) ^ e >>> 3
            },
            sigma1: function(e) {
                return t.ROTR(17, e) ^ t.ROTR(19, e) ^ e >>> 10
            },
            Ch: function(e, t, r) {
                return e & t ^ ~e & r
            },
            Maj: function(e, t, r) {
                return e & t ^ e & r ^ t & r
            },
            toHexStr: function(e) {
                for (var t = "", r = 7; r >= 0; r--)
                    t += (e >>> 4 * r & 15).toString(16);
                return t
            }
        }
            , r = {
            encode: function(e) {
                var t = e.replace(/[\u0080-\u07ff]/g, (function(e) {
                    var t = e.charCodeAt(0);
                    return String.fromCharCode(192 | t >> 6, 128 | 63 & t)
                }
                ));
                return t.replace(/[\u0800-\uffff]/g, (function(e) {
                    var t = e.charCodeAt(0);
                    return String.fromCharCode(224 | t >> 12, 128 | t >> 6 & 63, 128 | 63 & t)
                }
                ))
            },
            decode: function(e) {
                var t = e.replace(/[\u00e0-\u00ef][\u0080-\u00bf][\u0080-\u00bf]/g, (function(e) {
                    var t = (15 & e.charCodeAt(0)) << 12 | (63 & e.charCodeAt(1)) << 6 | 63 & e.charCodeAt(2);
                    return String.fromCharCode(t)
                }
                ));
                return t.replace(/[\u00c0-\u00df][\u0080-\u00bf]/g, (function(e) {
                    var t = (31 & e.charCodeAt(0)) << 6 | 63 & e.charCodeAt(1);
                    return String.fromCharCode(t)
                }
                ))
            }
        };
        return t.hash(e)
    }("339095508askt6b9l8" + e);
    //e = e + '&s=' + t
    return t
}""")

from urllib.parse import urlencode

def get_product_url(name): # hàm tạo url, payload của request api 
    url = 'https://fptshop.com.vn/dien-thoai/' + name
    s = get_s(f'name={name}&url={url}')
    params = {
        'name': name,
        'url': url,
        's': s # mã hash của url
    }
    return f"https://fptshop.com.vn/apiFPTShop/Product/GetProductDetail?{urlencode(params, safe=':')}"

from joblib import Parallel, delayed

def batch(iterable, n=1): # hàm chia 1 iterable object thành các batch có length = n
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

def crawl_url_slowly(product_list): # hàm crawl tuần tự
    return [get_product_url(i['nameAscii']) for i in product_list]

def crawl_url(product_list): # giảm thời gian tính bằng lập trình multiprocessing, với 4 processes xử lí từng batch_size=40
    urls = Parallel(n_jobs=4, backend='multiprocessing')(delayed(crawl_url_slowly)(lis) for lis in batch(product_list,40))
    urls = [i for sublis in urls for i in sublis]
    return urls
