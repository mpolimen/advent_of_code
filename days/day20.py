def pad(image, sym="."):
    cols = len(image[0])
    image.insert(0, sym*cols)
    image.append(sym*cols)
    for i in range(len(image)): image[i] = sym + image[i] + sym
    return image

def enhance(image, algo, oob="0"):
    def conv(b): return "0" if b == "." else "1"
    n, m, new_img = len(image), len(image[0]), []
    for r in range(n):
        new_img.append([])
        for c in range(m):
            bstr = []
            bstr.append(oob if c <= 0 or r <= 0 else conv(image[r-1][c-1]))
            bstr.append(oob if r <= 0 else conv(image[r-1][c]))
            bstr.append(oob if c >= m-1 or r <= 0 else conv(image[r-1][c+1]))
            bstr.append(oob if c <= 0 else conv(image[r][c-1]))
            bstr.append(conv(image[r][c]))
            bstr.append(oob if c >= m-1 else conv(image[r][c+1]))
            bstr.append(oob if c <= 0 or r >= n-1 else conv(image[r+1][c-1]))
            bstr.append(oob if r >= n-1 else conv(image[r+1][c]))
            bstr.append(oob if c >= m-1 or r >= n-1 else conv(image[r+1][c+1]))
            new_img[-1].append(algo[int(''.join(bstr), base=2)])
        new_img[-1] = ''.join(new_img[-1])
    return new_img

def count_pixels(image): return sum([line.count("#") for line in image])

if __name__ == "__main__":
    algo, image = input(), []
    input()
    while True:
        line = input()
        if line == '': break
        image.append(line)
    light = algo[0] != "."
    N = 50 # make N=2 for part 1
    for i in range(N):
        if light and i%2:
            image = enhance(pad(image, sym="#"), algo, oob="1")
        else: image = enhance(pad(image), algo)
    print(count_pixels(image))