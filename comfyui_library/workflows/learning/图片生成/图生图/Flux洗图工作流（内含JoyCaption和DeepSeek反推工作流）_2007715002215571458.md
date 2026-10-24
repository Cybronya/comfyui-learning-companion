---
key: 图片生成/图生图/Flux洗图工作流（内含JoyCaption和DeepSeek反推工作流）_2007715002215571458.json
name: Flux洗图工作流（内含JoyCaption和DeepSeek反推工作流）_2007715002215571458
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux洗图工作流（内含JoyCaption和DeepSeek反推工作流）_2007715002215571458.json
hash: bf2f2ed136cc5ea5
coverage: 0.777778
learned_at: 2026-10-23 11:02:15
nodes: [DualCLIPLoader, VAEEncode, LoadImage, KSampler, CLIPTextEncodeFlux, CLIPTextEncode, UNETLoader, KSampler, VAELoader, VAEEncode, Joy_caption_two, Joy_caption_two_load, PreviewImage, ShowText|pysssss, SaveImage, Image Comparer (rgthree), JWImageResizeByLongerSide, VAEDecode, SaveImage, Image Comparer (rgthree), VAEDecode, LatentUpscaleBy, ShowText|pysssss, Joy_caption_two, ShowText|pysssss, Translate, LoadImage, Joy_caption_two_load, JanusModelLoader, ShowText|pysssss, Translate, JanusImageUnderstanding, ShowText|pysssss, Save Text File, LoadImage, SaveText|pysssss]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.3500000000000001, "sampler_name": "euler", "scheduler": "normal", "seed": 51492426235954, "steps": 20}
---

# 图片生成/图生图/Flux洗图工作流（内含JoyCaption和DeepSeek反推工作流）_2007715002215571458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux洗图工作流（内含JoyCaption和DeepSeek反推工作流）_2007715002215571458.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `DualCLIPLoader`
- `VAEEncode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `Joy_caption_two`
- `Joy_caption_two_load`
- `PreviewImage`
- `ShowText|pysssss`
- `SaveImage`
- `Image Comparer (rgthree)`
- `JWImageResizeByLongerSide`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LatentUpscaleBy`
- `ShowText|pysssss`
- `Joy_caption_two`
- `ShowText|pysssss`
- `Translate`
- `LoadImage`
- `Joy_caption_two_load`
- `JanusModelLoader`
- `ShowText|pysssss`
- `Translate`
- `JanusImageUnderstanding`
- `ShowText|pysssss`
- `Save Text File`
- `LoadImage`
- `SaveText|pysssss`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `51492426235954`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.3500000000000001`

## 知识

覆盖率 **78%**（28/36）

**有卡**：`DualCLIPLoader`、`VAEEncode`、`LoadImage`、`KSampler`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`Joy_caption_two`、`Joy_caption_two_load`、`SaveImage`、`JWImageResizeByLongerSide`、`VAEDecode`、`LatentUpscaleBy`、`Translate`、`JanusModelLoader`、`JanusImageUnderstanding`、`Save Text File`、`SaveText|pysssss`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、CLIPTextEncodeFlux、LatentUpscaleBy
