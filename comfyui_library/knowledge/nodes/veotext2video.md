# VeoText2Video

## 节点类型

`VeoText2Video`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `enhance_prompt:BOOLEAN`（1 次）
- `enable_upsample:BOOLEAN`（1 次）
- `api_base:STRING`（1 次）
- `api_key:STRING`（1 次）
- `timeout:INT`（1 次）

## 输出

- `任务ID:STRING`（1 次）
- `状态:STRING`（1 次）
- `状态更新时间:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["8秒紧凑直播带货视频，女士通勤/时尚包包专场，镜头切换流畅，色彩明亮高饱和，符合电商直播视觉节奏，中文字幕清晰：\n\n1. 0-2秒（开场吸睛）：近景特写主播手持米白色真皮托特包，手指轻划包身质感，背景是简约ins风直播间（白色货架+`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
