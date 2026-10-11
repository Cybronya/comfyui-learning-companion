# RH_RhartVideoSparkvideo20FastTextToVideo

## 节点类型

`RH_RhartVideoSparkvideo20FastTextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（6 次）
- `prompt:STRING`（6 次）
- `resolution:COMBO`（6 次）
- `duration:COMBO`（6 次）
- `generateAudio:BOOLEAN`（6 次）
- `ratio:COMBO`（6 次）
- `webSearch:BOOLEAN`（6 次）
- `skip_error:BOOLEAN`（6 次）
- `seed:INT`（6 次）
- `returnLastFrame:BOOLEAN`（1 次）

## 输出

- `video:VIDEO`（6 次）
- `url:STRING`（6 次）
- `response:STRING`（6 次）
- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一、总体描述\n以“声临其境·悦见真我”为核心，塑造索尼耳机“高清音质、轻盈舒适、潮流百搭”的产品形象。整体为电影级写实质感+简约高级美学，融合微距特写、中景展示、全景场景化的视觉风格，从产品细节到使用场景，层层递进，丝滑衔接。以声音为`（2 次）
- `["", "720p", "5", true, "adaptive", false, false, 736992835, "randomize", false]`（1 次）
- `["", "720p", "5", true, "adaptive", false, false, 193527534852160, "randomize"]`（1 次）
- `["一、总体描述\n以“声临其境·悦见真我”为核心，塑造索尼耳机“高清音质、轻盈舒适、潮流百搭”的产品形象。整体为电影级写实质感+简约高级美学，融合微距特写、中景展示、全景场景化的视觉风格，从产品细节到使用场景，层层递进，丝滑衔接。以声音为`（1 次）
- `["一、总体描述\n以 “禅茶一味・碧水洗心” 为核心，塑造清冷强大的茶仙形象。整体为写实电影级质感 + 东方玄幻美学，融合水墨晕染、微观特写、全景磅礴的视觉风格，从茶之雅韵到灵力战斗，层层递进，丝滑衔接。以茶为刃、以禅为心，展现碧水洗涤尘`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
