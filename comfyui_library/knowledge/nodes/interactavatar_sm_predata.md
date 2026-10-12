# InteractAvatar_SM_Predata

## 节点类型

`InteractAvatar_SM_Predata`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（4 次）
- `vae:VAE`（4 次）
- `images:IMAGE`（4 次）
- `pose_images:IMAGE`（4 次）
- `audio:AUDIO`（4 次）
- `object_images:IMAGE`（4 次）
- `short_side:COMBO`（4 次）
- `prompt:STRING`（4 次）
- `negative_prompt:STRING`（4 次）
- `structured_prompt:STRING`（4 次）

## 输出

- `data_dict:CONDITIONING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, "Hand clenches in a fist to cheer,\nRest chin on one hand in thought.", "bright tones, overexposed, static, blurre`（1 次）
- `[512, "The woman took the coffee from the table and drank it.", "bright tones, overexposed, static, blurred details, sub`（1 次）
- `[512, "A woman with long dark hair, wearing large gold hoop earrings and a navy blue hoodie, sits holding a thin, flat, `（1 次）
- `[704, "The woman took the coffee from the table and drank it.", "bright tones, overexposed, static, blurred details, sub`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
