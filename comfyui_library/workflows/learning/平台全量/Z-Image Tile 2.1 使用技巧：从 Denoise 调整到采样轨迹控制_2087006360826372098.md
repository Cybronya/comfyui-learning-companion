---
key: 平台全量/Z-Image Tile 2.1 使用技巧：从 Denoise 调整到采样轨迹控制_2087006360826372098.json
name: Z-Image Tile 2.1 使用技巧：从 Denoise 调整到采样轨迹控制_2087006360826372098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Z-Image Tile 2.1 使用技巧：从 Denoise 调整到采样轨迹控制_2087006360826372098.json
hash: 913e299a44a3f663
coverage: 0.577778
learned_at: 2026-11-14 01:08:05
nodes: [Anything Everywhere, GetNode, PrimitiveStringMultiline, UNETLoader, CLIPLoader, VAELoader, SetNode, BasicGuider, RandomNoise, Seed (rgthree), VAEEncode, ModelPatchLoader, GetNode, GetNode, BasicScheduler, SigmasPreview, SigmasPreview, SigmasPreview, SplitSigmas, SigmasPreview, GetNode, SetNode, LoadImage, PrimitiveFloat, GetNode, ZImageFunControlnet, BasicScheduler, SplitSigmas, CLIPTextEncode, Image Comparer (rgthree), SetNode, BasicScheduler, SetNode, GetNode, GetNode, KSamplerSelect, SamplerCustomAdvanced, SetNode, SetNode, ResizeImageMaskNode, Image Comparer (rgthree), VAEDecode, SaveImage, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/Z-Image Tile 2.1 使用技巧：从 Denoise 调整到采样轨迹控制_2087006360826372098.json

> 来源文件 `comfyui_library/workflows/平台全量/Z-Image Tile 2.1 使用技巧：从 Denoise 调整到采样轨迹控制_2087006360826372098.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Output → Other

**节点**（45 个）：
- `Anything Everywhere`
- `GetNode`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `BasicGuider`
- `RandomNoise`
- `Seed (rgthree)`
- `VAEEncode` ★核心
- `ModelPatchLoader`
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `SigmasPreview`
- `SigmasPreview`
- `SigmasPreview`
- `SplitSigmas`
- `SigmasPreview`
- `GetNode`
- `SetNode`
- `LoadImage`
- `PrimitiveFloat`
- `GetNode`
- `ZImageFunControlnet`
- `BasicScheduler`
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `SetNode`
- `BasicScheduler`
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **58%**（26/45）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`BasicGuider`、`RandomNoise`、`Seed (rgthree)`、`VAEEncode`、`ModelPatchLoader`、`BasicScheduler`、`SigmasPreview`、`SplitSigmas`、`LoadImage`、`ZImageFunControlnet`、`CLIPTextEncode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ResizeImageMaskNode`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、ZImageFunControlnet、KSamplerSelect
