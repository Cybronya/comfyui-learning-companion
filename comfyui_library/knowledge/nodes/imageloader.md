# ImageLoader

## 节点类型

`ImageLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image:COMBO`（5 次）
- `upload:IMAGEUPLOAD`（5 次）

## 输出

- `IMAGE:IMAGE`（5 次）
- `MASK:MASK`（5 次）
- `PATH:PATH`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["c1508624b2f991975e2134c9f40057aaed64a0f9dc27820ff192a77c9471ca3b.jpg", "image"]`（1 次）
- `["4921d9fdeae1a191cf81e8346a65a25f99ccb3d4baa37c2ac7bfb860a907c718.png", "image"]`（1 次）
- `["484071e757f2fe6271df62a276d9f4c254514515f5e20f977c5bd6faf12b1859.png", "image"]`（1 次）
- `["0238b8af2502a1a274cac44a7cacae52f8607d6b1d383ff5ae8215b2e72e1c2d.webp", "image"]`（1 次）
- `["886660c7cef512345ecfddbab07f7cfbac69dc8a2e64f76bf12e5e33086b30a8.png", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
