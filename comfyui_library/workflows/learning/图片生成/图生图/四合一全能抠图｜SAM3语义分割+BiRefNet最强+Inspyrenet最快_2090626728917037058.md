---
key: 图片生成/图生图/四合一全能抠图｜SAM3语义分割+BiRefNet最强+Inspyrenet最快_2090626728917037058.json
name: 四合一全能抠图｜SAM3语义分割+BiRefNet最强+Inspyrenet最快_2090626728917037058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/四合一全能抠图｜SAM3语义分割+BiRefNet最强+Inspyrenet最快_2090626728917037058.json
hash: aa1938d8ccc83f0e
coverage: 0.906977
learned_at: 2026-10-21 00:51:02
nodes: [ImpactInt, RH_Translator, ThresholdMask, LoadRembgByBiRefNetModel, easy sam3ImageSegmentation, RembgByBiRefNet, InspyrenetRembg, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, Any Switch (rgthree), LayerMask: LoadBiRefNetModelV2, easy sam3ModelLoader, RMBG, LayerMask: BiRefNetUltraV2, Fast Groups Muter (rgthree), LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/四合一全能抠图｜SAM3语义分割+BiRefNet最强+Inspyrenet最快_2090626728917037058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/四合一全能抠图｜SAM3语义分割+BiRefNet最强+Inspyrenet最快_2090626728917037058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `ImpactInt`
- `RH_Translator`
- `ThresholdMask`
- `LoadRembgByBiRefNetModel`
- `easy sam3ImageSegmentation`
- `RembgByBiRefNet`
- `InspyrenetRembg`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `Any Switch (rgthree)`
- `LayerMask: LoadBiRefNetModelV2`
- `easy sam3ModelLoader`
- `RMBG`
- `LayerMask: BiRefNetUltraV2`
- `Fast Groups Muter (rgthree)`
- `LoadImage`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **91%**（39/43）

**有卡**：`ImpactInt`、`RH_Translator`、`ThresholdMask`、`LoadRembgByBiRefNetModel`、`easy sam3ImageSegmentation`、`RembgByBiRefNet`、`InspyrenetRembg`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`LayerMask: LoadBiRefNetModelV2`、`easy sam3ModelLoader`、`RMBG`、`LayerMask: BiRefNetUltraV2`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
