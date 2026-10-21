# RH_TopazlabsImageUpscaleHighFidelityV3

## 节点类型

`RH_TopazlabsImageUpscaleHighFidelityV3`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `opacity:FLOAT`（2 次）
- `recoveryStrength:FLOAT`（2 次）
- `strength:FLOAT`（2 次）
- `fixCompression:FLOAT`（2 次）
- `denoise:FLOAT`（2 次）
- `sharpen:FLOAT`（2 次）
- `subjectDetection:COMBO`（2 次）
- `faceEnhancementCreativity:FLOAT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1, 0.25, 0.5, 0.3, 0.3, "All", 0, 0.8, true, false, 1920, 1080, "png", false, 751418100, "randomize"]`（1 次）
- `[1, 1, 0.25, 0.5, 0.3, 0.3, "All", 0, 0.8, true, false, 1920, 1080, "png", false, 1732977036, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
