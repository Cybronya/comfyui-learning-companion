# GearLogC3DecodeSaveEXR

## 节点类型

`GearLogC3DecodeSaveEXR`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `filename_prefix:STRING`（1 次）
- `preview_ev:FLOAT`（1 次）
- `save_exr:BOOLEAN`（1 次）

## 输出

- `hdr_linear:IMAGE`（1 次）
- `tonemapped_preview:IMAGE`（1 次）
- `exr_paths:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["hdr/gear_hdr3", 0, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
