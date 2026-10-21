---
key: 图片生成/文生图/Krea_2_深度探索_从控制结果，到控制过程_Controlling_the_Generati_2080936885467312130.json
name: Krea_2_深度探索_从控制结果，到控制过程_Controlling_the_Generati_2080936885467312130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea_2_深度探索_从控制结果，到控制过程_Controlling_the_Generati_2080936885467312130.json
hash: 5d8e290d50dd1d61
coverage: 0.444444
learned_at: 2026-10-20 00:39:23
nodes: [EmptyLatentImage, SetNode, SetNode, SetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, ClownOptions_ExtraOptions_Beta, ClownOptions_ExtraOptions_Beta, VAEDecode, GetNode, VAEEncode, SetNode, GetNode, GetNode, GetNode, VAEDecode, VAEDecode, ImageStitch, ClownsharKSampler_Beta, SharkOptions_Beta, UNETLoader, ResolutionSelector, PrimitiveFloat, SetNode, SetNode, CLIPTextEncode, ClownsharKSampler_Beta, GetNode, SetNode, UNETLoader, ClownsharkChainsampler_Beta, GetNode, GetNode, GetNode, VAEDecode, SetNode, SetNode, Seed (rgthree), ResizeImageMaskNode, LoraLoaderModelOnly, Anything Everywhere, Anything Everywhere, Anything Everywhere, VAELoader, SetNode, ClownsharKSampler_Beta, SetNode, MarkdownNote, SaveImage, Image Comparer (rgthree), PreviewImage, Image Comparer (rgthree), CLIPLoader, SetNode, easy promptLine, SigmasPreview, BasicScheduler, PreviewImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 2, "denoise": 1, "height": 512, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent", "width": 512}
---

# 图片生成/文生图/Krea_2_深度探索_从控制结果，到控制过程_Controlling_the_Generati_2080936885467312130.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea_2_深度探索_从控制结果，到控制过程_Controlling_the_Generati_2080936885467312130.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `EmptyLatentImage` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ClownOptions_ExtraOptions_Beta`
- `ClownOptions_ExtraOptions_Beta`
- `VAEDecode` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `ClownsharKSampler_Beta` ★核心
- `SharkOptions_Beta`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `ClownsharKSampler_Beta` ★核心
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `ClownsharkChainsampler_Beta` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `Seed (rgthree)`
- `ResizeImageMaskNode`
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `VAELoader`
- `SetNode`
- `ClownsharKSampler_Beta` ★核心
- `SetNode`
- `MarkdownNote`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `SetNode`
- `easy promptLine`
- `SigmasPreview`
- `BasicScheduler`
- `PreviewImage`
- `PreviewImage`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `2`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **44%**（28/63）

**有卡**：`EmptyLatentImage`、`CLIPTextEncode`、`ClownOptions_ExtraOptions_Beta`、`VAEDecode`、`VAEEncode`、`ImageStitch`、`ClownsharKSampler_Beta`、`SharkOptions_Beta`、`UNETLoader`、`ResolutionSelector`、`ClownsharkChainsampler_Beta`、`Seed (rgthree)`、`ResizeImageMaskNode`、`LoraLoaderModelOnly`、`VAELoader`、`SaveImage`、`CLIPLoader`、`easy promptLine`、`SigmasPreview`、`BasicScheduler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
