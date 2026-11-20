---
key: 平台全量/Bernini_testing_video_edit+flashvsr放大，适合小显存_2069055524376764418.json
name: Bernini_testing_video_edit+flashvsr放大，适合小显存_2069055524376764418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Bernini_testing_video_edit+flashvsr放大，适合小显存_2069055524376764418.json
hash: 195b2df162090798
coverage: 0.907407
learned_at: 2026-11-14 00:20:18
nodes: [CLIPLoader, MarkdownNote, VantageWanBlockSwap, VantageWanBlockSwap, VAELoader, VHS_VideoInfo, CLIPTextEncode, BerniniConditioning, MarkdownNote, easy forLoopStart, PreviewAny, AudioConcat, SimpleCalculatorKJ, Note, SimpleCalculatorKJ, CLIPTextEncode, FloatConstant, BatchImagesNode, SamplerCustom, BasicScheduler, SplitSigmas, KSamplerSelect, SamplerCustom, VAEDecode, INTConstant, INTConstant, Note, WanVideoBlockSwap, WanVideoSchedulerv2, WanVideoAddFlashVSRInput, WanVideoFlashVSRDecoderLoader, WanVideoEmptyEmbeds, GetImageSizeAndCount, WanVideoContextOptions, WanVideoSamplerExtraArgs, ImageResizeKJv2, WanVideoDecode, WanVideoSamplerv2, VHS_VideoCombine, SimpleMath+, LoraLoaderModelOnly, LoraLoaderModelOnly, WanVideoTextEncodeCached, LoadImage, INTConstant, INTConstant, easy forLoopEnd, easy batchAnything, ImageFromBatch, VHS_LoadVideo, WanVideoExtraModelSelect, WanVideoModelLoader, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ]
patterns: []
missing: []
---

# 平台全量/Bernini_testing_video_edit+flashvsr放大，适合小显存_2069055524376764418.json

> 来源文件 `comfyui_library/workflows/平台全量/Bernini_testing_video_edit+flashvsr放大，适合小显存_2069055524376764418.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（54 个）：
- `CLIPLoader`
- `MarkdownNote`
- `VantageWanBlockSwap`
- `VantageWanBlockSwap`
- `VAELoader`
- `VHS_VideoInfo`
- `CLIPTextEncode` ★核心
- `BerniniConditioning`
- `MarkdownNote`
- `easy forLoopStart`
- `PreviewAny`
- `AudioConcat`
- `SimpleCalculatorKJ`
- `Note`
- `SimpleCalculatorKJ`
- `CLIPTextEncode` ★核心
- `FloatConstant`
- `BatchImagesNode`
- `SamplerCustom` ★核心
- `BasicScheduler`
- `SplitSigmas`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `INTConstant`
- `INTConstant`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoSchedulerv2`
- `WanVideoAddFlashVSRInput`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoEmptyEmbeds`
- `GetImageSizeAndCount`
- `WanVideoContextOptions`
- `WanVideoSamplerExtraArgs` ★核心
- `ImageResizeKJv2`
- `WanVideoDecode`
- `WanVideoSamplerv2` ★核心
- `VHS_VideoCombine`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanVideoTextEncodeCached`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `easy forLoopEnd`
- `easy batchAnything`
- `ImageFromBatch`
- `VHS_LoadVideo`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`

## 知识

覆盖率 **91%**（49/54）

**有卡**：`CLIPLoader`、`VantageWanBlockSwap`、`VAELoader`、`VHS_VideoInfo`、`CLIPTextEncode`、`BerniniConditioning`、`easy forLoopStart`、`AudioConcat`、`SimpleCalculatorKJ`、`FloatConstant`、`BatchImagesNode`、`SamplerCustom`、`BasicScheduler`、`SplitSigmas`、`KSamplerSelect`、`VAEDecode`、`INTConstant`、`WanVideoBlockSwap`、`WanVideoSchedulerv2`、`WanVideoAddFlashVSRInput`、`WanVideoFlashVSRDecoderLoader`、`WanVideoEmptyEmbeds`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`WanVideoSamplerExtraArgs`、`ImageResizeKJv2`、`WanVideoDecode`、`WanVideoSamplerv2`、`VHS_VideoCombine`、`SimpleMath+`、`LoraLoaderModelOnly`、`WanVideoTextEncodeCached`、`LoadImage`、`easy forLoopEnd`、`easy batchAnything`、`ImageFromBatch`、`VHS_LoadVideo`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`DiffusionModelLoaderKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom
