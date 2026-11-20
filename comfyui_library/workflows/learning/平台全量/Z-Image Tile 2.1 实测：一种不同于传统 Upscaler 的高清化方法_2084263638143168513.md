---
key: 平台全量/Z-Image Tile 2.1 实测：一种不同于传统 Upscaler 的高清化方法_2084263638143168513.json
name: Z-Image Tile 2.1 实测：一种不同于传统 Upscaler 的高清化方法_2084263638143168513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Z-Image Tile 2.1 实测：一种不同于传统 Upscaler 的高清化方法_2084263638143168513.json
hash: 9a557907413cb599
coverage: 0.288288
learned_at: 2026-11-14 01:08:05
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, PreviewAny, GetImageSize, ComfyMathExpression, PrimitiveInt, Anything Everywhere, SetNode, GetNode, PrimitiveInt, GetNode, PreviewAny, GetNode, PreviewAny, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, PreviewAny, Note, GetNode, PrimitiveStringMultiline, GetNode, SetNode, PreviewImage, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, SetNode, CLIPTextEncode, BasicGuider, Reroute, RandomNoise, Seed (rgthree), KSamplerSelect, GetNode, VAEEncode, VAEDecode, GetImageSize, ComfyMathExpression, PreviewAny, ComfyMathExpression, ComfyMathExpression, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, Note, Note, GetNode, GetNode, ResizeImageMaskNode, PreviewImage, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SplitImageToTileList, GetNode, GetNode, GetNode, GetNode, ImageScale, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SamplerCustomAdvanced, SetNode, ImageScale, GetNode, GetNode, GetNode, GetNode, GetNode, ZImageFunControlnet, ModelPatchLoader, PrimitiveFloat, PrimitiveInt, PrimitiveInt, BasicScheduler, SplitSigmas, ImageMergeTileList, SaveImage, LoadImage, LoadImage, PreviewImage, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/Z-Image Tile 2.1 实测：一种不同于传统 Upscaler 的高清化方法_2084263638143168513.json

> 来源文件 `comfyui_library/workflows/平台全量/Z-Image Tile 2.1 实测：一种不同于传统 Upscaler 的高清化方法_2084263638143168513.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetImageSize`
- `ComfyMathExpression`
- `PrimitiveInt`
- `Anything Everywhere`
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `PreviewAny`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PreviewAny`
- `Note`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `Reroute`
- `RandomNoise`
- `Seed (rgthree)`
- `KSamplerSelect` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `ComfyMathExpression`
- `PreviewAny`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SplitImageToTileList`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScale`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `ImageScale`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ZImageFunControlnet`
- `ModelPatchLoader`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `BasicScheduler`
- `SplitSigmas`
- `ImageMergeTileList`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `MarkdownNote`

## 知识

覆盖率 **29%**（32/111）

**有卡**：`GetImageSize`、`ComfyMathExpression`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`BasicGuider`、`RandomNoise`、`Seed (rgthree)`、`KSamplerSelect`、`VAEEncode`、`VAEDecode`、`ResizeImageMaskNode`、`SplitImageToTileList`、`ImageScale`、`SamplerCustomAdvanced`、`ZImageFunControlnet`、`ModelPatchLoader`、`BasicScheduler`、`SplitSigmas`、`ImageMergeTileList`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、ZImageFunControlnet、KSamplerSelect
