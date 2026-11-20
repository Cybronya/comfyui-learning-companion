---
key: 平台全量/各种视频水印去除，含seedance2.0即梦水印去除（支持自动遮罩，手动遮罩）_2020682584543469569.json
name: 各种视频水印去除，含seedance2.0即梦水印去除（支持自动遮罩，手动遮罩）_2020682584543469569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/各种视频水印去除，含seedance2.0即梦水印去除（支持自动遮罩，手动遮罩）_2020682584543469569.json
hash: 3e3e0353ae0fd1f1
coverage: 0.571429
learned_at: 2026-11-14 01:51:48
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, MathExpression|pysssss, GetNode, GetNode, GetNode, RepeatImageBatch, ImageResizeKJv2, ImageResizeKJv2, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, GrowMaskWithBlur, MaskToImage, RepeatImageBatch, DiffuEraserLoader, DiffuEraserSampler, WatermarkDetectorLoader, ImageResizeKJv2, ImageConcanate, GetNode, DiffuEraserLoader, GetNode, GetNode, FlashVSRNode, SetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), easy compare, GetNode, DiffuEraserSampler, MathExpression|pysssss, GetImagesFromBatchIndexed, GetNode, GetNode, ImageResizeKJv2, Any Switch (rgthree), Any Switch (rgthree), VHS_VideoCombine, easy ifElse, MaskPreview+, WatermarkDetector, MaskToImage, GetNode, GetNode, GetNode, DiffuEraserSampler, GetNode, ImageConcanate, DiffuEraserLoader, ImageResizeKJv2, GetNode, FlashVSRNode, LoadImage, MaskToImage, VHS_LoadVideo, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfo, SetNode, RepeatImageBatch, GetNode, Fast Groups Muter (rgthree), FlashVSRNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/各种视频水印去除，含seedance2.0即梦水印去除（支持自动遮罩，手动遮罩）_2020682584543469569.json

> 来源文件 `comfyui_library/workflows/平台全量/各种视频水印去除，含seedance2.0即梦水印去除（支持自动遮罩，手动遮罩）_2020682584543469569.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（84 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `RepeatImageBatch`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GrowMaskWithBlur`
- `MaskToImage`
- `RepeatImageBatch`
- `DiffuEraserLoader`
- `DiffuEraserSampler` ★核心
- `WatermarkDetectorLoader`
- `ImageResizeKJv2`
- `ImageConcanate`
- `GetNode`
- `DiffuEraserLoader`
- `GetNode`
- `GetNode`
- `FlashVSRNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `easy compare`
- `GetNode`
- `DiffuEraserSampler` ★核心
- `MathExpression|pysssss`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `VHS_VideoCombine`
- `easy ifElse`
- `MaskPreview+`
- `WatermarkDetector`
- `MaskToImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `DiffuEraserSampler` ★核心
- `GetNode`
- `ImageConcanate`
- `DiffuEraserLoader`
- `ImageResizeKJv2`
- `GetNode`
- `FlashVSRNode`
- `LoadImage`
- `MaskToImage`
- `VHS_LoadVideo`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfo`
- `SetNode`
- `RepeatImageBatch`
- `GetNode`
- `Fast Groups Muter (rgthree)`
- `FlashVSRNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **57%**（48/84）

**有卡**：`MathExpression|pysssss`、`RepeatImageBatch`、`ImageResizeKJv2`、`LoadImage`、`GrowMaskWithBlur`、`MaskToImage`、`DiffuEraserLoader`、`DiffuEraserSampler`、`WatermarkDetectorLoader`、`ImageConcanate`、`FlashVSRNode`、`easy compare`、`GetImagesFromBatchIndexed`、`VHS_VideoCombine`、`MaskPreview+`、`WatermarkDetector`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、ImageResizeKJv2、MaskPreview+、DiffuEraserLoader、easy compare、FlashVSRNode
