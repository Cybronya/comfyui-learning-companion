# SAM3VideoSegmentation

## 节点类型

`SAM3VideoSegmentation`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `video_frames:IMAGE`（3 次）
- `video:VIDEO`（3 次）
- `positive_points:SAM3_POINTS_PROMPT`（3 次）
- `negative_points:SAM3_POINTS_PROMPT`（3 次）
- `prompt_mode:COMBO`（3 次）
- `text_prompt:STRING`（3 次）
- `frame_idx:INT`（3 次）
- `score_threshold:FLOAT`（3 次）

## 输出

- `video_state:SAM3_VIDEO_STATE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["point", 0.3, 0.3]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
