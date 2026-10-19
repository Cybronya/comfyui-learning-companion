# t5gemmaApplyLLMToSDXLAdapter

## 节点类型

`t5gemmaApplyLLMToSDXLAdapter`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `llm_hidden_states:LLM_HIDDEN_STATES`（2 次）
- `llm_attention_mask:LLM_ATTENTION_MASK`（2 次）
- `llm_adapter:LLM_ADAPTER`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `target_width:INT`（2 次）
- `target_height:INT`（2 次）
- `crop_w:INT`（2 次）
- `crop_h:INT`（2 次）

## 输出

- `CONDITIONING:CONDITIONING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024, 1024, 1024, 0, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
