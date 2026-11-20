---
key: 平台全量/Qwen image_edit_ControlNet_1961270893328666626.json
name: Qwen image_edit_ControlNet_1961270893328666626
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen image_edit_ControlNet_1961270893328666626.json
hash: f26c398544415065
coverage: 0.814815
learned_at: 2026-11-14 00:50:48
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, Anything Everywhere, Anything Everywhere, Anything Everywhere, ModelSamplingAuraFlow, SeedVR2BlockSwap, CFGNorm, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Image Comparer (rgthree), SetUnionControlNetType, SaveImage, Note, SeedVR2GGUF, AIO_Preprocessor, UNETLoader, PrimitiveFloat, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, ControlNetLoader, TextEncodeQwenImageEdit, TextEncodeQwenImageEdit, KSampler, EmptyLatentImage, CR Text, LoadImage, ControlNetApplyAdvanced, LoraLoaderModelOnly, PreviewImage, LoadImage, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, KSampler, SeedVR2BlockSwap, SeedVR2GGUF, PreviewImage, SaveImage, LoadImage, ControlNetApplyAdvanced, CFGNorm, ControlNetLoader, SetUnionControlNetType, AIO_Preprocessor, PreviewImage, ModelSamplingAuraFlow, CLIPLoader, VAELoader, VAEDecode, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1, "denoise": 1, "height": 1376, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 397623419622816, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen image_edit_ControlNet_1961270893328666626.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen image_edit_ControlNet_1961270893328666626.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `ModelSamplingAuraFlow`
- `SeedVR2BlockSwap`
- `CFGNorm`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SetUnionControlNetType`
- `SaveImage`
- `Note`
- `SeedVR2GGUF`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `PrimitiveFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `ControlNetLoader`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEdit`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `CR Text`
- `LoadImage`
- `ControlNetApplyAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SeedVR2BlockSwap`
- `SeedVR2GGUF`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `ControlNetApplyAdvanced` ★核心
- `CFGNorm`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `397623419622816`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1376`
- `batch_size` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **81%**（44/54）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`SeedVR2BlockSwap`、`CFGNorm`、`LayerUtility: ImageScaleByAspectRatio V2`、`SetUnionControlNetType`、`SaveImage`、`SeedVR2GGUF`、`AIO_Preprocessor`、`UNETLoader`、`VAEDecode`、`ControlNetLoader`、`TextEncodeQwenImageEdit`、`KSampler`、`EmptyLatentImage`、`CR Text`、`LoadImage`、`ControlNetApplyAdvanced`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
