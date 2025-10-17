import colorsys


def srgb(channel):
	if channel <= 0.04045:
		channel /= 12.92
	else:
		channel = ((channel + 0.055) / 1.055) ** 2.4
	return channel


def relative_luminance(r, g, b):
	return 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b)


def contrast_ratio(rgb1, rgb2):
	luminance1 = relative_luminance(*rgb1)
	luminance2 = relative_luminance(*rgb2)
	max_luminance = max(luminance1, luminance2)
	min_luminance = min(luminance1, luminance2)
	return (max_luminance + 0.05) / (min_luminance + 0.05)


min_contrast_ratio = 7.0
colors = [
	(237, 53, 36),
	(250, 157, 1),
	(46, 218, 119),
	(20, 199, 222),
	(1, 111, 255),
	(68, 79, 173),
	(140, 84, 208),
]
high_contrast_colors = []
for rgb in colors:
	r, g, b = [channel / 255.0 for channel in rgb]
	h, l, s = colorsys.rgb_to_hls(r, g, b)
	if contrast_ratio((r, g, b), (1, 1, 1)) >= min_contrast_ratio:
		high_contrast_colors.append(rgb)
		continue
	step = 0.0001
	while l >= 0:
		r, g, b = colorsys.hls_to_rgb(h, l, s)
		if contrast_ratio((r, g, b), (1, 1, 1)) >= min_contrast_ratio:
			r, g, b = [int(channel * 255.0 + 0.5) for channel in (r, g, b)]
			norm_r = r / 255.0
			norm_g = g / 255.0
			norm_b = b / 255.0
			if (
				contrast_ratio((norm_r, norm_g, norm_b), (1, 1, 1))
				>= min_contrast_ratio
			):
				high_contrast_colors.append((r, g, b))
				break
		l -= step
	else:
		high_contrast_colors.append((0, 0, 0))
print(high_contrast_colors)
