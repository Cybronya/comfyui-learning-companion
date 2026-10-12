# OverlayVideos

## 节点类型

`OverlayVideos`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `bg_video:STRING`（1 次）
- `fg_video:STRING`（1 次）
- `external_audio:STRING`（1 次）
- `x:INT`（1 次）
- `y:INT`（1 次）
- `fg_width:INT`（1 次）
- `fg_height:INT`（1 次）
- `keep_audio_from:COMBO`（1 次）

## 输出

- `video_path:STRING`（1 次）
- `video:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 576, 188, 188, "background"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
