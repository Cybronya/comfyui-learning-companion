# TutengGeminiAPI

## 节点类型

`TutengGeminiAPI`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `object_image:IMAGE`（2 次）
- `subject_image:IMAGE`（2 次）
- `scene_image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `model:STRING`（2 次）
- `resolution:COMBO`（2 次）
- `num_images:INT`（2 次）
- `temperature:FLOAT`（2 次）
- `top_p:FLOAT`（2 次）
- `seed:INT`（2 次）

## 输出

- `generated_images:IMAGE`（2 次）
- `response:STRING`（2 次）
- `image_url:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["把猫改成站起来。给四张", "gemini-2.5-flash-image", "1024x1024", 1, 1, 0.95, 1131339054, "randomize", 120, "", "https://apis.kuai.`（1 次）
- `["把猫改成站起来。Redraw the content of Figure 1 onto Figure 2, add content to Figure 1 to fit the aspect ratio of Figure 2, com`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
