---
key: 平台全量/[Z-Image Series 03] Controlnet Tile 与 eta_2091879249308381185.json
name: [Z-Image Series 03] Controlnet Tile 与 eta_2091879249308381185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/[Z-Image Series 03] Controlnet Tile 与 eta_2091879249308381185.json
hash: 60fd1bb2e5932ca3
coverage: 0.466667
learned_at: 2026-11-14 01:08:52
nodes: [SetNode, GetNode, SetNode, ModelPatchLoader, SetNode, UNETLoader, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, GetNode, SetNode, CLIPLoader, SetNode, SetNode, SetNode, SetNode, SetNode, ResizeImageMaskNode, GetNode, GetNode, EmptyLatentImage, PreviewImage, SetNode, VAEEncodeTiled, ResizeImageMaskNode, ZImageFunControlnet, Seed (rgthree), SetNode, GetNode, GetNode, BasicGuider, RandomNoise, GetNode, SamplerCustomAdvanced, VAEDecodeTiled, GetNode, SplitSigmas, BasicScheduler, GetNode, GetNode, GetNode, GetNode, BasicGuider, RandomNoise, GetNode, SamplerCustomAdvanced, VAEDecodeTiled, GetNode, SplitSigmas, BasicScheduler, GetNode, GetNode, Image Comparer (rgthree), ImageBlur, Image Comparer (rgthree), Image Comparer (rgthree), SamplerEulerAncestral, LoadImage, LoadImage, SamplerCustomAdvanced, RandomNoise, GetNode, BasicGuider, GetNode, GetNode, GetNode, GetNode, VAEEncodeTiled, SetNode, ZImageFunControlnet, UNETLoader, GetNode, SetNode, ModelPatchLoader, GetNode, Image Comparer (rgthree), SplitSigmas, KSamplerSelect, ResolutionSelector, PrimitiveFloat, VAELoader, Anything Everywhere, PreviewImage, PreviewImage, SamplerEulerAncestral, BasicScheduler, MarkdownNote, SaveImage, VAEDecodeTiled]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 512, "width": 512}
---

# 平台全量/[Z-Image Series 03] Controlnet Tile 与 eta_2091879249308381185.json

> 来源文件 `comfyui_library/workflows/平台全量/[Z-Image Series 03] Controlnet Tile 与 eta_2091879249308381185.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
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
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `Seed (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `RandomNoise`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SplitSigmas`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `RandomNoise`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SplitSigmas`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageBlur`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SamplerEulerAncestral` ★核心
- `LoadImage`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `GetNode`
- `BasicGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncodeTiled` ★核心
- `SetNode`
- `ZImageFunControlnet`
- `UNETLoader` ★核心
- `GetNode`
- `SetNode`
- `ModelPatchLoader`
- `GetNode`
- `Image Comparer (rgthree)`
- `SplitSigmas`
- `KSamplerSelect` ★核心
- `ResolutionSelector`
- `PrimitiveFloat`
- `VAELoader`
- `Anything Everywhere`
- `PreviewImage`
- `PreviewImage`
- `SamplerEulerAncestral` ★核心
- `BasicScheduler`
- `MarkdownNote`
- `SaveImage`
- `VAEDecodeTiled` ★核心

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **47%**（42/90）

**有卡**：`ModelPatchLoader`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`ResizeImageMaskNode`、`EmptyLatentImage`、`VAEEncodeTiled`、`ZImageFunControlnet`、`Seed (rgthree)`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`SplitSigmas`、`BasicScheduler`、`ImageBlur`、`SamplerEulerAncestral`、`LoadImage`、`KSamplerSelect`、`ResolutionSelector`、`VAELoader`、`SaveImage`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage、ResolutionSelector、LoadImage、UNETLoader、ZImageFunControlnet
