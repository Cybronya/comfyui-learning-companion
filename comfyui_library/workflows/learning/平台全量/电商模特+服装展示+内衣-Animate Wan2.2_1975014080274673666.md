---
key: 平台全量/电商模特+服装展示+内衣-Animate Wan2.2_1975014080274673666.json
name: 电商模特+服装展示+内衣-Animate Wan2.2_1975014080274673666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/电商模特+服装展示+内衣-Animate Wan2.2_1975014080274673666.json
hash: e46a1e44de61710d
coverage: 0.536842
learned_at: 2026-11-14 02:24:44
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PreviewImage, SetNode, CLIPVisionEncode, RembgByBiRefNet, SetNode, SetNode, SetNode, CLIPVisionLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, wanBlockSwap, WanAnimateToVideo, LayerUtility: ImageRemoveAlpha, GetNode, GetNode, LoraLoaderModelOnly, GetNode, GetNode, GetNode, ImageConcatMulti, GetImageSizeAndCount, PlaySound|pysssss, PlaySound|pysssss, PlaySound|pysssss, PlaySound|pysssss, ImageConcatMulti, PoseAndFaceDetection, easy cleanGpuUsed, easy sleep, SetNode, DrawViTPose, SetNode, GetNode, UnetLoaderGGUF, LayerMask: SegformerB2ClothesUltra, GrowMask, BlockifyMask, DrawMaskOnImage, SetNode, SetNode, GetNode, GetNode, Int, CLIPTextEncode, SetNode, SetNode, SetNode, CLIPTextEncode, PathchSageAttentionKJ, TorchCompileModelWanVideoV2, ModelSamplingSD3, SetNode, VAELoader, CLIPLoader, VAEDecode, TrimVideoLatent, GetNode, SetNode, KSampler, GetNode, MarkdownNote, LoadImage, GetNode, GetNode, OnnxDetectionModelLoader, SetNode, ImageResizeKJv2, SetNode, SimpleMath+, easy showAnything, StringToInt, easy showAnything, VHS_VideoCombine, SetNode, VHS_VideoCombine, VHS_VideoCombine, AutoDownloadBiRefNetModel, ImageResizeKJv2, SetNode, GetNode, DF_Integer, LoadImage, VHS_LoadVideo, PreviewImage, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 823099774639999, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/电商模特+服装展示+内衣-Animate Wan2.2_1975014080274673666.json

> 来源文件 `comfyui_library/workflows/平台全量/电商模特+服装展示+内衣-Animate Wan2.2_1975014080274673666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `CLIPVisionEncode`
- `RembgByBiRefNet`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `WanAnimateToVideo`
- `LayerUtility: ImageRemoveAlpha`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `ImageConcatMulti`
- `PoseAndFaceDetection`
- `easy cleanGpuUsed`
- `easy sleep`
- `SetNode`
- `DrawViTPose`
- `SetNode`
- `GetNode`
- `UnetLoaderGGUF` ★核心
- `LayerMask: SegformerB2ClothesUltra`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Int`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `TorchCompileModelWanVideoV2`
- `ModelSamplingSD3`
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `GetNode`
- `SetNode`
- `KSampler` ★核心
- `GetNode`
- `MarkdownNote`
- `LoadImage`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SimpleMath+`
- `easy showAnything`
- `StringToInt`
- `easy showAnything`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `AutoDownloadBiRefNetModel`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `DF_Integer`
- `LoadImage`
- `VHS_LoadVideo`
- `PreviewImage`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `823099774639999`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **54%**（51/95）

**有卡**：`CLIPVisionEncode`、`RembgByBiRefNet`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`wanBlockSwap`、`WanAnimateToVideo`、`LayerUtility: ImageRemoveAlpha`、`ImageConcatMulti`、`GetImageSizeAndCount`、`PlaySound|pysssss`、`PoseAndFaceDetection`、`easy cleanGpuUsed`、`easy sleep`、`DrawViTPose`、`UnetLoaderGGUF`、`LayerMask: SegformerB2ClothesUltra`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`Int`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`TorchCompileModelWanVideoV2`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`TrimVideoLatent`、`KSampler`、`LoadImage`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`SimpleMath+`、`StringToInt`、`VHS_VideoCombine`、`AutoDownloadBiRefNetModel`、`DF_Integer`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、CLIPVisionEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
