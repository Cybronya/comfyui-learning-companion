# easy multiTrackEditor

## 节点类型

`easy multiTrackEditor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `prompt_override:*`（5 次）
- `image:IMAGE`（5 次）
- `audio:AUDIO`（5 次）
- `video:VIDEO`（5 次）
- `resolution:COMFY_DYNAMICCOMBO_V3`（5 次）
- `resolution.aspect_ratio:COMBO`（5 次）
- `resolution.megapixels:FLOAT`（5 次）
- `format:COMBO`（5 次）
- `track_data:TRACK_DATA`（5 次）

## 输出

- `TRACKS_INFO:TRACKS_INFO`（5 次）
- `IMAGES:IMAGE`（5 次）
- `AUDIO:AUDIO`（5 次）
- `VIDEO:VIDEO`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["width x height (megapixels)", "9:16 (Portrait Widescreen)", 2, "MiniMax", "{\"muted\":false,\"volume_db\":0,\"tracks\"`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
