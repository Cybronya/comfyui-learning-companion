# RHMiniMaxH3Ref2VAModelLoader

## 节点类型

`RHMiniMaxH3Ref2VAModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 11 个 workflow 中。

## 输入

- `model_root:COMBO`（11 次）
- `dtype:COMBO`（11 次）
- `transformer_path:COMBO`（11 次）
- `attention_backend:COMBO`（9 次）

## 输出

- `h3_model:MINIMAX_H3_DIRECT_MODEL`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MiniMax-H3", "auto", "MiniMax-H3-Ref2VA-int8_convrot.safetensors", "auto"]`（9 次）
- `["MiniMax-H3", "auto", "MiniMax-H3-Ref2VA-int8_convrot.safetensors"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
