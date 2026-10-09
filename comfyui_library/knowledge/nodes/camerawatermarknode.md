# CameraWatermarkNode

## 节点类型

`CameraWatermarkNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `exif_data:STRING`（1 次）
- `layout:COMBO`（1 次）
- `restore_preset:BOOLEAN`（1 次）
- `randomize_style:BOOLEAN`（1 次）
- `random_style_selection:STRING`（1 次）
- `seed:INT`（1 次）
- `use_exif:BOOLEAN`（1 次）
- `block_a_text_1:STRING`（1 次）
- `block_a_text_2:STRING`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["6. 画内叠加 - 右下角", false, false, "1-10", 572983194546463, "randomize", true, "Xiaomi15 Ultra", "Main Camera", "© OTT", "L`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
