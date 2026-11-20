---
key: 平台全量/H3+PikaFlex_Wallpaper_Loop_动态壁纸_2117863969422667777.json
name: H3+PikaFlex_Wallpaper_Loop_动态壁纸_2117863969422667777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/H3+PikaFlex_Wallpaper_Loop_动态壁纸_2117863969422667777.json
hash: 3371f71a2c04c95e
coverage: 0.884615
learned_at: 2026-11-14 00:31:12
nodes: [UNETLoader, MiniMaxH3Loop, CLIPLoader, VAELoader, VAELoader, LoadImage, PrimitiveStringMultiline, MiniMaxH3ReferenceToVideo, RandomNoise, KSamplerSelect, ManualSigmas, BasicGuider, SamplerCustomAdvanced, MiniMaxH3LoopDecode, CreateVideo, SaveVideo, LoopInterpolate, ImageResizeKJv2, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, GetImageSizeAndCount, ImageResizeKJv2, ResolutionSelector, PrimitiveFloat, ComfyMathExpression]
patterns: []
missing: []
---

# 平台全量/H3+PikaFlex_Wallpaper_Loop_动态壁纸_2117863969422667777.json

> 来源文件 `comfyui_library/workflows/平台全量/H3+PikaFlex_Wallpaper_Loop_动态壁纸_2117863969422667777.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `MiniMaxH3Loop`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LoopDecode`
- `CreateVideo`
- `SaveVideo`
- `LoopInterpolate`
- `ImageResizeKJv2`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `ResolutionSelector`
- `PrimitiveFloat`
- `ComfyMathExpression`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`UNETLoader`、`MiniMaxH3Loop`、`CLIPLoader`、`VAELoader`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3LoopDecode`、`CreateVideo`、`SaveVideo`、`LoopInterpolate`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`GetImageSizeAndCount`、`ResolutionSelector`、`ComfyMathExpression`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
