# RH_TopazlabsImageUpscaleTextRefine

## 节点类型

`RH_TopazlabsImageUpscaleTextRefine`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `scale:COMBO`（1 次）
- `subjectDetection:COMBO`（1 次）
- `faceEnhancement:BOOLEAN`（1 次）
- `faceEnhancementCreativity:FLOAT`（1 次）
- `faceEnhancementStrength:FLOAT`（1 次）
- `skip_error:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2x", "All", true, 0, 0.8, false, 995198089600526, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
