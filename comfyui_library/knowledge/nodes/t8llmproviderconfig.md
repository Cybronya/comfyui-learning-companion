# T8LLMProviderConfig

## 节点类型

`T8LLMProviderConfig`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `provider:COMBO`（1 次）
- `temperature_policy:COMBO`（1 次）
- `local_model:COMBO`（1 次）
- `local_mmproj:COMBO`（1 次）
- `local_context_size:INT`（1 次）
- `local_max_tokens:INT`（1 次）
- `local_think_mode:COMBO`（1 次）
- `local_reasoning_effort:COMBO`（1 次）
- `local_video_sample_fps:FLOAT`（1 次）
- `local_unload_policy:COMBO`（1 次）

## 输出

- `provider_config:T8_LLM_PROVIDER_CONFIG`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Local Qwen", "AUTO（兼容策略）", "Huihui-Qwen3.8-27B-abliterated-Q4_K.gguf", "AUTO（自动匹配）", 32768, 4096, "关闭（推荐，速度优先）", "medi`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
