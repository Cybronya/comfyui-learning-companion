---
key: 视频生成/图生视频/WAN2.2图生视频_2025568584335892482.json
name: WAN2.2图生视频_2025568584335892482.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2025568584335892482.json
hash: 183efb2a76a718f2
coverage: 0.958333
learned_at: 2026-10-15 22:35:12
nodes: [PathchSageAttentionKJ, wanBlockSwap, wanBlockSwap, VAELoader, CLIPTextEncode, CLIPTextEncode, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoadImage, WanImageToVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, CLIPLoader, PreviewImage, UNETLoader, VHS_VideoCombine, ImageResize+]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "increment"}
---

# 视频生成/图生视频/WAN2.2图生视频_2025568584335892482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2025568584335892482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `wanBlockSwap`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `WanImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `PreviewImage`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `ImageResize+`

## 关键参数

- `seed` = `disable`
- `steps` = `increment`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`PathchSageAttentionKJ`、`wanBlockSwap`、`VAELoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LoadImage`、`WanImageToVideo`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`VHS_VideoCombine`、`ImageResize+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
