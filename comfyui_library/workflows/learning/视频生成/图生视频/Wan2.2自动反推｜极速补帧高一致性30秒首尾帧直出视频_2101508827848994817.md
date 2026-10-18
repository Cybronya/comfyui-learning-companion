---
key: 视频生成/图生视频/Wan2.2自动反推｜极速补帧高一致性30秒首尾帧直出视频_2101508827848994817.json
name: Wan2.2自动反推｜极速补帧高一致性30秒首尾帧直出视频_2101508827848994817
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2自动反推｜极速补帧高一致性30秒首尾帧直出视频_2101508827848994817.json
hash: d934942f5e463778
coverage: 0.388268
learned_at: 2026-10-17 02:14:41
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, VAEDecode, SetNode, GetNode, VAEDecode, SetNode, GetNode, GetNode, VAEDecode, SetNode, GetNode, GetNode, VAEDecode, SetNode, SetNode, GetNode, VAEDecode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, SetNode, SetNode, SetNode, SetNode, SetNode, easy int, Mute / Bypass Relay (rgthree), SetNode, SetNode, easy cleanGpuUsed, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, Mute / Bypass Repeater (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPLoader, VAELoader, easy int, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, GetNode, CLIPTextEncode, VAEDecode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, easy int, SetNode, PrimitiveFloat, GetNode, Mute / Bypass Repeater (rgthree), GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, CLIPTextEncode, GetNode, CLIPTextEncode, ModelSamplingSD3, ModelPassThrough, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, WanAdvancedI2V, WanAdvancedI2V, WanAdvancedI2V, WanAdvancedI2V, WanAdvancedI2V, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, SetNode, ImageFlip, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LayerUtility: ImageReelComposit, SetNode, Fast Groups Bypasser (rgthree), GetNode, GetNode, easy showAnything, easy showAnything, easy showAnything, easy showAnything, easy showAnything, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ModelPassThrough, SetNode, GetNode, SetNode, ImageBatchExtendWithOverlap, Split String, SomethingToString, ModelSamplingSD3, VHS_VideoCombine, ImageResizeKJv2, GetNode, LoadImage, Fast Groups Bypasser (rgthree), PlaySound|pysssss, PlaySound|pysssss, CLIPTextEncode, easy showAnything, CLIPTextEncode, Fast Groups Bypasser (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReel, LoadImage, LoadImage, SaveImage, Fast Groups Bypasser (rgthree), Any Switch (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, llama_cpp_instruct_adv, LoraLoaderModelOnly, easy int, easy int, WanAdvancedI2V, SaveImage, UNETLoader, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, FL_RIFE, easy showAnything, SaveText|pysssss, llama_cpp_parameters, Fast Groups Bypasser (rgthree), UNETLoader, llama_cpp_model_loader, TextInput_, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2自动反推｜极速补帧高一致性30秒首尾帧直出视频_2101508827848994817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2自动反推｜极速补帧高一致性30秒首尾帧直出视频_2101508827848994817.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（358 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `Mute / Bypass Relay (rgthree)`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Mute / Bypass Repeater (rgthree)`
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
- `CLIPLoader`
- `VAELoader`
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `SetNode`
- `PrimitiveFloat`
- `GetNode`
- `Mute / Bypass Repeater (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelPassThrough`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `WanAdvancedI2V`
- `WanAdvancedI2V`
- `WanAdvancedI2V`
- `WanAdvancedI2V`
- `WanAdvancedI2V`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `ImageFlip`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageReelComposit`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ModelPassThrough`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageBatchExtendWithOverlap`
- `Split String`
- `SomethingToString`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `GetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReel`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `easy int`
- `WanAdvancedI2V`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `FL_RIFE`
- `easy showAnything`
- `SaveText|pysssss`
- `llama_cpp_parameters`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `llama_cpp_model_loader`
- `TextInput_`
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

覆盖率 **39%**（139/358）

**有卡**：`VAEDecode`、`easy int`、`Mute / Bypass Relay (rgthree)`、`easy cleanGpuUsed`、`Mute / Bypass Repeater (rgthree)`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`ImageResizeKJv2`、`LoadImage`、`ModelSamplingSD3`、`ModelPassThrough`、`ImageBatchExtendWithOverlap`、`WanAdvancedI2V`、`ImageFlip`、`LayerUtility: ImageReelComposit`、`Split String`、`SomethingToString`、`VHS_VideoCombine`、`PlaySound|pysssss`、`LayerUtility: ImageReel`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`llama_cpp_instruct_adv`、`LoraLoaderModelOnly`、`UNETLoader`、`FL_RIFE`、`SaveText|pysssss`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`TextInput_`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
