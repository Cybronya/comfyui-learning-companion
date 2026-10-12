# QWEN3VL_Video

## 节点类型

`QWEN3VL_Video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video:VIDEO`（1 次）
- `video_path:STRING`（1 次）
- `model:COMBO`（1 次）
- `user_prompt:STRING`（1 次）
- `seed:INT`（1 次）
- `api_key:STRING`（1 次）

## 输出

- `text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "qwen3-vl-plus", "请详细描述视频中的人物最初的姿势（可以适当描述最初接触到的物品）、与周边物品交互的动作、行为等。其他着装、外貌、场景都不需要做任何描述", 277995088456033, "randomize`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
