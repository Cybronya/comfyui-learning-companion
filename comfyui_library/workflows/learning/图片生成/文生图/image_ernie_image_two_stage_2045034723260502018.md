---
key: 图片生成/文生图/image_ernie_image_two_stage_2045034723260502018.json
name: image_ernie_image_two_stage_2045034723260502018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/image_ernie_image_two_stage_2045034723260502018.json
hash: f3a566c002609f54
coverage: 0.703704
learned_at: 2026-10-21 02:57:10
nodes: [SaveImage, MarkdownNote, MarkdownNote, EmptyFlux2LatentImage, VAEDecode, CLIPTextEncode, CLIPTextEncode, StringReplace, PrimitiveStringMultiline, TextGenerate, PrimitiveBoolean, ComfySwitchNode, StringReplace, StringReplace, PreviewAny, PreviewAny, INTConstant, PreviewAny, INTConstant, PreviewAny, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, CLIPLoader, VAELoader, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/image_ernie_image_two_stage_2045034723260502018.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/image_ernie_image_two_stage_2045034723260502018.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `StringReplace`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `StringReplace`
- `StringReplace`
- `PreviewAny`
- `PreviewAny`
- `INTConstant`
- `PreviewAny`
- `INTConstant`
- `PreviewAny`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **70%**（19/27）

**有卡**：`SaveImage`、`EmptyFlux2LatentImage`、`VAEDecode`、`CLIPTextEncode`、`StringReplace`、`TextGenerate`、`PrimitiveBoolean`、`INTConstant`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、KSamplerAdvanced、EmptyFlux2LatentImage、SaveImage
