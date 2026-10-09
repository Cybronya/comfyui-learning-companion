# RH_RhartVideoSparkvideo20TextToVideo

## 节点类型

`RH_RhartVideoSparkvideo20TextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `resolution:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `generateAudio:BOOLEAN`（1 次）
- `ratio:COMBO`（1 次）
- `webSearch:BOOLEAN`（1 次）
- `skip_error:BOOLEAN`（1 次）
- `seed:INT`（1 次）
- `returnLastFrame:BOOLEAN`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）
- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["核心主题：「孤剑踏雪・寒梅寻踪」\n塑造孤高冷峻的江湖侠客形象，整体为武侠电影写实质感 + 东方写意美学，融合雪落寒林、梅影横斜、剑风破雪的视觉风格，从踏雪独行的孤寂到拔剑出鞘的凌厉，层层递进。以剑为诺、以梅为骨，展现侠客一诺千金的江湖`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
