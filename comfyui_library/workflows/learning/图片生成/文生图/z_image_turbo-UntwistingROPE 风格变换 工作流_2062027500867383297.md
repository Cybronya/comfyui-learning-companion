---
key: 图片生成/文生图/z_image_turbo-UntwistingROPE 风格变换 工作流_2062027500867383297.json
name: z_image_turbo-UntwistingROPE 风格变换 工作流_2062027500867383297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z_image_turbo-UntwistingROPE 风格变换 工作流_2062027500867383297.json
hash: ecd6fd9f2014972c
coverage: 0.7
learned_at: 2026-10-19 23:03:29
nodes: [CFGGuider, Note, KSamplerSelect, SamplerCustomAdvanced, BasicScheduler, ImageScaleToTotalPixels, VAEEncode, UNETLoader, GetImageSize, SetNode, PreviewImage, GetNode, VAEDecode, EmptySD3LatentImage, RandomNoise, SaveImage, VAELoader, CLIPLoader, ImageResizeKJv2, Note, Note, RFInversion, Note, Note, CLIPTextEncode, CLIPTextEncode, UntwistingRoPE, Note, UnofficialExtensions, LoadImage]
patterns: []
missing: []
---

# 图片生成/文生图/z_image_turbo-UntwistingROPE 风格变换 工作流_2062027500867383297.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z_image_turbo-UntwistingROPE 风格变换 工作流_2062027500867383297.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CFGGuider`
- `Note`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `GetImageSize`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `RandomNoise`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `ImageResizeKJv2`
- `Note`
- `Note`
- `RFInversion`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UntwistingRoPE`
- `Note`
- `UnofficialExtensions`
- `LoadImage`

## 知识

覆盖率 **70%**（21/30）

**有卡**：`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicScheduler`、`ImageScaleToTotalPixels`、`VAEEncode`、`UNETLoader`、`GetImageSize`、`VAEDecode`、`EmptySD3LatentImage`、`RandomNoise`、`SaveImage`、`VAELoader`、`CLIPLoader`、`ImageResizeKJv2`、`RFInversion`、`CLIPTextEncode`、`UntwistingRoPE`、`UnofficialExtensions`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
