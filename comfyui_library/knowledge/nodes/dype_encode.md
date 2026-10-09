# DyPE_Encode

## 节点类型

`DyPE_Encode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `clip:CLIP`（5 次）
- `latent:LATENT`（5 次）
- `width:INT`（5 次）
- `height:INT`（5 次）
- `pos_text:STRING`（5 次）

## 输出

- `positive:CONDITIONING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[3840, 2160, ""]`（3 次）
- `[3840, 2160, "In the center of the screen is a pot of tiger skin orchid, which is emerald green in color and has leaves `（1 次）
- `[1536, 1536, "\nIn the bustling core of a downtown creative district as dusk fades into night, a graceful woman holding `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
