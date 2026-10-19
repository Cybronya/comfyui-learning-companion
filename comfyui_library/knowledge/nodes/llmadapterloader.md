# LLMAdapterLoader

## 节点类型

`LLMAdapterLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `adapter_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `force_reload:BOOLEAN`（1 次）

## 输出

- `llm_adapter:LLM_ADAPTER`（1 次）
- `info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["rw_g-1b_adapter_51k.safetensors", "gemma", "auto", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
