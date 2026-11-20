---
key: 平台全量/Kontext一句话换装lora调试版本2.0_1959508870999781377.json
name: Kontext一句话换装lora调试版本2.0_1959508870999781377
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext一句话换装lora调试版本2.0_1959508870999781377.json
hash: 9bb13adbf66c87c1
coverage: 0.826923
learned_at: 2026-11-14 00:35:09
nodes: [FluxGuidance, ReferenceLatent, ConditioningZeroOut, GetImageSize+, KSampler, CR SDXL Aspect Ratio, Image Comparer (rgthree), CLIPTextEncode, FluxKontextImageScale, ConditioningZeroOut, FluxGuidance, ReferenceLatent, LoraLoaderModelOnly, KSampler, ImageResizeKJv2, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, DualCLIPLoader, VAELoader, VAEEncode, Text Concatenate, CR Text, Text Concatenate, ShowText|pysssss, CR Text, CR Text, SaveImage, VAEDecode, ShowText|pysssss, CLIPTextEncode, CR Text, CR Latent Input Switch, ImageConcatMulti, VAEDecode, ShowText|pysssss, CR Text Blacklist, ShowText|pysssss, ShowText|pysssss, CR Text Blacklist, VAEEncode, PreviewImage, FluxKontextImageScale, Joy_caption_two, Joy_caption_two_load, PreviewImage, LoadImage, LoadImage, ShowText|pysssss, CR Text, Text Concatenate, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 56304425751608, "steps": 20}
---

# 平台全量/Kontext一句话换装lora调试版本2.0_1959508870999781377.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext一句话换装lora调试版本2.0_1959508870999781377.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `FluxGuidance`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `GetImageSize+`
- `KSampler` ★核心
- `CR SDXL Aspect Ratio`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `FluxKontextImageScale`
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `Text Concatenate`
- `CR Text`
- `Text Concatenate`
- `ShowText|pysssss`
- `CR Text`
- `CR Text`
- `SaveImage`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `CR Text`
- `CR Latent Input Switch`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `CR Text Blacklist`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `CR Text Blacklist`
- `VAEEncode` ★核心
- `PreviewImage`
- `FluxKontextImageScale`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `ShowText|pysssss`
- `CR Text`
- `Text Concatenate`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `56304425751608`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（43/52）

**有卡**：`FluxGuidance`、`ReferenceLatent`、`ConditioningZeroOut`、`GetImageSize+`、`KSampler`、`CR SDXL Aspect Ratio`、`CLIPTextEncode`、`FluxKontextImageScale`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`VAEEncode`、`Text Concatenate`、`CR Text`、`SaveImage`、`VAEDecode`、`CR Latent Input Switch`、`ImageConcatMulti`、`CR Text Blacklist`、`Joy_caption_two`、`Joy_caption_two_load`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
