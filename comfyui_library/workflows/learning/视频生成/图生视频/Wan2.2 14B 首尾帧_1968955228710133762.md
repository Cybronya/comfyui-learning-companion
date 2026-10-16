---
key: 视频生成/图生视频/Wan2.2 14B 首尾帧_1968955228710133762.json
name: Wan2.2 14B 首尾帧_1968955228710133762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1968955228710133762.json
hash: 0f2840bb3afb775d
coverage: 1
learned_at: 2026-10-15 22:31:47
nodes: [UNETLoader, LoadImage, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, CLIPTextEncode, VAELoader, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, VAEDecode, WanFirstLastFrameToVideo, LoadImage, CLIPTextEncode, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B 首尾帧_1968955228710133762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968955228710133762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `WanFirstLastFrameToVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`UNETLoader`、`LoadImage`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`WanFirstLastFrameToVideo`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
