# Lynx_Encode

## 节点类型

`Lynx_Encode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `args:Lynx_INFO`（1 次）
- `fps:INT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `pos_text:STRING`（1 次）
- `neg_text:STRING`（1 次）

## 输出

- `conds:Lynx_COND`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[16, 832, 480, "A person wear  a red suit, carves a pumpkin on a porch in the evening. The camera captures their upper b`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
