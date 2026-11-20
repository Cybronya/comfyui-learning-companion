---
key: 平台全量/Flux.2 Klein 9B-KV Tile Upscale：无需 ControlNet 的任意尺_2066503754844823553.json
name: Flux.2 Klein 9B-KV Tile Upscale：无需 ControlNet 的任意尺_2066503754844823553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2 Klein 9B-KV Tile Upscale：无需 ControlNet 的任意尺_2066503754844823553.json
hash: b6bc0a96eb9e9e01
coverage: 0.336735
learned_at: 2026-11-14 00:28:51
nodes: [Flux2Scheduler, ConditioningZeroOut, EmptyFlux2LatentImage, ReferenceLatent, Reroute, VAEEncode, FluxKVCache, SamplerCustom, SetNode, GetImageSize, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, ImageScale, PreviewAny, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, PreviewAny, LoraLoaderModelOnly, GetNode, SetNode, SetNode, ImageScaleToTotalPixels, GetImageSize, SetNode, GetNode, SetNode, GetNode, SetNode, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, SplitImageToTileList, Note, GetImageSize, ComfyMathExpression, SetNode, PrimitiveInt, PrimitiveInt, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, ImageScale, ComfyMathExpression, LoadImage, LoadImage, Image Comparer (rgthree), PreviewAny, PreviewAny, PreviewAny, ComfyMathExpression, SetNode, ComfyMathExpression, SetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, PreviewImage, ColorMatchV2, PrimitiveFloat, UNETLoader, CLIPLoader, VAELoader, Anything Everywhere3, MarkdownNote, ImageMergeTileList, SaveImage]
patterns: []
missing: []
---

# 平台全量/Flux.2 Klein 9B-KV Tile Upscale：无需 ControlNet 的任意尺_2066503754844823553.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2 Klein 9B-KV Tile Upscale：无需 ControlNet 的任意尺_2066503754844823553.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（98 个）：
- `Flux2Scheduler`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `Reroute`
- `VAEEncode` ★核心
- `FluxKVCache`
- `SamplerCustom` ★核心
- `SetNode`
- `GetImageSize`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageScale`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `PreviewAny`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `SplitImageToTileList`
- `Note`
- `GetImageSize`
- `ComfyMathExpression`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageScale`
- `ComfyMathExpression`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `ComfyMathExpression`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ColorMatchV2`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `MarkdownNote`
- `ImageMergeTileList`
- `SaveImage`

## 知识

覆盖率 **34%**（33/98）

**有卡**：`Flux2Scheduler`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`ReferenceLatent`、`VAEEncode`、`FluxKVCache`、`SamplerCustom`、`GetImageSize`、`ComfyMathExpression`、`VAEDecode`、`ImageScale`、`KSamplerSelect`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`SplitImageToTileList`、`LoadImage`、`CLIPTextEncode`、`ColorMatchV2`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageMergeTileList`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
