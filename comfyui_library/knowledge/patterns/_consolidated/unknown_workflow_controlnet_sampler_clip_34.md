---
name: unknown_workflow_controlnet_sampler_clip_34
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.406667
common_nodes: [Anything Everywhere, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, GetNode, Image Comparer (rgthree), KSamplerSelect, LoadImage, ModelPatchLoader, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, SplitSigmas, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet]
problems: []
missing: []
members: [平台全量/Z-Image Tile 2.1 使用技巧：从 Denoise 调整到采样轨迹控制_2087006360826372098.json, 平台全量/Z-Image Tile 2.1 实测：一种不同于传统 Upscaler 的高清化方法_2084263638143168513.json, 平台全量/Z-Image-Turbo 模型（ ComfyUI 原生节点分块放大流 ）_2066027264583753729.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Z-Image Tile 2.1 使用技巧：从 Denoise 调整到采样轨迹控制_2087006360826372098.json、平台全量/Z-Image Tile 2.1 实测：一种不同于传统 Upscaler 的高清化方法_2084263638143168513.json、平台全量/Z-Image-Turbo 模型（ ComfyUI 原生节点分块放大流 ）_2066027264583753729.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：41%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `ModelPatchLoader`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ImageMergeTileList` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `SplitImageToTileList` —— 2/3 个有
- `ColorMatchV2` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `SigmasPreview` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
