# SenseNova_SM_Sampler

## 节点类型

`SenseNova_SM_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `model:MODEL`（11 次）
- `image:IMAGE`（11 次）
- `img_mode:COMBO`（11 次）
- `prompt:STRING`（11 次）
- `seed:INT`（11 次）
- `steps:INT`（11 次）
- `target_pixels:COMBO`（11 次）
- `cfg:FLOAT`（11 次）
- `img_cfg:FLOAT`（11 次）
- `timestep_shift:FLOAT`（11 次）

## 输出

- `image:IMAGE`（11 次）
- `text:STRING`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["edit", "a photo of a cat", 809608695, "randomize", 8, "9:16", 1, 1, 3, 1, 0, 1, "none", false, false, true, 1024, 0.7,`（1 次）
- `["edit", "a photo of a cat", 2136157389, "randomize", 8, "9:16", 1, 1, 3, 1, 0, 1, "none", false, false, true, 1024, 0.7`（1 次）
- `["vqa", "画面中的内容和元素、排版和布局是什么？", 888, "fixed", 8, "9:16", 1, 1, 3, 1, 1, 1, "none", false, true, 1024, 256, 0.9, 0, 0, 0]`（1 次）
- `["edit", "把图片变成2D动漫风格", 888, "fixed", 8, "9:16", 1, 1, 3, 1, 1, 1, "none", false, true, 1024, 256, 0.9, 0, 0, 0]`（1 次）
- `["interleave", "该信息图以手绘卡通风格呈现，主题为“【关于公共交通的新闻报道与信息更新】”，整体布局呈螺旋式或S形路径，从顶部开始，依次向下延伸至底部，象征着信息流动和城市发展进程。背景为浅米色，边框带有虚线和星星、云朵等装`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
