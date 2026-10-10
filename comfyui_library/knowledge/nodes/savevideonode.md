# SaveVideoNode

## 节点类型

`SaveVideoNode`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `video:VIDEO`（1 次）
- `audio:AUDIO`（1 次）
- `output_path:STRING`（1 次）
- `filename_prefix:STRING`（1 次）
- `fps:COMBO`（1 次）
- `video_format:COMBO`（1 次）
- `codec:COMBO`（1 次）
- `preset:COMBO`（1 次）
- `crf:COMBO`（1 次）

## 输出

- `保存信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["video", "视频", "自动", "mp4", "自动", "fast", "自动", "自动", "自动"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
