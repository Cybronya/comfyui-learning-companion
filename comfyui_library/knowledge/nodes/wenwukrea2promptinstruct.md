# WenWuKrea2PromptInstruct

## 节点类型

`WenWuKrea2PromptInstruct`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `llama_model:LLAMACPPMODEL`（1 次）
- `queue_handler:*`（1 次）
- `user_prompt:STRING`（1 次）
- `style:COMBO`（1 次）
- `style_image:COMBO`（1 次）
- `max_frames:INT`（1 次）
- `max_size:INT`（1 次）
- `seed:INT`（1 次）
- `force_offload:BOOLEAN`（1 次）
- `save_states:BOOLEAN`（1 次）

## 输出

- `output:STRING`（1 次）
- `output_list:STRING`（1 次）
- `state_uid:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一个标准的中国美人，呆呆的望着前方，近景", "洗图", "pasted/82aad2a5703ce10bf0925dbb8768a64232eaf34ec7de3e55b59a7e3edcdc0901.png", 24, 768, 9`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
