---
key: 平台全量/Beautiful and Exquisite Rock Painting Mural Style_1888771444896161794.json
name: Beautiful and Exquisite Rock Painting Mural Style_1888771444896161794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Beautiful and Exquisite Rock Painting Mural Style_1888771444896161794.json
hash: ff41f140c5a27795
coverage: 0.888889
learned_at: 2026-11-14 00:19:44
nodes: [CR Integer To String, Seed, EmptyLatentImage, FluxSamplerParams+, Primitive float [Crystools], UnetLoaderGGUF, CLIPTextEncode, DualCLIPLoaderGGUF, VAELoader, UpscaleModelLoader, ImageUpscaleWithModel, SaveImage, VAEDecode, PreviewImage, Image Comparer (rgthree), Text Multiline, LoraLoaderModelOnly, TeaCache]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 768}
---

# 平台全量/Beautiful and Exquisite Rock Painting Mural Style_1888771444896161794.json

> 来源文件 `comfyui_library/workflows/平台全量/Beautiful and Exquisite Rock Painting Mural Style_1888771444896161794.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CR Integer To String`
- `Seed`
- `EmptyLatentImage` ★核心
- `FluxSamplerParams+` ★核心
- `Primitive float [Crystools]`
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoaderGGUF`
- `VAELoader`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `TeaCache`

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`CR Integer To String`、`Seed`、`EmptyLatentImage`、`FluxSamplerParams+`、`Primitive float [Crystools]`、`UnetLoaderGGUF`、`CLIPTextEncode`、`DualCLIPLoaderGGUF`、`VAELoader`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`SaveImage`、`VAEDecode`、`Text Multiline`、`LoraLoaderModelOnly`、`TeaCache`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、FluxSamplerParams+、Seed、ImageUpscaleWithModel
