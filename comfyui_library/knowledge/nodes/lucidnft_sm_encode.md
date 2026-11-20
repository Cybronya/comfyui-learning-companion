# LucidNFT_SM_Encode

## 节点类型

`LucidNFT_SM_Encode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP_VISION:CLIP_VISION`（1 次）
- `cond:CONDITIONING`（1 次）
- `positive:CONDITIONING`（1 次）
- `seed:INT`（1 次）
- `emb:COMBO`（1 次）
- `connector:COMBO`（1 次）
- `model_type:COMBO`（1 次）

## 输出

- `condition:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1380352230, "randomize", "prompt_embeddings.pt", "lucid_connector.pth", "bf16"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
