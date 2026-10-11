# LoadVideoNode

## 节点类型

`LoadVideoNode`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `video_file:COMBO`（14 次）
- `upload:IMAGEUPLOAD`（14 次）

## 输出

- `video:VIDEO`（14 次）
- `audio:AUDIO`（14 次）
- `filename:STRING`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["c7f49f902e24902a324c202aa93f1c64519c68730c5e96771db7a18c1916b6a2.mp4", "image"]`（3 次）
- `["23274869543dc5cd0f384cedb3be021e3d4829fd087850d98cfc95b973972b20.mp4", "image"]`（2 次）
- `["67b5871272d914289e9c3e7e7f4e162b7b0b3fc9b90b452298d41bc0a2f3b213.mp4", "image"]`（1 次）
- `["9f4d0ff680aaefe7d7b443218c90de201e642a61a013d64c409d181cdc5d1f93.mp4", "image"]`（1 次）
- `["f8987697fe3544503c0768b32ddf60e377ebe9dbbd25ed3eaf2bdeb997e0c4db.mp4", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
