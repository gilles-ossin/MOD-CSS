def cd0():
    return """
    // standard name 
    &lt;p :box="co[blue]"&gt;lorem ipsum dolor ...&lt;/p&gt;
    
    // Hex Value 
    &lt;p :box="co[#0d6efd]"&gt;lorem ipsum dolor ...&lt;/p&gt;
    
    // RGB or RGBA Value
    &lt;p :box="co[rgb(13, 110, 253)]"&gt;lorem ipsum dolor ...&lt;/p&gt;
    
    // variable
    &lt;p :box="co[var(--txt-title)]"&gt;lorem ipsum dolor ...&lt;/p&gt;
    
    // hsl and any others unit(s) supported by CSS
    &lt;p :box="co[hsl(216, 98%, 52%)]"&gt;lorem ipsum dolor ...&lt;/p&gt;"""

def cd1():
     return """
     // Font-size 
    &lt;p :box="fo.sz[12px]"&gt;lorem ipsum dolor ...&lt;/p&gt;
    
    // Font-style
    &lt;p :box="fo.sy[italic]"&gt;lorem ipsum dolor ...&lt;/p&gt;
    
    // Font-family, Font-weight 
    // Rem, em % or any others unit(s) supported by CSS 
    &lt;p :box="fo.fa[monospace] fo.wg[500] fo.sz[1.2rem]"&gt;lorem ipsum dolor ...&lt;/p&gt;"""

def cd2():
    return """
     // Background 
    &lt;p :box="bg[lightgray]"&gt;lorem ipsum dolor ...&lt;/p&gt;
    
    // Background-color with any others unit(s) supported by CSS 
    &lt;p :box="bg.co[hsla(175, 86%, 53%, 0.3)]"&gt;lorem ipsum dolor ...&lt;/p&gt;"""   

def cd3():
    return """
     // 1st Example
    &lt;p :box="bd[1px solid gray]"&gt;lorem ipsum dolor ...&lt;/p&gt;
    // or detailed
    &lt;p :box="bd.wd[1px] bd.sy[solid] bd.co[gray]"&gt;lorem ipsum dolor ...&lt;/p&gt;

    // 2nd example 
    &lt;p :box="bd[.1em dashed #808080]"&gt;lorem ipsum dolor ...&lt;/p&gt;"""

def cd4():
    return """
     // First
    &lt;p :box="br[8px]"&gt;lorem ipsum dolor ...&lt;/p&gt;
                
    // 2nd
    &lt;p :box="br[0 1rem]"&gt;lorem ipsum dolor ...&lt;/p&gt;"""
    
def cd5():
    return """
     // Margin-left
    &lt;p :box="m.lf[30px]"&gt;lorem ipsum dolor ...&lt;/p&gt;                
    
    // Margin-right
    &lt;p :box="m.rg[30px]"&gt;lorem ipsum dolor ...&lt;/p&gt;
    
    // Margin X & Y
    &lt;p :box="m[30px 15px]"&gt;lorem ipsum dolor ...&lt;/p&gt;"""

def cd6():
    return """
     // Padding-top
    &lt;p  :box="p.tp[10px]"&gt;lorem ipsum dolor ...&lt;/p&gt;
                
     // Padding-right
    &lt;p :box="p.rg[20px]"&gt;lorem ipsum dolor ...&lt;/p&gt;
    
    // Padding
    &lt;p :box="p[10px]"&gt;lorem ipsum dolor ...&lt;/p&gt;"""

def cd7():
    return """
     // height 30px, width 90%
    &lt;p :box="h[30px] w[90%]"&gt;lorem ipsum dolor ...&lt;/p&gt;
                
     // height auto, width 400px
    &lt;p :box="h[auto] w[400px]"&gt;lorem ipsum dolor ...&lt;/p&gt;  
     
     // set height & width in once
    &lt;p :box="h*w[40px]"&gt;lorem&lt;/p&gt;"""

# FLEXGRID    
def flx0():
    return """
    &lt;div :mod="row[100%]"&gt;
        &lt;div :mod="col[5.4rem]"&gt;5.4rem&lt;/div&gt;
        &lt;div :mod="col[100px]"&gt;100px&lt;/div&gt;
        &lt;div :mod="col[25%]"&gt;25%&lt;/div&gt;
        &lt;div :mod="col[auto]"&gt;auto&lt;/div&gt;
    &lt;/div&gt; """

def flx1():
    return """
    &lt;div :mod="row[fit]"&gt;
        &lt;div :mod="col[5rem]"&gt;5rem&lt;/div&gt;
        &lt;div :mod="col[25%]"&gt;25%&lt;/div&gt;
        &lt;div :mod="col[auto]"&gt;auto&lt;/div&gt;
    &lt;/div&gt;"""

def flx2():
    return """
    &lt;div :mod="row[100%]"&gt;
        &lt;div :mod="col[auto 5%]"&gt;auto offset 5%&lt;/div&gt;
        &lt;div :mod="col[fit 15%]"&gt;fit with offset 15%&lt;/div&gt;
        &lt;div :mod="col[250px]"&gt;250px&lt;/div&gt;
        &lt;div :mod="col[10vmax]"&gt;10vmax&lt;/div&gt;
    &lt;/div&gt;"""

def flx3():
    return """
    &lt;div :mod="row[auto]"&gt;
        &lt;div :mod="col[12em]"&gt;4em&lt;/div&gt;
        &lt;div :mod="col[22%]"&gt;22%&lt;/div&gt;
        &lt;div :mod="col[32vh]"&gt;32vh&lt;/div&gt;
        &lt;div :mod="col[250px]"&gt;250px&lt;/div&gt;
        &lt;div :mod="col[auto]"&gt;auto&lt;/div&gt;
    &lt;/div&gt;"""

def flx4():
    return """
    &lt;div :mod="row[100% 10px]"&gt;
        &lt;div :mod="col[auto]"&gt;auto&lt;/div&gt;
        &lt;div :mod="col[auto]"&gt;auto&lt;/div&gt;
        &lt;div :mod="col[auto]"&gt;auto&lt;/div&gt;
        &lt;div :mod="col[auto]"&gt;auto&lt;/div&gt;
    &lt;/div&gt;"""

# BREAKPOINTS    
def brk0():
    return """
    &lt;input :box="w[100%] || lg? w[55%]" type="text" placeholder="Type here"&gt;"""

def brk1():
    return """
     &lt;div :mod="row[100%]"&gt;
        &lt;div :mod="col[100%] || md? col[37.5%] || lg? col[50%]"&gt;col&lt;/div&gt;
        &lt;div :mod="col[100%] || md? col[37.5%] || lg? col[50%]"&gt;col&lt;/div&gt;
        &lt;div :mod="col[100%] || md? col[25%]" :box="lg? dsp[none]"&gt;col&lt;/div&gt;
    &lt;/div&gt;"""

# Pseudo states
def ps1():
    return """
&lt;button class="btn btn-success" :box="hover: bg[purple] co[lightblue] bd[none]"&gt;..&lt;/button&gt;"""

def ps2():
    return """
&lt;input type="checkbox" :box="w*h[32px] ... && checked: bg[#3137fd80]"&gt;"""

def ps3():
    return """
&lt;input class="input-line" :box="focus: bg[none] bd.co[blue]" type="text"  ..&gt;"""

# Selecteurs
def sel1():
    return """
1. Set selector
    &lt;div :var="li:nth-child(even) { bg[#202020] co[#f4f4f4] }"&gt;&lt;/div&gt;
    &lt;div :var="li:nth-child(odd) { bg[lightblue] co[blue] }"&gt;&lt;/div&gt;

2. Create your elements
&lt;ul :box="ls[none]"&gt;
    {% for x in '123456' %}
    &lt;li :box="p[4px 6px] m.bt[2px]"&gt;Line {{ x }}&lt;/li&gt;
    {% endfor %}
&lt;/ul&gt;"""

def sel2():
    return """
// 1st. Create new class
&lt;div :var=".input-line { w[100% !important] m.tp[6px] p[.3rem] p.lf[1rem] h[35px] co[lightgray] bg[#90909010] ot*bd[none] 
    bd.bt[1px solid gray] && focus: bg[none] bd.co[gold] }"&gt;&lt;/div&gt;

// 2nd. Set class on element
&lt;input class="input-line"  type="text" placeholder="Type here"&gt;"""

def sel3():
    return """
// Update and setting classes
&lt;button class="btn btn-primary" :var=".btn-primary:hover { bg[#0f256e] co[lightblue] bx.sh[0px 2px 3px 1px #12ace930] }"&gt; 
Primary&lt;/button&gt;"""

def sel4():
    return """
// Update and setting classes
&lt;div :var=".btn-secondary{ bg[#EC3883] bd[none] && focus*hover: bg[#EC388380] co[pink] bx.sh[0px 2px 3px 1px #ea10a580]}"&gt;&lt;/div&gt;

// or set ID or any other selector
&lt;div :var="#btn{ bg[#EC3883] bd[none] && focus*hover: bg[#EC388380] co[pink] bx.sh[0px 2px 3px 1px #ea10a580]}"&gt;&lt;/div&gt;

// HTML Element
&lt;button class="btn btn-secondary" id="btn"&gt;Secondary&lt;/button&gt;"""
