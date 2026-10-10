# RH_Pixverse_v5_5_Text2Video

## 节点类型

`RH_Pixverse_v5_5_Text2Video`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt:STRING`（1 次）
- `resolution:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `resolution_ratio:COMBO`（1 次）
- `thinking_type:COMBO`（1 次）
- `negative_prompt:STRING`（1 次）
- `generate_audio_switch:BOOLEAN`（1 次）
- `generate_multi_clip_switch:BOOLEAN`（1 次）

## 输出

- `video:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["【艺术风格设定】： 卡通3D 动画电影画质，角色建模圆润。极致材质：皮革靴子的细腻纹理、金属扣件的柔和反光。色调温暖丰富，充满梦幻感，电影级柔和光影，极致细节。\n（0-2s：细节起势） 镜头起始于极低的贴地视角，大特写一双精美的皮革短`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
