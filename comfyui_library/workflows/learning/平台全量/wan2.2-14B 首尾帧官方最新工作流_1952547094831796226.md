---
key: 平台全量/wan2.2-14B 首尾帧官方最新工作流_1952547094831796226.json
name: wan2.2-14B 首尾帧官方最新工作流_1952547094831796226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2-14B 首尾帧官方最新工作流_1952547094831796226.json
hash: 6e242fc819d2001b
coverage: 0.866667
learned_at: 2026-11-14 01:19:25
nodes: [CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, UNETLoader, UNETLoader, CLIPTextEncode, VAELoader, Note, SaveVideo, KSamplerAdvanced, VAEDecode, CreateVideo, KSamplerAdvanced, Note, CLIPTextEncode, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, CLIPTextEncode, VAELoader, Note, SaveVideo, KSamplerAdvanced, VAEDecode, CreateVideo, KSamplerAdvanced, CLIPVisionLoader, CLIPVisionEncode, LayerUtility: ImageMaskScaleAs, CLIPVisionEncode, WanFirstLastFrameToVideo, LayerUtility: ImageScaleByAspectRatio V2, Note, CLIPTextEncode, MarkdownNote, LoadImage, WanFirstLastFrameToVideo, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAs, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/wan2.2-14B 首尾帧官方最新工作流_1952547094831796226.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2-14B 首尾帧官方最新工作流_1952547094831796226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
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

覆盖率 **87%**（39/45）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`SaveVideo`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`LayerUtility: ImageMaskScaleAs`、`WanFirstLastFrameToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
