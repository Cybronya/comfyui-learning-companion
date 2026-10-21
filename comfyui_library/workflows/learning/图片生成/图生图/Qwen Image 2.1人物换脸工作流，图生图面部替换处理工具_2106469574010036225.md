---
key: 图片生成/图生图/Qwen Image 2.1人物换脸工作流，图生图面部替换处理工具_2106469574010036225.json
name: Qwen Image 2.1人物换脸工作流，图生图面部替换处理工具_2106469574010036225
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1人物换脸工作流，图生图面部替换处理工具_2106469574010036225.json
hash: d85dbfc1b4a4c53e
coverage: 0.864407
learned_at: 2026-10-21 00:42:19
nodes: [VAELoader, QwenImage21Cache, CLIPLoader, SaveImage, TextEncodeQwenImage21, LoadImage, Reroute, GrowMaskWithBlur, LayerUtility: CropByMask V2, GrowMaskWithBlur, LayerUtility: RestoreCropBox, ComfySwitchNode, QwenPERewriteT8, easy cleanGpuUsed, ColorMatch, LayerUtility: ImageScaleRestore V2, EmptyLatentImage, VAEDecode, LoadImage, KSampler, CR Prompt Text, Image Comparer (rgthree), SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, UNETLoader, QwenImage21SpectrumT8, easy showAnything, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1人物换脸工作流，图生图面部替换处理工具_2106469574010036225.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1人物换脸工作流，图生图面部替换处理工具_2106469574010036225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `VAELoader`
- `QwenImage21Cache`
- `CLIPLoader`
- `SaveImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `Reroute`
- `GrowMaskWithBlur`
- `LayerUtility: CropByMask V2`
- `GrowMaskWithBlur`
- `LayerUtility: RestoreCropBox`
- `ComfySwitchNode`
- `QwenPERewriteT8`
- `easy cleanGpuUsed`
- `ColorMatch`
- `LayerUtility: ImageScaleRestore V2`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `CR Prompt Text`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `easy showAnything`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（51/59）

**有卡**：`VAELoader`、`QwenImage21Cache`、`CLIPLoader`、`SaveImage`、`TextEncodeQwenImage21`、`LoadImage`、`GrowMaskWithBlur`、`LayerUtility: CropByMask V2`、`LayerUtility: RestoreCropBox`、`QwenPERewriteT8`、`easy cleanGpuUsed`、`ColorMatch`、`LayerUtility: ImageScaleRestore V2`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`UNETLoader`、`QwenImage21SpectrumT8`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
