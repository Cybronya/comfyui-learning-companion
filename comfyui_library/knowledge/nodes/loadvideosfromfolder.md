# LoadVideosFromFolder

## 节点类型

`LoadVideosFromFolder`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `video:STRING`（3 次）
- `force_rate:FLOAT`（3 次）
- `custom_width:INT`（3 次）
- `custom_height:INT`（3 次）
- `frame_load_cap:INT`（3 次）
- `skip_first_frames:INT`（3 次）
- `select_every_nth:INT`（3 次）
- `output_type:COMBO`（3 次）
- `grid_max_columns:INT`（3 次）
- `add_label:BOOLEAN`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["E:\\ComfyUI_windows_portable\\ComfyUI\\output\\MusicVideo\\mynewvideo", 0, 0, 0, 0, 0, 1, "batch", 4, false]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
