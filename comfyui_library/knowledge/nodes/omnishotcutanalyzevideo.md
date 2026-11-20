# OmniShotCutAnalyzeVideo

## 节点类型

`OmniShotCutAnalyzeVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video:VIDEO`（1 次）
- `checkpoint_name:COMBO`（1 次）
- `mode:COMBO`（1 次）
- `num_context_frames:INT`（1 次）

## 输出

- `result_json:STRING`（1 次）
- `shot_count:INT`（1 次）
- `fps:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["OmniShotCut_ckpt.pth", "default", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
