# XB_llamaInstruct

## 节点类型

`XB_llamaInstruct`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `llama_model:LLAMACPPMODEL`（2 次）
- `parameters:LLAMACPPARAMS`（2 次）
- `images:IMAGE`（2 次）
- `queue_handler:*`（2 次）
- `preset_prompt:COMBO`（2 次）
- `custom_prompt:STRING`（2 次）
- `system_prompt:STRING`（2 次）
- `inference_mode:COMBO`（2 次）
- `max_frames:INT`（2 次）
- `max_size:INT`（2 次）

## 输出

- `output:STRING`（2 次）
- `output_list:STRING`（2 次）
- `state_uid:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Prompt Style - Cinematic [EN]", "nangongwan", "您是文生图模型领域的提示词工程专家。您的任务是识别图片反推提示词或者将用户的提示词使用中文扩展为高效的图像生成提示词。\n\n在撰写答案前，请`（1 次）
- `["Prompt Style - Cinematic [EN]", "孤独，大海，老人", "", "one by one", 24, 256, 799390026640047, "randomize", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
