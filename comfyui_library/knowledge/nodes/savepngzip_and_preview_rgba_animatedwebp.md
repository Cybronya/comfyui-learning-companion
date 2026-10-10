# SavePNGZIP_and_Preview_RGBA_AnimatedWEBP

## 节点类型

`SavePNGZIP_and_Preview_RGBA_AnimatedWEBP`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images_rgb:IMAGE`（1 次）
- `images_alpha:IMAGE`（1 次）
- `filename_prefix:STRING`（1 次）
- `fps:FLOAT`（1 次）
- `lossless:BOOLEAN`（1 次）
- `quality:INT`（1 次）
- `method:COMBO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ComfyUI", 16, true, 80, "default"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
