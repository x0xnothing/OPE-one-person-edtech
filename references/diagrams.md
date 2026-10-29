# Diagrams cookbook (TikZ · circuitikz · pgfplots · mhchem) + pitfalls

Principles: draw to scale (use real ratios/angles), label every quantity exactly as in the text,
`\small`/`\scriptsize` labels, line width 0.8–1.1 pt for print, keep figures ≤ column width,
centre with `\begin{center}…\end{center}`. Colours in print: black + one accent (`etblue`) + light fills (`etfill`).
TikZ libraries loaded: calc, arrows.meta, positioning, patterns, decorations.*, shapes.geometric, angles, quotes, 3d, shadows.

## Mechanics
```latex
% inclined plane with block resting ON the slope (angle = atan(h/b))
\begin{tikzpicture}[scale=0.9,font=\small]
 \fill[pattern=north east lines](0,0) rectangle (5.6,-0.18);
 \draw[thick](0,0)--(5.2,0)--(5.2,3)--cycle;                 % atan(3/5.2)=30°
 \begin{scope}[shift={(2.6,1.5)},rotate=30]                  % point on hypotenuse, rotate by slope angle
   \draw[thick,fill=black!8](-0.45,0) rectangle (0.45,0.6); \node at (0,0.3){\SI{5}{kg}};
   \draw[-{Latex[length=2.5mm]},thick](0.45,0.3)--(1.8,0.3) node[above]{$T$};
 \end{scope}
 \draw (0.9,0) arc (0:30:0.9); \node at (1.4,0.28){\SI{30}{\degree}};
\end{tikzpicture}
% projectile path
\draw[thick,domain=0:6,smooth,variable=\x] plot ({\x},{\x*tan(45)-0.5*9.8*\x*\x/(2*10^2*cos(45)^2)});
% vector parallelogram
\draw[-{Latex},thick](0,0)--(3,0) node[midway,below]{$\vec P$};
\draw[-{Latex},thick](0,0)--(1,1.7) node[midway,left]{$\vec Q$};
\draw[dashed](3,0)--(4,1.7)--(1,1.7); \draw[-{Latex},very thick,etblue](0,0)--(4,1.7) node[midway,above]{$\vec R$};
\pic[draw,angle radius=5mm,"$\theta$",angle eccentricity=1.6]{angle=A--O--B};   % needs named coordinates
```
## Gas / heat (piston, thermometer) — see `demos/04-note-qr/note-qr.tex` (`\gascyl`, `\thermo` macros).
Random molecule dots: `\pgfmathsetseed{7}` then `\node[gasdot] at ({0.1+1.5*rnd},{0.1+1.2*rnd}){};` (braces!).

## Circuits (circuitikz, labels kept horizontal by edtech.sty)
```latex
\begin{circuitikz}[scale=0.8,font=\small]
 \draw (0,0) to[battery1,l={\SI{12}{V}, $r=\SI{1}{\ohm}$}] (0,2.4) to[R,l=\SI{4}{\ohm}] (2.6,2.4) -- (3.2,2.4);
 \draw (3.2,2.4) to[R,l_=\SI{3}{\ohm},*-*] (3.2,0);  \draw (3.2,2.4)--(4.6,2.4) to[R,l=\SI{6}{\ohm}] (4.6,0)--(0,0);
\end{circuitikz}
% Wheatstone bridge
\draw (0,0) to[R,l=$P$] (1.8,1.8) to[R,l=$Q$] (3.6,0) (0,0) to[R,l_=$R$] (1.8,-1.8) to[R,l_=$S$] (3.6,0);
\draw (1.8,1.8) to[rmeter,t=G] (1.8,-1.8);
```
Other bipoles: `C` capacitor, `L` inductor, `ammeter`, `voltmeter`, `lamp`, `switch`, `D` diode, `cV`/`vsource`, `isource`.

## Graphs (pgfplots)
```latex
\begin{tikzpicture}\begin{axis}[width=6cm,height=4.5cm,axis lines=left,xlabel={$t$ (s)},ylabel={$v$ (m s$^{-1}$)},
   xmin=0,xmax=6,ymin=0,ymax=14,xtick={0,2,4,6},ytick={0,6,12},grid=major,grid style={black!15}]
  \addplot[thick,domain=0:4]{3*x};
\end{axis}\end{tikzpicture}
```
## Chemistry
`\ce{2H2 + O2 -> 2H2O}`, `\ce{N2 + 3H2 <=> 2NH3}`, `\ce{Cu^2+}`, `\ce{CH3COOH}`; beakers/containers: the
`\beaker` macro in `demos/10-photo-to-print/photo-to-print.tex`; energy levels: horizontal lines + arrows
(model test demo). Structural formulas: `\usepackage{chemfig}` → `\chemfig{H-C(-[2]H)(-[6]H)-H}` (add when needed).

## Geometry / coordinate plots
Circle + tangents: see `demos/07-buet-written` (plot lines with `domain`, centre dot, dashed radius).
Use `\usetikzlibrary{intersections}` for intersection points; angles with `pic{angle=…}`.

## Known pitfalls (all hit during development — avoid them)
1. `\\` inside a `p{}` table cell ends the row → use `>{\raggedright}p{..}` and `\tabularnewline`.
2. `\multirow` + `\rowcolor`: put the multirow in the LAST row of the group with a negative count (`\multirow{-2}{*}{…}`).
3. Computed TikZ coordinates containing `(`…`)` must be braced: `({…},{…})`.
4. Do not nest a tikzpicture inside a TikZ node (options leak: anchors, text width). Pre-build in a `\savebox`.
5. `\href{url}{\qrcode{…}}` is not clickable in XeLaTeX → use `\ytqr`/`\urlqr`/`\linkbox`.
6. Units: always `\SI{value}{unit}` (never type "m/s" by hand); math in Latin digits.
7. A big unbreakable block (tabularx, minipage, tikz) that does not fit jumps to the next page and leaves a hole → make it breakable (xltabular / breakable tcolorbox) or shrink/move it; `check_fill.py` reports it.
8. Labels overlapping lines: move label with `above/below/left/right`, `pos=`, or `xshift/yshift`; verify in the PNG preview.
