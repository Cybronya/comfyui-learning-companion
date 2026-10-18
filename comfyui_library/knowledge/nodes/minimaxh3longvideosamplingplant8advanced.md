# MiniMaxH3LongVideoSamplingPlanT8Advanced

## 节点类型

`MiniMaxH3LongVideoSamplingPlanT8Advanced`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mode:COMBO`（1 次）
- `extra_tail_steps:INT`（1 次）
- `tail_spacing:COMBO`（1 次）
- `manual_sigmas:STRING`（1 次）

## 输出

- `sampling_plan:H3_T8_LONG_VIDEO_SAMPLING_PLAN`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["manual_second_pass", 0, "video_sigma_linear", "0.5, 0.412, 0.350, 0"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
