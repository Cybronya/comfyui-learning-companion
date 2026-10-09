# AILab_MiniCPM_4_V_Advanced

## 节点类型

`AILab_MiniCPM_4_V_Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `video:VIDEO`（2 次）
- `model:COMBO`（2 次）
- `preset_prompt:COMBO`（2 次）
- `custom_prompt:STRING`（2 次）
- `system_prompt:STRING`（2 次）
- `max_new_tokens:INT`（2 次）
- `temperature:FLOAT`（2 次）
- `top_p:FLOAT`（2 次）
- `top_k:INT`（2 次）

## 输出

- `PROMPT:STRING`（2 次）
- `STRING:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MiniCPM-V-4.5-int4", "Describe", "你是专业的导演，擅长剧情推演，请分析图片，给出电影级高质量视频提示词，包括整体画面、动作、运镜等，提示词结构为“主体+动作+场景+风格+相机”，自动推演拍摄角度、镜头类`（1 次）
- `["MiniCPM-V-4.5-int4", "Describe", "你是专业动画表情设计师，擅长动态表情制作，请分析图片，给出电影级高质量视频提示词，包括整体画面、动作、运镜等，提示词结构为“主体+动作+场景+风格+相机”，自动推演拍摄`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
