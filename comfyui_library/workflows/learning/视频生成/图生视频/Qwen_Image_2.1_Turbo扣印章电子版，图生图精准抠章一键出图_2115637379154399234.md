---
key: 视频生成/图生视频/Qwen_Image_2.1_Turbo扣印章电子版，图生图精准抠章一键出图_2115637379154399234.json
name: Qwen_Image_2.1_Turbo扣印章电子版，图生图精准抠章一键出图_2115637379154399234
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_Turbo扣印章电子版，图生图精准抠章一键出图_2115637379154399234.json
hash: ba7c98ef2f849bf3
coverage: 0.933333
learned_at: 2026-10-30 17:58:34
nodes: [BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, SamplerCustom, ManualSigmas, FluxKontextImageScale, SaveImage, VAEDecode, SaveImageAdvanced, UNETLoader, CLIPLoader, VAELoader, LoadImage, KSamplerSelect, TextEncodeQwenImage21, easy showAnything, easy promptConcat, CR Text, CR Text, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1_Turbo扣印章电子版，图生图精准抠章一键出图_2115637379154399234.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_Turbo扣印章电子版，图生图精准抠章一键出图_2115637379154399234.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `SamplerCustom` ★核心
- `ManualSigmas`
- `FluxKontextImageScale`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `KSamplerSelect` ★核心
- `TextEncodeQwenImage21`
- `easy showAnything`
- `easy promptConcat`
- `CR Text`
- `CR Text`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **93%**（42/45）

**有卡**：`BRIA_RMBG_ModelLoader_Zho`、`BRIA_RMBG_Zho`、`SamplerCustom`、`ManualSigmas`、`FluxKontextImageScale`、`SaveImage`、`VAEDecode`、`SaveImageAdvanced`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`KSamplerSelect`、`TextEncodeQwenImage21`、`easy promptConcat`、`CR Text`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
