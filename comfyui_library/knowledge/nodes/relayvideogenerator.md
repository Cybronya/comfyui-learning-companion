# RelayVideoGenerator

## 节点类型

`RelayVideoGenerator`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `info:STRING`（1 次）
- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `image4:IMAGE`（1 次）
- `image5:IMAGE`（1 次）
- `image6:IMAGE`（1 次）
- `image7:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `ratio:COMBO`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `task_id:STRING`（1 次）
- `response:STRING`（1 次）
- `video_url:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["图1的单头女子在跳踢踏舞，并说到：“豆包真棒”", "auto", "720P", "10", 737821281272477, "randomize", "true", "false"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
