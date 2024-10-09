set(0,'defaultAxesFontName','Arial') % set default font as Arial
set(0,'defaultAxesFontSize',9) % set default font size 9
set(0,'DefaultLineLineWidth',1) % set default data-linewidth 1
set(0,'DefaultAxesLineWidth',1) % set default Axes-linewidth 1

close all; % close all the figure windows

figure; % new figure
hold on; % overlap multiple graphs
x = linspace(0,2*pi, 101); y1 = sin(x); y2 = cos(x);
plot(x, y1, Color='r', LineStyle='-') % plot sin(x)
plot(x, y2,Color='b', LineStyle='-') % plot cos(x)
legend(["sin(x)", "cos(x)"], location="southwest") % plot legend
xlim([0, 2*pi]); % set x limit values
ylim([-1,1]); % set y limit values
xticks(linspace(0,2*pi,5)) % set x tick positions
xticklabels({'0', '\pi/2', '\pi', '3\pi/2', '2\pi'}) % set x tick labels
yticks(linspace(-1,1,3)) % set y tick positions
xlabel("x", "FontSize",9) % set x axis label
ylabel("y", "FontSize",9) % set y axis label
box on; % set box
plot_size_in_cm(7.5,4) % make plot in cm size
saveas(gcf, 'example.svg', 'svg') % save as svg file

function plot_size_in_cm(x_width, y_width)
cm_to_pt = 37.8; % constant to make figure exact size in cm scale
% set figure position and size
set(gcf, 'position', [500 100 x_width*cm_to_pt y_width*cm_to_pt]);
end
