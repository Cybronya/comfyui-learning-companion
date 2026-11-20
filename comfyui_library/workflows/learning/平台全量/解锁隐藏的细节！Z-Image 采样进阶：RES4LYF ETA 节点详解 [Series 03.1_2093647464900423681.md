---
key: 平台全量/解锁隐藏的细节！Z-Image 采样进阶：RES4LYF ETA 节点详解 [Series 03.1_2093647464900423681.json
name: 解锁隐藏的细节！Z-Image 采样进阶：RES4LYF ETA 节点详解 [Series 03.1_2093647464900423681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/解锁隐藏的细节！Z-Image 采样进阶：RES4LYF ETA 节点详解 [Series 03.1_2093647464900423681.json
hash: e7a7b6942cfece42
coverage: 0.410256
learned_at: 2026-11-14 02:44:08
nodes: [SetNode, GetNode, SetNode, ModelPatchLoader, SetNode, UNETLoader, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, PrimitiveStringMultiline, SetNode, CLIPLoader, SetNode, CLIPTextEncode, GetNode, SetNode, SetNode, SetNode, TextBoxConcatenate, Anything Everywhere, GetNode, GetNode, SetNode, SetNode, ResizeImageMaskNode, GetNode, GetNode, EmptyLatentImage, PreviewImage, SetNode, VAEEncodeTiled, ResizeImageMaskNode, ZImageFunControlnet, VAELoader, Seed (rgthree), SetNode, ImageBlur, LoadImage, LoadImage, VAEEncodeTiled, SetNode, ZImageFunControlnet, UNETLoader, GetNode, SetNode, ModelPatchLoader, GetNode, PrimitiveInt, GetNode, VAEDecode, GetNode, VAEDecode, GetNode, GetNode, ClownsharKSampler_Beta, ClownsharKSampler_Beta, ResolutionSelector, GetNode, GetNode, PrimitiveFloat, SharkOptions_Beta, ClownOptions_SDE_Beta, easy promptLine, Image Comparer (rgthree), SetNode, VAEDecodeTiled, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PreviewImage, PreviewImage, VAEDecodeTiled, SaveImage, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 6, "denoise": 1, "height": 512, "sampler_name": -1, "scheduler": 1, "seed": 3.4, "steps": "beta57", "width": 512}
---

# 平台全量/解锁隐藏的细节！Z-Image 采样进阶：RES4LYF ETA 节点详解 [Series 03.1_2093647464900423681.json

> 来源文件 `comfyui_library/workflows/平台全量/解锁隐藏的细节！Z-Image 采样进阶：RES4LYF ETA 节点详解 [Series 03.1_2093647464900423681.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `ModelPatchLoader`
- `SetNode`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `TextBoxConcatenate`
- `Anything Everywhere`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `SetNode`
- `VAEEncodeTiled` ★核心
- `ResizeImageMaskNode`
- `ZImageFunControlnet`
- `VAELoader`
- `Seed (rgthree)`
- `SetNode`
- `ImageBlur`
- `LoadImage`
- `LoadImage`
- `VAEEncodeTiled` ★核心
- `SetNode`
- `ZImageFunControlnet`
- `UNETLoader` ★核心
- `GetNode`
- `SetNode`
- `ModelPatchLoader`
- `GetNode`
- `PrimitiveInt`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ClownsharKSampler_Beta` ★核心
- `ClownsharKSampler_Beta` ★核心
- `ResolutionSelector`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `SharkOptions_Beta`
- `ClownOptions_SDE_Beta`
- `easy promptLine`
- `Image Comparer (rgthree)`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `MarkdownNote`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `3.4`
- `steps` = `beta57`
- `cfg` = `6`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **41%**（32/78）

**有卡**：`ModelPatchLoader`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`TextBoxConcatenate`、`ResizeImageMaskNode`、`EmptyLatentImage`、`VAEEncodeTiled`、`ZImageFunControlnet`、`VAELoader`、`Seed (rgthree)`、`ImageBlur`、`LoadImage`、`VAEDecode`、`ClownsharKSampler_Beta`、`ResolutionSelector`、`SharkOptions_Beta`、`ClownOptions_SDE_Beta`、`easy promptLine`、`VAEDecodeTiled`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage、ResolutionSelector、LoadImage、UNETLoader
