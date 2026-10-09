# RH_DLSS5FrameInterpolation

## 节点类型

`RH_DLSS5FrameInterpolation`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `video:VIDEO`（2 次）
- `image:IMAGE`（2 次）
- `audio:AUDIO`（2 次）
- `output_fps:COMBO`（2 次）
- `motion:COMBO`（2 次）
- `scene_change_threshold:FLOAT`（2 次）
- `keep_audio:COMBO`（2 次）
- `runtime_dir:STRING`（2 次）
- `wine_prefix:STRING`（2 次）

## 输出

- `images:IMAGE`（2 次）
- `video:VIDEO`（2 次）
- `status:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2x", "auto", 0.24, "on", "", ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
