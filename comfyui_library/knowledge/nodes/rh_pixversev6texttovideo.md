# RH_PixverseV6TextToVideo

## 节点类型

`RH_PixverseV6TextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `resolution:COMBO`（2 次）
- `duration:INT`（2 次）
- `generateAudioSwitch:BOOLEAN`（2 次）
- `aspectRatio:COMBO`（2 次）
- `thinkingType:COMBO`（2 次）
- `skip_error:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["# 一、总体描述\n以“竹影惊鸿·剑定乾坤”为核心，塑造白衣剑客**身姿飘逸、剑法凌厉、侠气凛然**的人物形象。整体为电影级写实武侠质感+中式水墨意境美学，融合微距剑刃特写、中景武打对拆、全景竹林纵深的视觉风格，从兵器细节到招式对决，层`（1 次）
- `["一名孤独的男子骑乘着一条威严的巨龙,高空飞越郁郁葱葱的热带岛屿。镜头以广角无人机式跟拍展开,从大尺度航拍视角平滑环绕巨龙飞行,运动流畅、稳定,并伴随轻微景深变化。下方海浪猛烈拍击陡峭悬崖,形成强烈纵深感。巨龙振翅穿过云层,黄金时刻的温暖`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
