# FB_Qwen3TTSDialogueInference

## 节点类型

`FB_Qwen3TTSDialogueInference`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `role_bank:QWEN3_ROLE_BANK`（1 次）
- `script:STRING`（1 次）
- `model_choice:COMBO`（1 次）
- `device:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `language:COMBO`（1 次）
- `pause_linebreak:FLOAT`（1 次）
- `period_pause:FLOAT`（1 次）
- `comma_pause:FLOAT`（1 次）
- `question_pause:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "1.7B", "auto", "fp32", "Auto", 1, 1, 4, 0.6000000000000001, 0.30000000000000004, false, 4, 503819185113633, "rando`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
