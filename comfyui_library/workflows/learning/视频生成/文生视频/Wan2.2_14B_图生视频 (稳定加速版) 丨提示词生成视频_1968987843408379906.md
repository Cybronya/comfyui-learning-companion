---
key: 视频生成/文生视频/Wan2.2_14B_图生视频 (稳定加速版) 丨提示词生成视频_1968987843408379906.json
name: Wan2.2_14B_图生视频 (稳定加速版) 丨提示词生成视频_1968987843408379906.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_14B_图生视频 (稳定加速版) 丨提示词生成视频_1968987843408379906.json
hash: 29690589a20d84df
coverage: 1
learned_at: 2026-10-15 22:43:46
nodes: [UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, KSamplerAdvanced, VAELoader, CLIPTextEncode, LoadImage, VAEDecode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine, WanImageToVideo, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2_14B_图生视频 (稳定加速版) 丨提示词生成视频_1968987843408379906.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1968987843408379906.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAELoader`、`LoadImage`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`ModelSamplingSD3`、`VHS_VideoCombine`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
