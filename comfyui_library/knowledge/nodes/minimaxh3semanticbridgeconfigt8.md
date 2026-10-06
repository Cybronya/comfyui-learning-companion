# MiniMaxH3SemanticBridgeConfigT8

## 节点类型

`MiniMaxH3SemanticBridgeConfigT8`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 13 个 workflow 中。

## 输入

- `model_name:COMBO`（13 次）
- `enabled:BOOLEAN`（13 次）
- `alpha:FLOAT`（13 次）
- `magnitude_match:COMBO`（13 次）
- `token_scope:COMBO`（13 次）
- `device:COMBO`（13 次）
- `chunk_tokens:INT`（13 次）

## 输出

- `semantic_bridge:T8_SEMANTIC_BRIDGE`（13 次）
- `report_json:STRING`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["t8_compat/MiniMaxH3_SemanticBridge_v1_T8_Compat.safetensors", true, 0.12000000000000002, "per_token", "all_tokens", "a`（7 次）
- `["t8_compat/BUNNY_H3_ActionLogic_Bridge_V1_T8_Compat.safetensors", true, 0.10000000000000002, "per_token", "all_tokens",`（4 次）
- `["t8_compat/BUNNY_H3_ActionLogic_Bridge_V1_T8_Compat.safetensors", true, 0.1, "per_token", "all_tokens", "auto", 256]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
