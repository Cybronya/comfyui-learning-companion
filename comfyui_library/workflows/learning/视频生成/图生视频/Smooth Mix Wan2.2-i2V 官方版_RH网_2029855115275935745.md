---
key: 视频生成/图生视频/Smooth Mix Wan2.2-i2V 官方版_RH网_2029855115275935745.json
name: Smooth Mix Wan2.2-i2V 官方版_RH网_2029855115275935745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Smooth Mix Wan2.2-i2V 官方版_RH网_2029855115275935745.json
hash: cad2d66d0aac3894
coverage: 0.913043
learned_at: 2026-10-15 22:35:23
nodes: [CLIPTextEncode, easy cleanGpuUsed, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, WanImageToVideo, VAELoader, CLIPTextEncode, KSamplerAdvanced, easy int, VHS_VideoCombine, Text Multiline, VHS_VideoCombine, RIFE VFI, ImageScaleBy, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, GetNode, VAEDecode, SetNode]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Smooth Mix Wan2.2-i2V 官方版_RH网_2029855115275935745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029855115275935745.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `WanImageToVideo`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `VHS_VideoCombine`
- `Text Multiline`
- `VHS_VideoCombine`
- `RIFE VFI`
- `ImageScaleBy`
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`CLIPTextEncode`、`easy cleanGpuUsed`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`WanImageToVideo`、`VAELoader`、`KSamplerAdvanced`、`easy int`、`VHS_VideoCombine`、`Text Multiline`、`RIFE VFI`、`ImageScaleBy`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageScaleBy
