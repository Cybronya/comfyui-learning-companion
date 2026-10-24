# LucidFlux_SM_Encode

## 节点类型

`LucidFlux_SM_Encode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `state_dict:LucidFlux_SD`（3 次）
- `CLIP_VISION:CLIP_VISION`（3 次）
- `image:IMAGE`（3 次）
- `positive:CONDITIONING`（3 次）
- `emb:COMBO`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `swinir:COMBO`（1 次）

## 输出

- `condition:CONDITIONING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["prompt_embeddings.pt", 1024, 1024]`（2 次）
- `["general_swinir_v1.ckpt", 1024, 1024, "prompt_embeddings.pt"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
