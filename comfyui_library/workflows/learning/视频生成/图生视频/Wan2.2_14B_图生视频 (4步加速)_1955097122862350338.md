---
key: 视频生成/图生视频/Wan2.2_14B_图生视频 (4步加速)_1955097122862350338.json
name: Wan2.2_14B_图生视频 (4步加速)_1955097122862350338.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955097122862350338.json
hash: cede6add9266954b
coverage: 1
learned_at: 2026-10-15 22:31:07
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, VAEDecode, CLIPTextEncode, VAELoader, LoadImage, CLIPTextEncode, WanImageToVideo, VHS_VideoCombine, CLIPLoader, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_14B_图生视频 (4步加速)_1955097122862350338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955097122862350338.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（18 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `VHS_VideoCombine`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`LoraLoaderModelOnly`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`LoadImage`、`WanImageToVideo`、`VHS_VideoCombine`、`CLIPLoader`、`UNETLoader`、`ModelSamplingSD3`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
