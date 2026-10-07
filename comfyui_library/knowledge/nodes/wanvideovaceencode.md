# WanVideoVACEEncode

## 节点类型

`WanVideoVACEEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:WANVAE`（3 次）
- `input_frames:IMAGE`（3 次）
- `ref_images:IMAGE`（3 次）
- `input_masks:MASK`（3 次）
- `prev_vace_embeds:WANVIDIMAGE_EMBEDS`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `num_frames:INT`（3 次）

## 输出

- `vace_embeds:WANVIDIMAGE_EMBEDS`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 1.0000000000000002, 0, 1, false]`（2 次）
- `[832, 480, 81, 0.20000000000000004, 0, 1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
