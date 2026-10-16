# ShellAgentPluginVideoCombineEncrypt

## 节点类型

`ShellAgentPluginVideoCombineEncrypt`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `audio:AUDIO`（3 次）
- `vae:VAE`（3 次）
- `frame_rate:FLOAT`（3 次）
- `loop_count:INT`（3 次）
- `filename_prefix:STRING`（3 次）
- `format:COMBO`（3 次）
- `quality:INT`（3 次）
- `pingpong:BOOLEAN`（3 次）
- `encrypt:BOOLEAN`（3 次）

## 输出

- `Filenames:VHS_FILENAMES`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, 0, "ShellAgent_Encrypted", "video/h264-mp4", 65, false, false, "slower", "none", 20, "yuv420p", "bt709", "pc", "", `（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
