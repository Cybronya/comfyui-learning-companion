# BerniniPromptEnhancer

## 节点类型

`BerniniPromptEnhancer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 12 个 workflow 中。

## 输入

- `source_video:IMAGE`（12 次）
- `source_image:IMAGE`（12 次）
- `reference_images:IMAGE`（12 次）
- `prompt:STRING`（12 次）
- `task_type:COMBO`（12 次）
- `video_frames:INT`（12 次）

## 输出

- `system_prompt:STRING`（12 次）
- `user_prompt:STRING`（12 次）
- `llm_prompt:STRING`（12 次）
- `api_prompt:STRING`（12 次）
- `json_mode:STRING`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "t2v", 8]`（3 次）
- `["An epic cinematic fantasy scene: a young guardian in white and gold ceremonial armor stands on the edge of a high plat`（1 次）
- `["这个女人看到 F1赛车和卡车激烈的竞速后，非常的惊讶。", "i2v", 3]`（1 次）
- `["用这个图像当中的女性去替换视频当中的女性，正在跳舞。", "rv2v", 3]`（1 次）
- `["在电影级的场景当中，载着汽车飞行器逃离沙虫巨口。", "r2v", 3]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
