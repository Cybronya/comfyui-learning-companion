# StariAI-MiniMaxH3-Skill

## 节点类型

`StariAI-MiniMaxH3-Skill`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_1:IMAGE`（1 次）
- `image_2:IMAGE`（1 次）
- `image_3:IMAGE`（1 次）
- `image_4:IMAGE`（1 次）
- `images:IMAGE`（1 次）
- `video:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `skill:COMBO`（1 次）
- `user_prompt:STRING`（1 次）
- `model:COMBO`（1 次）

## 输出

- `视觉分析:STRING`（1 次）
- `最终提示词:STRING`（1 次）
- `运行状态:STRING`（1 次）
- `模型信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["h3-prompt-writing", "根据参考素材和当前 skill 生成完整视频提示词。图一的女生，扭动着身体舞蹈，制作15秒视频", "openai/gpt-5.6-luna"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
