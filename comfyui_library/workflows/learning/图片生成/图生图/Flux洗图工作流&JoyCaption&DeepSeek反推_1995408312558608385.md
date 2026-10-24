---
key: 图片生成/图生图/Flux洗图工作流&JoyCaption&DeepSeek反推_1995408312558608385.json
name: Flux洗图工作流&JoyCaption&DeepSeek反推_1995408312558608385
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux洗图工作流&JoyCaption&DeepSeek反推_1995408312558608385.json
hash: 137a2481a0f45cc4
coverage: 0.736842
learned_at: 2026-10-23 11:02:14
nodes: [VAEEncode, CLIPTextEncode, KSampler, Joy_caption_two_load, ShowText|pysssss, VAEDecode, SaveImage, Image Comparer (rgthree), ShowText|pysssss, Joy_caption_two, ShowText|pysssss, Translate, LoadImage, Joy_caption_two_load, JanusModelLoader, ShowText|pysssss, Translate, JanusImageUnderstanding, ShowText|pysssss, Save Text File, LoadImage, SaveText|pysssss, JWImageResizeByLongerSide, VAELoader, DualCLIPLoader, Joy_caption_two, VAEDecode, CLIPTextEncodeFlux, LatentUpscaleBy, VAEEncode, UNETLoader, Image Comparer (rgthree), PreviewImage, SaveImage, Note, KSampler, Note, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.7000000000000002, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 886931616088451, "steps": 30}
---

# 图片生成/图生图/Flux洗图工作流&JoyCaption&DeepSeek反推_1995408312558608385.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux洗图工作流&JoyCaption&DeepSeek反推_1995408312558608385.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `Joy_caption_two_load`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
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
- `JWImageResizeByLongerSide`
- `VAELoader`
- `DualCLIPLoader`
- `Joy_caption_two`
- `VAEDecode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `LatentUpscaleBy`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SaveImage`
- `Note`
- `KSampler` ★核心
- `Note`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `886931616088451`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.7000000000000002`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`VAEEncode`、`CLIPTextEncode`、`KSampler`、`Joy_caption_two_load`、`VAEDecode`、`SaveImage`、`Joy_caption_two`、`Translate`、`LoadImage`、`JanusModelLoader`、`JanusImageUnderstanding`、`Save Text File`、`SaveText|pysssss`、`JWImageResizeByLongerSide`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncodeFlux`、`LatentUpscaleBy`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、CLIPTextEncodeFlux、LatentUpscaleBy
