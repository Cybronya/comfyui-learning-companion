---
key: 视频生成/图生视频/Wan2.2自动反推图生视频｜Remix3.0人物特效一键出片_2103065382646018049.json
name: Wan2.2自动反推图生视频｜Remix3.0人物特效一键出片_2103065382646018049
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2自动反推图生视频｜Remix3.0人物特效一键出片_2103065382646018049.json
hash: b19a06ea85ed4c2e
coverage: 0.656489
learned_at: 2026-10-17 02:29:30
nodes: [ModelPatchTorchSettings, ModelSamplingSD3, Reroute, Reroute, Reroute, SetNode, SetNode, Reroute, Reroute, SomethingToString, GetNode, Reroute, SetNode, Reroute, Reroute, Reroute, PathchSageAttentionKJ, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, easy setNode, easy cleanGpuUsed, VAEDecode, Reroute, llama_cpp_unload_model, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPTextEncode, CLIPTextEncode, PreviewImage, Reroute, GetNode, FL_RIFE, easy int, easy int, ModelPassThrough, ModelPassThrough, LoraLoaderModelOnly, ModelPassThrough, PathchSageAttentionKJ, ModelPassThrough, VAELoader, easy showAnything, PainterI2V, easy int, UNETLoader, UNETLoader, ModelSamplingSD3, CLIPLoader, CR Prompt Text, llama_cpp_parameters, Reroute, Reroute, WanMoeKSampler, LoraLoaderModelOnly, CR Prompt Text, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, PreviewAny, easy int, SetNode, SetNode, GetNode, easy showAnything, GetNode, easy showAnything, PreviewAudio, PreviewAudio, easy getNode, PlaySound|pysssss, VHS_VideoCombine, llama_cpp_model_loader, PreviewAudio, WujiAudioLoader, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ImageResizeKJv2, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2自动反推图生视频｜Remix3.0人物特效一键出片_2103065382646018049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2自动反推图生视频｜Remix3.0人物特效一键出片_2103065382646018049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（131 个）：
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `SomethingToString`
- `GetNode`
- `Reroute`
- `SetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy setNode`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Reroute`
- `llama_cpp_unload_model`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Reroute`
- `GetNode`
- `FL_RIFE`
- `easy int`
- `easy int`
- `ModelPassThrough`
- `ModelPassThrough`
- `LoraLoaderModelOnly` ★核心
- `ModelPassThrough`
- `PathchSageAttentionKJ`
- `ModelPassThrough`
- `VAELoader`
- `easy showAnything`
- `PainterI2V`
- `easy int`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `CR Prompt Text`
- `llama_cpp_parameters`
- `Reroute`
- `Reroute`
- `WanMoeKSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `PreviewAny`
- `easy int`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `easy showAnything`
- `PreviewAudio`
- `PreviewAudio`
- `easy getNode`
- `PlaySound|pysssss`
- `VHS_VideoCombine`
- `llama_cpp_model_loader`
- `PreviewAudio`
- `WujiAudioLoader`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（86/131）

**有卡**：`ModelPatchTorchSettings`、`ModelSamplingSD3`、`SomethingToString`、`PathchSageAttentionKJ`、`easy setNode`、`easy cleanGpuUsed`、`VAEDecode`、`llama_cpp_unload_model`、`CLIPTextEncode`、`FL_RIFE`、`easy int`、`ModelPassThrough`、`LoraLoaderModelOnly`、`VAELoader`、`PainterI2V`、`UNETLoader`、`CLIPLoader`、`CR Prompt Text`、`llama_cpp_parameters`、`WanMoeKSampler`、`llama_cpp_instruct_adv`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`PreviewAudio`、`easy getNode`、`PlaySound|pysssss`、`VHS_VideoCombine`、`llama_cpp_model_loader`、`WujiAudioLoader`、`ImageResizeKJv2`、`LoadImage`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
