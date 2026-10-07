# Qwen2.5VL

## 节点类型

`Qwen2.5VL`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `text:STRING`（2 次）
- `model:COMBO`（2 次）
- `quantization:COMBO`（2 次）
- `keep_model_loaded:BOOLEAN`（2 次）
- `temperature:FLOAT`（2 次）
- `max_new_tokens:INT`（2 次）
- `seed:INT`（2 次）
- `video_path:STRING`（2 次）

## 输出

- `STRING:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "Qwen2.5-VL-7B-Instruct", "none", false, 0.7, 512, 989, "randomize", ""]`（1 次）
- `["图片描述内容要求：\n请简单描述一下画面主题内容。\n\n然后并补充更详细相关内容：\n主体相关：人物性别、姿势动作、形态（肤色，发型，身材）、人物朝向、视角、表情、互动内容、服装和配饰，等等不限于；\n所在场景：场景中的其他物体元素和`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
