# BatchExtractFrameFromVideoNode

## 节点类型

`BatchExtractFrameFromVideoNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `folder_selection_mode:COMBO`（1 次）
- `video_folder:COMBO`（1 次）
- `custom_video_folder_path:STRING`（1 次）
- `frame_extraction_method:COMBO`（1 次）
- `frame_number:INT`（1 次）
- `timestamp:FLOAT`（1 次）
- `output_format:COMBO`（1 次）
- `image_quality:INT`（1 次）
- `output_filename_prefix:STRING`（1 次）
- `output_folder:STRING`（1 次）

## 输出

- `image_paths:STRING`（1 次）
- `frame_indices:INT`（1 次）
- `status_message:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["select_from_input_dir", "video", "", "frame_number", 1, 0, "png", 100, "mums_batch", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
