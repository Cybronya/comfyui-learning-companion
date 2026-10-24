# HMPipelineImage

## 节点类型

`HMPipelineImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `hm_image_pipeline:HMIMAGEPIPELINE`（6 次）
- `ref_head_pose:HEAD_POSE`（6 次）
- `ref_expression:EXPRESSION`（6 次）
- `drive_head_pose:HEAD_POSE`（6 次）
- `drive_expression:EXPRESSION`（6 次）
- `prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）

## 输出

- `IMAGE:IMAGE`（6 次）
- `LATENT:LATENT`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "", "", 25, 744436851193818, "randomize", 1.5, -1]`（1 次）
- `[0, "", "", 25, 285022768417059, "randomize", 1.5, -1]`（1 次）
- `[0, "", "", 25, 513133866158575, "randomize", 1.2000000000000002, 0]`（1 次）
- `[0, "", "", 25, 20743671025631, "randomize", 1.2000000000000002, 0]`（1 次）
- `[0, "", "", 25, 624529011481719, "randomize", 1.5, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
