---
key: 图片生成/图生图/Costume Changes and Face Swaps Flux3_klein 图像编辑_2113428085260513281.json
name: Costume Changes and Face Swaps Flux3_klein 图像编辑_2113428085260513281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Costume Changes and Face Swaps Flux3_klein 图像编辑_2113428085260513281.json
hash: bf385560ddbf605d
coverage: 0.875
learned_at: 2026-10-26 22:01:25
nodes: [KSampler, VAEDecode, ReferenceMultiLatent, MarkdownNote, CLIPTextEncode, Image Comparer (rgthree), TextGenerate, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, SaveImage, LoadImage, CLIPTextEncode, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "bong_tangent", "seed": 73654105373752, "steps": 25}
---

# 图片生成/图生图/Costume Changes and Face Swaps Flux3_klein 图像编辑_2113428085260513281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Costume Changes and Face Swaps Flux3_klein 图像编辑_2113428085260513281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ReferenceMultiLatent`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `TextGenerate`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `73654105373752`
- `steps` = `25`
- `cfg` = `3.5`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`KSampler`、`VAEDecode`、`ReferenceMultiLatent`、`CLIPTextEncode`、`TextGenerate`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`LoadImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ReferenceMultiLatent
