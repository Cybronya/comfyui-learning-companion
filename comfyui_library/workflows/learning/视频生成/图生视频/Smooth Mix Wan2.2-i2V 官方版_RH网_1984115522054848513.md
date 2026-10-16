---
key: 视频生成/图生视频/Smooth Mix Wan2.2-i2V 官方版_RH网_1984115522054848513.json
name: Smooth Mix Wan2.2-i2V 官方版_RH网_1984115522054848513.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1984115522054848513.json
hash: 3dd50e511f0837ee
coverage: 0.807692
learned_at: 2026-10-15 22:32:47
nodes: [Note, CLIPTextEncode, easy cleanGpuUsed, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, LoadImage, CLIPLoader, WanImageToVideo, Note, VAELoader, CLIPTextEncode, VAEDecode, SetNode, KSamplerAdvanced, easy int, VHS_VideoCombine, GetNode, Text Multiline, VHS_VideoCombine, RIFE VFI, ImageScaleBy, KSamplerAdvanced, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Smooth Mix Wan2.2-i2V 官方版_RH网_1984115522054848513.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1984115522054848513.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `Note`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoadImage`
- `CLIPLoader`
- `WanImageToVideo`
- `Note`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `KSamplerAdvanced` ★核心
- `easy int`
- `VHS_VideoCombine`
- `GetNode`
- `Text Multiline`
- `VHS_VideoCombine`
- `RIFE VFI`
- `ImageScaleBy`
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`CLIPTextEncode`、`easy cleanGpuUsed`、`UNETLoader`、`ModelSamplingSD3`、`LoadImage`、`CLIPLoader`、`WanImageToVideo`、`VAELoader`、`VAEDecode`、`KSamplerAdvanced`、`easy int`、`VHS_VideoCombine`、`Text Multiline`、`RIFE VFI`、`ImageScaleBy`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageScaleBy
