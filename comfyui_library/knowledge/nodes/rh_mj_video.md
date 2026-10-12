# RH_MJ_Video

## 节点类型

`RH_MJ_Video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `motion:COMBO`（2 次）
- `notify_hook:STRING`（2 次）
- `seed:INT`（2 次）

## 输出

- `video1:VIDEO`（2 次）
- `video2:VIDEO`（2 次）
- `video3:VIDEO`（2 次）
- `video4:VIDEO`（2 次）
- `task_id:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "high", "", 103968876, "randomize"]`（1 次）
- `["", "high", "", 1587836064, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
