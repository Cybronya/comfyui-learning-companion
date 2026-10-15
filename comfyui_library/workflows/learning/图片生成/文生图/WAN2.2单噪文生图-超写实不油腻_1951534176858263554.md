---
key: 图片生成/文生图/WAN2.2单噪文生图-超写实不油腻_1951534176858263554.json
name: WAN2.2单噪文生图-超写实不油腻_1951534176858263554
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.2单噪文生图-超写实不油腻_1951534176858263554.json
hash: a547252b95299939
coverage: 0.833333
learned_at: 2026-10-15 22:27:34
nodes: [PathchSageAttentionKJ, UnetLoaderGGUF, Lora Loader Stack (rgthree), SaveImage, ModelSamplingSD3, VAELoader, FastLaplacianSharpen, FastFilmGrain, easy cleanGpuUsed, easy clearCacheAll, WanVideoNAG, VAEDecode, CLIPTextEncode, PreviewImage, MarkdownNote, Label (rgthree), KSampler, MarkdownNote, MarkdownNote, Label (rgthree), CLIPLoader, CLIPTextEncode, Note Plus (mtb), EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 0.8, "denoise": 0.8500000000000002, "height": 1088, "sampler_name": "euler", "scheduler": "bong_tangent", "seed": 994727085451482, "steps": 10, "width": 1920}
---

# 图片生成/文生图/WAN2.2单噪文生图-超写实不油腻_1951534176858263554.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN2.2单噪文生图-超写实不油腻_1951534176858263554.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `Lora Loader Stack (rgthree)`
- `SaveImage`
- `ModelSamplingSD3`
- `VAELoader`
- `FastLaplacianSharpen`
- `FastFilmGrain`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `WanVideoNAG`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `MarkdownNote`
- `Label (rgthree)`
- `KSampler` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note Plus (mtb)`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `994727085451482`
- `steps` = `10`
- `cfg` = `0.8`
- `sampler_name` = `euler`
- `scheduler` = `bong_tangent`
- `denoise` = `0.8500000000000002`
- `width` = `1920`
- `height` = `1088`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`Lora Loader Stack (rgthree)`、`SaveImage`、`ModelSamplingSD3`、`VAELoader`、`FastLaplacianSharpen`、`FastFilmGrain`、`easy cleanGpuUsed`、`easy clearCacheAll`、`WanVideoNAG`、`VAEDecode`、`CLIPTextEncode`、`Label (rgthree)`、`KSampler`、`CLIPLoader`、`Note Plus (mtb)`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、Lora Loader Stack (rgthree)、SaveImage
