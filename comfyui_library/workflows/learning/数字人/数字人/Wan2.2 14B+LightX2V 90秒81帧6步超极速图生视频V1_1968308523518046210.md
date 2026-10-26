---
key: 数字人/数字人/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1968308523518046210.json
name: Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1968308523518046210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1968308523518046210.json
hash: ca141a69e477bea9
coverage: 1
learned_at: 2026-10-26 01:57:48
nodes: [ModelSamplingSD3, LayerUtility: PurgeVRAM, UNETLoader, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, KSamplerAdvanced, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: PurgeVRAM, CLIPTextEncode, VAELoader, VAEDecode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LoadImage, CLIPTextEncode, VHS_VideoCombine, WanImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 数字人/数字人/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1968308523518046210.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1968308523518046210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanImageToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`LoadImage`、`VHS_VideoCombine`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
