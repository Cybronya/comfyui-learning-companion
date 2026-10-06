# SaveVideo

## 节点类型

`SaveVideo`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 24 个 workflow 中。

## 输入

- `video:VIDEO`（31 次）
- `filename_prefix:STRING`（31 次）
- `format:COMFY_DYNAMICCOMBO_V3`（29 次）
- `codec:COMFY_DYNAMICCOMBO_V3`（29 次）
- `format.codec:COMFY_DYNAMICCOMBO_V3`（29 次）
- `format.codec.encoding:COMFY_DYNAMICCOMBO_V3`（4 次）
- `format:COMBO`（2 次）
- `codec:COMBO`（2 次）

## 输出

- `video_url:STRING`（31 次）
- `video:VIDEO`（31 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["video/ComfyUI", "auto", "auto", "auto"]`（7 次）
- `["H3抽帧视频/图片", "auto", "auto", "auto"]`（5 次）
- `["video/H3_MultiTrack_Final", "auto", "auto", "auto"]`（5 次）
- `["hailuoH3", "mp4", "h264", "auto", "auto"]`（3 次）
- `["video/MiniMax_H3_24G_BALANCED_NATIVE_24fps", "auto", "auto", "auto"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
