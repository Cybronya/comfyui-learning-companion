# LTXVHDRDecodePostprocess

## 节点类型

`LTXVHDRDecodePostprocess`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `exposure:FLOAT`（1 次）
- `save_exr:BOOLEAN`（1 次）
- `output_dir:STRING`（1 次）
- `filename_prefix:STRING`（1 次）
- `half_precision:BOOLEAN`（1 次）

## 输出

- `tonemapped:IMAGE`（1 次）
- `hdr_linear:IMAGE`（1 次）
- `exr_files:*`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[7.1, false, "output/hdr_exr3", "frame", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
