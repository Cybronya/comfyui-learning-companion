# LayerUtility: JoyCaptionBeta1

## 节点类型

`LayerUtility: JoyCaptionBeta1`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `joycaption_beta1_model:JOYCAPTIONBETA1_MODEL`（2 次）
- `extra_options:JoyCaption2ExtraOption`（2 次）
- `caption_type:COMBO`（2 次）
- `caption_length:COMBO`（2 次）
- `max_new_tokens:INT`（2 次）
- `top_p:FLOAT`（2 次）
- `top_k:INT`（2 次）
- `temperature:FLOAT`（2 次）
- `user_prompt:STRING`（2 次）

## 输出

- `text:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Descriptive", "long", 512, 0.9, 0, 0.6, ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
