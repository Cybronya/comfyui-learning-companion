# RunningHub Univideo Editor

## 节点类型

`RunningHub Univideo Editor`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `pipeline:RH_Univideo_Pipeline`（3 次）
- `ref_video:VIDEO`（3 次）
- `ref_image:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `num_frames:INT`（3 次）
- `sample_steps:INT`（3 次）
- `fps:INT`（3 次）
- `seed:INT`（3 次）

## 输出

- `video:VIDEO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Change the man to look like he is sculpted from chocolate.", 832, 480, 81, 20, 24, 181100133220799, "randomize"]`（1 次）
- `["", 832, 480, 81, 20, 24, 1057509379690859, "randomize"]`（1 次）
- `["", 832, 480, 81, 20, 16, 472874461794068, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
