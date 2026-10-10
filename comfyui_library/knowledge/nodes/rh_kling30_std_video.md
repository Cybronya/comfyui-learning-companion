# RH_Kling30_Std_Video

## 节点类型

`RH_Kling30_Std_Video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `end_image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `duration:COMBO`（1 次）
- `cfg_scale:FLOAT`（1 次）
- `sound:BOOLEAN`（1 次）
- `seed:INT`（1 次）
- `negative_prompt:STRING`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `video_url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["手持摄像机拍摄，呼吸感运镜，近景特写。 在漆黑的废土工厂遗迹中，一台巨大的生锈动力装甲正在被维修。维修工手中的焊枪喷射出耀眼的蓝色火花，火花在镜头前飞溅，产生真实的镜头光晕效果。镜头随呼吸轻微晃动，焦距在装甲的金属质感和飞溅的火花之间快`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
