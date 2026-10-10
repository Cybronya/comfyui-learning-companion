---
key: 视频生成/文生视频/最新 WAN 2.2 Animate V2+SeC Mask新遮罩+继续运动+循环和细节升级工作流_1980274281676496897.json
name: 最新 WAN 2.2 Animate V2+SeC Mask新遮罩+继续运动+循环和细节升级工作流_1980274281676496897
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/最新 WAN 2.2 Animate V2+SeC Mask新遮罩+继续运动+循环和细节升级工作流_1980274281676496897.json
hash: 86c8b143e9612ddc
coverage: 0.408602
learned_at: 2026-10-10 23:13:21
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UnetLoaderGGUF, TorchCompileModel, ModelPatchTorchSettings, SetNode, SetNode, PathchSageAttentionKJ, SetNode, PreviewImage, SetNode, SetNode, SetNode, CLIPVisionLoader, CLIPVisionEncode, GetNode, PreviewAnimation, PreviewAnimation, SetNode, SetNode, CLIPTextEncode, GetNode, easy showAnything, GetNode, ImageUpscaleWithModel, UpscaleModelLoader, GetNode, easy showAnything, WanAnimateToVideo, KSampler, GetNode, GetNode, GetNode, SetNode, DrawViTPose, PoseAndFaceDetection, VHS_VideoCombine, KSampler, VAEDecode, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, DrawMaskOnImage, SetNode, VAEDecode, GetNode, WanAnimateToVideo, ImageFromBatch, SetNode, GetNode, DrawMaskOnImage, easy showAnything, ImageFromBatch, ImageBatch, easy forLoopEnd, easy showAnything, easy forLoopStart, easy cleanGpuUsed, GetNode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, VAEDecode, ModelSamplingSD3, GetNode, WanVideoEnhanceAVideoKJ, ContextWindowsManual, VAEEncode, GetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, FloatConstant, ImageResizeKJv2, Fast Groups Bypasser (rgthree), KSampler, ImageBatch, GetNode, ImageResizeKJv2, ImageUpscaleWithModel, SetNode, GetNode, Reroute, Reroute, Reroute, LoadImage, GetImageSizeAndCount, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, OnnxDetectionModelLoader, SetNode, SetNode, Reroute, SetNode, CLIPTextEncode, GetNode, CLIPTextEncode, TorchCompileModel, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, UpscaleModelLoader, Note, Note, Display Int (rgthree), PrimitiveInt, ResolutionMaster, CLIPTextEncode, PoseRetargetPromptHelper, easy showAnything, easy showAnything, PreviewAnimation, SetNode, VHS_VideoInfoLoaded, SeCVideoSegmentation, GrowMaskWithBlur, BlockifyMask, SeCModelLoader, Note, Note, GetNode, Fast Groups Bypasser (rgthree), PointsEditor, INTConstant, FloatConstant, SetNode, SetNode, INTConstant, SetNode, FloatConstant, GetNode, GetNode, easy showAnything, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, GetNode, VHS_VideoCombine, GetNode, SetNode, SetNode, SetNode, MathExpression|pysssss, GetNode, TrimVideoLatent, easy cleanGpuUsed, GetNode, GetNode]
patterns: [image_to_image]
missing: [Display Int (rgthree), MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, easy forLoopEnd, easy forLoopStart]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.15, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 888, "steps": 10}
discoveries: [次要节点 `Display Int (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/最新 WAN 2.2 Animate V2+SeC Mask新遮罩+继续运动+循环和细节升级工作流_1980274281676496897.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/最新 WAN 2.2 Animate V2+SeC Mask新遮罩+继续运动+循环和细节升级工作流_1980274281676496897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（186 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UnetLoaderGGUF` ★核心
- `TorchCompileModel`
- `ModelPatchTorchSettings`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `GetNode`
- `PreviewAnimation`
- `PreviewAnimation`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `easy showAnything`
- `GetNode`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `GetNode`
- `easy showAnything`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `WanAnimateToVideo`
- `ImageFromBatch`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `easy showAnything`
- `ImageFromBatch`
- `ImageBatch`
- `easy forLoopEnd`
- `easy showAnything`
- `easy forLoopStart`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `GetNode`
- `WanVideoEnhanceAVideoKJ`
- `ContextWindowsManual`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `FloatConstant`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `ImageBatch`
- `GetNode`
- `ImageResizeKJv2`
- `ImageUpscaleWithModel`
- `SetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoadImage`
- `GetImageSizeAndCount`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `Reroute`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `TorchCompileModel`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `Note`
- `Note`
- `Display Int (rgthree)`
- `PrimitiveInt`
- `ResolutionMaster`
- `CLIPTextEncode` ★核心
- `PoseRetargetPromptHelper`
- `easy showAnything`
- `easy showAnything`
- `PreviewAnimation`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SeCVideoSegmentation`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `SeCModelLoader`
- `Note`
- `Note`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `PointsEditor`
- `INTConstant`
- `FloatConstant`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `FloatConstant`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `TrimVideoLatent`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `888`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.15`

## 知识

覆盖率 **41%**（76/186）

**有卡**：`UnetLoaderGGUF`、`TorchCompileModel`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CLIPVisionLoader`、`CLIPVisionEncode`、`PreviewAnimation`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`WanAnimateToVideo`、`KSampler`、`DrawViTPose`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`VAEDecode`、`TrimVideoLatent`、`ImageResizeKJv2`、`DrawMaskOnImage`、`ImageFromBatch`、`ImageBatch`、`ModelSamplingSD3`、`WanVideoEnhanceAVideoKJ`、`ContextWindowsManual`、`VAEEncode`、`FloatConstant`、`LoadImage`、`GetImageSizeAndCount`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`OnnxDetectionModelLoader`、`ResolutionMaster`、`PoseRetargetPromptHelper`、`VHS_VideoInfoLoaded`、`SeCVideoSegmentation`、`GrowMaskWithBlur`、`BlockifyMask`、`SeCModelLoader`、`PointsEditor`、`INTConstant`、`VHS_LoadVideo`

**缺卡**（12）：`Display Int (rgthree)`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy clearCacheAll`、`easy forLoopEnd`、`easy forLoopStart`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Display Int (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
