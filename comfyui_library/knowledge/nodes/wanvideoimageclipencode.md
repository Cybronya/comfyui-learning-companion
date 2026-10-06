# WanVideoImageClipEncode

## 节点类型

`WanVideoImageClipEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:WANCLIP`（2 次）
- `image:IMAGE`（2 次）
- `vae:WANVAE`（2 次）
- `generation_width:INT`（1 次）
- `generation_height:INT`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, 81, true, 0, 1, 1, true]`（1 次）
- `[512, 768, 53, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
