# RH_Vidu_Text2Video

## 节点类型

`RH_Vidu_Text2Video`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `style:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `resolution:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `movement_amplitude:COMBO`（1 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `video_url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["镜头1（0-2秒）：紫色的夜空下，朦胧的月光洒在一片魔法森林中。森林中堆满了巨大的橙色南瓜，微弱的紫色光点在空气中漂浮，像萤火虫般闪烁。镜头从地面慢慢升起，穿过藤蔓缠绕的树木，映射出梦幻般的紫色背景。\n镜头2（2-4秒）：镜头转向一只`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
