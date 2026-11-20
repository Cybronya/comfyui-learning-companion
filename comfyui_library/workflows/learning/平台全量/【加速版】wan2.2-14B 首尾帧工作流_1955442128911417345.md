---
key: 平台全量/【加速版】wan2.2-14B 首尾帧工作流_1955442128911417345.json
name: 【加速版】wan2.2-14B 首尾帧工作流_1955442128911417345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【加速版】wan2.2-14B 首尾帧工作流_1955442128911417345.json
hash: a73e4c7255c6890b
coverage: 0.906977
learned_at: 2026-11-14 01:23:22
nodes: [CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, CLIPTextEncode, VAELoader, SaveVideo, KSamplerAdvanced, VAEDecode, CreateVideo, KSamplerAdvanced, Note, CLIPTextEncode, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, CLIPTextEncode, VAELoader, Note, SaveVideo, KSamplerAdvanced, VAEDecode, CreateVideo, KSamplerAdvanced, CLIPVisionLoader, CLIPVisionEncode, LayerUtility: ImageMaskScaleAs, CLIPVisionEncode, WanFirstLastFrameToVideo, LayerUtility: ImageScaleByAspectRatio V2, Note, CLIPTextEncode, MarkdownNote, LoadImage, WanFirstLastFrameToVideo, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAs, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/【加速版】wan2.2-14B 首尾帧工作流_1955442128911417345.json

> 来源文件 `comfyui_library/workflows/平台全量/【加速版】wan2.2-14B 首尾帧工作流_1955442128911417345.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `KSamplerAdvanced` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `LayerUtility: ImageMaskScaleAs`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoadImage`
- `WanFirstLastFrameToVideo`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAs`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`SaveVideo`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`LayerUtility: ImageMaskScaleAs`、`WanFirstLastFrameToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
