# RunningHub Univideo Generator(MultiID)

## 节点类型

`RunningHub Univideo Generator(MultiID)`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `pipeline:RH_Univideo_Pipeline`（4 次）
- `ref_image1:IMAGE`（4 次）
- `ref_image2:IMAGE`（4 次）
- `ref_image3:IMAGE`（4 次）
- `prompt:STRING`（4 次）
- `width:INT`（4 次）
- `height:INT`（4 次）
- `num_frames:INT`（4 次）
- `sample_steps:INT`（4 次）
- `fps:INT`（4 次）

## 输出

- `video:VIDEO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A girl, now dressed in a bikini, sits comfortably on a beach lounge chair. On her right shoulder, a fluffy, yellow Pik`（1 次）
- `["A girl, now dressed in a bikini, sits comfortably on a beach lounge chair. On her right shoulder, a fluffy, yellow Pik`（1 次）
- `["A girl, now dressed in a bikini, sits comfortably on a beach lounge chair. On her right shoulder, a fluffy, yellow Pik`（1 次）
- `["A girl, now dressed in a bikini, sits comfortably on a beach lounge chair. On her right shoulder, a fluffy, yellow Pik`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
