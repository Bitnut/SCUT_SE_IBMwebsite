/**
 * Created by wangboquan on 16/9/1.
 */
function btn1() {
    $('a#btn1').addClass('active');
    $('a#btn2').removeClass('active');
    $('a#btn3').removeClass('active');

    document.getElementById("content_title").innerHTML = "为什么要加入我们"
    document.getElementById("content").innerHTML =
        "初入大学, 很多同学都会经历一个困惑、迷茫的时期——对自己的专业的困惑，对自己未来方向的迷茫，大学的时间何其宝贵，我们需要做的那么多，时间又那么宝贵，我们是多么需要一个提高我们专业技能的同时还能锻炼个人通用技能的地方，可放眼我华工各种社团俱乐部，竟然真的很难找到一个这样的组织。</br>" +
        "然而今时不同往日，我们软件学院的IBM主机创新俱乐部成立了。在这里，我们有许多擅长各个IT领域的师兄和老师来指导我们的技术，也可以通过参加俱乐部组织的各种讲座、培训来提高自己的专业技术水平，更可以通过参与组织讲座、参与俱乐部日常运营管理，来锻炼自己的通用技能，所谓一举两得，不正是如此吗？</br>" +
        "除此之外，我们还会组织会员到IBM公司或其他高校、IT企业进行参观学习，提高会员对IT企业文化的认识；我们在俱乐部内部也会组织项目开发，或是承接、协助IBM主机教育中心、软件学院和学校的一些技术型项目，以及参加IBM公司组织开展的各种比赛、夏令营，让大家在校园里就能接触到企业文化和项目开发，为将来的学习和工作打下坚实基础，赢在起跑线上。</br>" +
        "如果你怀瑾握瑜，身为技术大神却苦于没有项目而无处一展长才，那就加入我们吧；如果你毛羽未丰，一心想提高自己的各方面能力却因为没有机会，那么也请加入我们吧——只需点击主页左上方的“加入我们”，就可以报名啦——软院IBM主机创新俱乐部，定不负所望！"
}

function btn2() {
    $('a#btn2').addClass('active');
    $('a#btn1').removeClass('active');
    $('a#btn3').removeClass('active');

    document.getElementById("content_title").innerHTML = "报名方式"
    document.getElementById("content").innerHTML =
        "1、 浏览网站，了解俱乐部背景和现状。</br>" +
        "2、 找到报名入口，并按照要求填写个人相关资料。</br>" +
        "3、 资料填写完并确认提交后会提示报名成功，等待面试官通知具体面试时间。</br>" +
        "4、 收到面试通知及时回复，并按要求准时到场。</br>" +
        "5、 面试结束，面试结果会由面试官尽快发出，请耐心等待</br>"
}

function btn3() {
    $('a#btn3').addClass('active');
    $('a#btn2').removeClass('active');
    $('a#btn1').removeClass('active');

    document.getElementById("content_title").innerHTML = "特别提醒"
    document.getElementById("content").innerHTML =
        "1、 俱乐部为软件学院专属组织，可享有年度综合测评德育加分。</br>" +
        "2、 不同部门职能不同，但均有机会进入实验室参与项目开发。</br>" +
        "3、 秘书部主管财务与活动申报，人力资源部主管成员事务与信息管理，组织部主管活动举办，宣传部主管活动宣传。</br>" +
        "4、 本俱乐部专注于技术学习和应用软件开发，鼓励成员学习IT技术。</br>" +
        "5、 大三会组织成员参加每年由IBM公司发起的各项比赛。</br>" +
        "6、 有开发经验的学生可以加入院长的实验室参与项目开发,与研究生交流合作。</br>" +
        "7、 报名学生需要对IT技术学习抱有热情，努力好学，欢迎零IT基础的大一新生加入。</br>"
}

$(document).ready(function() {
    $('[data-toggle="offcanvas"]').click(function () {
        $('.row-offcanvas').toggleClass('active')
    });
});