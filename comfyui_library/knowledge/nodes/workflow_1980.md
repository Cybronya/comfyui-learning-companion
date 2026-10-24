# workflow>加载图像+

## 节点类型

`workflow>加载图像+`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `遮罩:MASK`（3 次）

## 输出

- `遮罩:MASK`（3 次）
- `字符串:STRING`（3 次）
- `图像:IMAGE`（3 次）
- `LayerUtility: ImageScaleByAspectRatio V2 遮罩:MASK`（3 次）
- `原始大小:BOX`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["f158e7250bb3563be0c668b4304ea8b11888e520b0f85bdf7d19bd9a3183690e.png", "image", "wd-v1-4-moat-tagger-v2", 0.35, 0.85, `（1 次）
- `["311f892fb80c62b6799f20ebce10d1808ddd9605e160954c9067f511d64a0b0a.png", "image", "wd-v1-4-moat-tagger-v2", 0.35, 0.85, `（1 次）
- `["871bf6b4e281919c88e71e79f592856214b79253d476f5dffecf4109d2023e36.png", "image", "wd-v1-4-moat-tagger-v2", 0.35, 0.85, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
