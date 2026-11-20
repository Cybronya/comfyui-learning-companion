---
key: 平台全量/Wan2.2-Animate动作迁移流官方流for循环（适配小显存8G）+sam3背景替换_2033058828845064193.json
name: Wan2.2-Animate动作迁移流官方流for循环（适配小显存8G）+sam3背景替换_2033058828845064193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Animate动作迁移流官方流for循环（适配小显存8G）+sam3背景替换_2033058828845064193.json
hash: 97264d4dcc33428f
coverage: 0.881356
learned_at: 2026-11-14 01:05:57
nodes: [TrimVideoLatent, KSampler, CLIPVisionEncode, DWPreprocessor, INTConstant, INTConstant, VHS_VideoInfoLoaded, VAELoader, WanAnimateToVideo, TrimVideoLatent, VAEDecode, VHS_GetImageCount, ImageFromBatch, ModelSamplingSD3, VAEDecode, ModelSamplingSD3, PixelPerfectResolution, DWPreprocessor, SetNode, GetNode, UNETLoader, SimpleMath+, KSampler, CLIPTextEncode, WanAnimateToVideo, easy sam3VideoModelExtraConfig, ImageBlend, VHS_VideoCombine, GetNode, GetNode, CLIPTextEncode, DrawMaskOnImage, SetNode, easy sam3VideoSegmentation, SetNode, workflow>背景与主体遮罩, Reroute, VHS_VideoCombine, GetImageSizeAndCount, easy sam3ModelLoader, easy framesEditor, LoraLoaderModelOnly, LoraLoaderModelOnly, UnetLoaderGGUF, LoadImage, VHS_LoadVideo, INTConstant, CLIPVisionLoader, TorchCompileModel, PathchSageAttentionKJ, VantageWanBlockSwap, CLIPLoader, SimpleMath+, easy forLoopEnd, ImageBatch, easy forLoopStart, Display Int (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 888, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2-Animate动作迁移流官方流for循环（适配小显存8G）+sam3背景替换_2033058828845064193.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Animate动作迁移流官方流for循环（适配小显存8G）+sam3背景替换_2033058828845064193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（59 个）：
- `TrimVideoLatent`
- `KSampler` ★核心
- `CLIPVisionEncode`
- `DWPreprocessor`
- `INTConstant`
- `INTConstant`
- `VHS_VideoInfoLoaded`
- `VAELoader`
- `WanAnimateToVideo`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `ImageFromBatch`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `SetNode`
- `GetNode`
- `UNETLoader` ★核心
- `SimpleMath+`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `WanAnimateToVideo`
- `easy sam3VideoModelExtraConfig`
- `ImageBlend`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `DrawMaskOnImage`
- `SetNode`
- `easy sam3VideoSegmentation`
- `SetNode`
- `workflow>背景与主体遮罩`
- `Reroute`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `easy sam3ModelLoader`
- `easy framesEditor`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `VHS_LoadVideo`
- `INTConstant`
- `CLIPVisionLoader`
- `TorchCompileModel`
- `PathchSageAttentionKJ`
- `VantageWanBlockSwap`
- `CLIPLoader`
- `SimpleMath+`
- `easy forLoopEnd`
- `ImageBatch`
- `easy forLoopStart`
- `Display Int (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `888`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（52/59）

**有卡**：`TrimVideoLatent`、`KSampler`、`CLIPVisionEncode`、`DWPreprocessor`、`INTConstant`、`VHS_VideoInfoLoaded`、`VAELoader`、`WanAnimateToVideo`、`VAEDecode`、`VHS_GetImageCount`、`ImageFromBatch`、`ModelSamplingSD3`、`PixelPerfectResolution`、`UNETLoader`、`SimpleMath+`、`CLIPTextEncode`、`easy sam3VideoModelExtraConfig`、`ImageBlend`、`VHS_VideoCombine`、`DrawMaskOnImage`、`easy sam3VideoSegmentation`、`workflow>背景与主体遮罩`、`GetImageSizeAndCount`、`easy sam3ModelLoader`、`easy framesEditor`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`LoadImage`、`VHS_LoadVideo`、`CLIPVisionLoader`、`TorchCompileModel`、`PathchSageAttentionKJ`、`VantageWanBlockSwap`、`CLIPLoader`、`easy forLoopEnd`、`ImageBatch`、`easy forLoopStart`、`Display Int (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
