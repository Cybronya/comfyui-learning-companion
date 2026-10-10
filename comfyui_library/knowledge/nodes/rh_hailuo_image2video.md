# RH_Hailuo_Image2Video

## 节点类型

`RH_Hailuo_Image2Video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `seed:INT`（1 次）
- `enable_prompt_expansion:BOOLEAN`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `video_url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["镜头一（0s–3s）镜头从台阶底部缓缓推进，云雾在阶梯两侧翻涌。\n光线从厚重的云层中穿透，银白的光束洒落在庙宇与石阶上，建筑轮廓在光与影的交替中显现。\n镜头二（3s–7s）镜头向上缓缓升起，穿越浮空拱桥与塔楼之间的狭窄通道。\n阳光`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
