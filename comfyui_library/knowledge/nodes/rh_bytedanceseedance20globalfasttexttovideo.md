# RH_BytedanceSeedance20GlobalFastTextToVideo

## 节点类型

`RH_BytedanceSeedance20GlobalFastTextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（3 次）
- `prompt:STRING`（3 次）
- `resolution:COMBO`（3 次）
- `duration:COMBO`（3 次）
- `generateAudio:BOOLEAN`（3 次）
- `ratio:COMBO`（3 次）
- `skip_error:BOOLEAN`（3 次）
- `seed:INT`（3 次）
- `returnLastFrame:BOOLEAN`（3 次）

## 输出

- `video:VIDEO`（3 次）
- `url:STRING`（3 次）
- `response:STRING`（3 次）
- `image:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["武侠风格视听大片，竹林里白衣剑客与蓑衣刀客对峙。镜头在两人之间缓慢推移，焦点在雨滴和剑柄之间切换，气氛压抑到极点，只能听见雨声。突然一道惊雷闪过，两人同时冲锋，侧拍镜头极速平移，捕捉泥浆飞溅的脚步。双兵相接瞬间画面切换为极慢动作，清晰展`（1 次）
- `["武侠风格视听大片，竹林里白衣剑客与蓑衣刀客对峙。镜头在两人之间缓慢推移，焦点在雨滴和剑柄之间切换，气氛压抑到极点，只能听见雨声。突然一道惊雷闪过，两人同时冲锋，侧拍镜头极速平移，捕捉泥浆飞溅的脚步。双兵相接瞬间画面切换为极慢动作，清晰展`（1 次）
- `["武侠风格视听大片，竹林里白衣剑客与蓑衣刀客对峙。镜头在两人之间缓慢推移，焦点在雨滴和剑柄之间切换，气氛压抑到极点，只能听见雨声。突然一道惊雷闪过，两人同时冲锋，侧拍镜头极速平移，捕捉泥浆飞溅的脚步。双兵相接瞬间画面切换为极慢动作，清晰展`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
