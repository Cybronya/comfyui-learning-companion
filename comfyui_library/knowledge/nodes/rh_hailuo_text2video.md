# RH_Hailuo_Text2Video

## 节点类型

`RH_Hailuo_Text2Video`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prompt:STRING`（2 次）
- `model:COMBO`（2 次）
- `duration:COMBO`（2 次）
- `enable_prompt_expansion:BOOLEAN`（2 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（2 次）
- `video_url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["镜头一（0s–3s）镜头从云层之间缓缓推进，整座城市被浅金与雾白的晨光笼罩。建筑的轮廓在轻雾中若隐若现，玻璃穹顶反射着柔和光线。镜头低空环绕滑行，光影如流体在表面流动，梦幻而宁静。\n镜头二（3s–7s）镜头穿过半透明穹顶，进入内部空间`（1 次）
- `["", "t2v-standard", "10", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
