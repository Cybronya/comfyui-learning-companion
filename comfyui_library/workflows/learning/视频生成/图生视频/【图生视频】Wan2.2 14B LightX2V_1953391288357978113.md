---
key: 视频生成/图生视频/【图生视频】Wan2.2 14B LightX2V_1953391288357978113.json
name: 【图生视频】Wan2.2 14B LightX2V_1953391288357978113.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953391288357978113.json
hash: 88cb1a562d4c7da1
coverage: 0.956522
learned_at: 2026-10-15 22:31:05
nodes: [UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, SaveImage, WanImageToVideo, PreviewImage, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/【图生视频】Wan2.2 14B LightX2V_1953391288357978113.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953391288357978113.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `WanImageToVideo`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`SaveImage`、`WanImageToVideo`、`LayerUtility: PurgeVRAM`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
