# RH_RhartVideoSparkvideo20MiniMultimodalVideo

## 节点类型

`RH_RhartVideoSparkvideo20MiniMultimodalVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `image4:IMAGE`（3 次）
- `image5:IMAGE`（3 次）
- `image6:IMAGE`（3 次）
- `image7:IMAGE`（3 次）
- `image8:IMAGE`（3 次）
- `image9:IMAGE`（3 次）
- `video1:VIDEO`（3 次）

## 输出

- `video:VIDEO`（3 次）
- `url:STRING`（3 次）
- `response:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["image1的图像用video1的生长动画和运镜展示，不要video的画面内容", "720p", "10", true, "adaptive", true, "all", false, -1, "randomize", false]`（2 次）
- `["", "720p", "10", true, "9:16", true, "all", false, 2131433209, "randomize", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
