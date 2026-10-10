---
key: comfyui-workflow-templates-json/image_omnigen2_image_edit.json
name: image_omnigen2_image_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_omnigen2_image_edit.json
hash: 0783a407d8808d35
official: true
coverage: 0.888889
learned_at: 2026-10-10 22:48:22
nodes: [SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, EmptySD3LatentImage, RandomNoise, DualCFGGuider, VAELoader, CLIPLoader, UNETLoader, LoadImage, BasicScheduler, KSamplerSelect, MarkdownNote, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEEncode, CLIPTextEncode, CLIPTextEncode, GetImageSize, MarkdownNote, MarkdownNote, VAEDecode, SaveImage, LoadImage, VAEEncode]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/image_omnigen2_image_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_omnigen2_image_edit.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `EmptySD3LatentImage`
- `RandomNoise`
- `DualCFGGuider`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `MarkdownNote`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `VAEEncode` ★核心

## 知识

覆盖率 **89%**（24/27）

**有卡**：`SamplerCustomAdvanced`、`ReferenceLatent`、`EmptySD3LatentImage`、`RandomNoise`、`DualCFGGuider`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`BasicScheduler`、`KSamplerSelect`、`ImageScaleToTotalPixels`、`VAEEncode`、`CLIPTextEncode`、`GetImageSize`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
