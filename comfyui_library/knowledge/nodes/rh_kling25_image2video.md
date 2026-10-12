# RH_Kling25_Image2Video

## 节点类型

`RH_Kling25_Image2Video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `duration:COMBO`（3 次）
- `guidance_scale:FLOAT`（3 次）
- `seed:INT`（3 次）

## 输出

- `video:VIDEO`（3 次）
- `video_url:STRING`（3 次）
- `response:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["镜头一（0s–2s）缓缓从果园的树梢俯拍而下，阳光穿透枝叶洒落，一名少女立于树影间，微风轻掠，她抬头望向镜头，眼底映着碎光。\n镜头二（2s–5s）运镜平滑推近，她伸手摘下一颗红苹果，阳光在果实表面闪烁，她微微一笑，神情宁静。\n镜头三`（1 次）
- `["胖虎正在骂橘猫", "10", 0.5000000000000001, 484766036, "randomize"]`（1 次）
- `["美女向着镜头走来", "10", 0.5000000000000001, 1755075858, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
