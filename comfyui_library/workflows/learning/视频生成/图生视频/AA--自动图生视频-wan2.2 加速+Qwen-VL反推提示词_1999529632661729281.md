---
key: 视频生成/图生视频/AA--自动图生视频-wan2.2 加速+Qwen-VL反推提示词_1999529632661729281.json
name: AA--自动图生视频-wan2.2 加速+Qwen-VL反推提示词_1999529632661729281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AA--自动图生视频-wan2.2 加速+Qwen-VL反推提示词_1999529632661729281.json
hash: e6d7d5b854cebf1a
coverage: 0.8
learned_at: 2026-10-15 22:33:37
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Note, Note, CLIPTextEncode, LayerUtility: PurgeVRAM, easy saveText, SaveImage, ImageScaleBy, VAELoader, CLIPLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, easy showAnything, CLIPTextEncode, ImageScaleBy, VHS_VideoCombine, WanImageToVideo, Note, Note, easy int, Note, easy float, Qwen3_VQA, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/AA--自动图生视频-wan2.2 加速+Qwen-VL反推提示词_1999529632661729281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999529632661729281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `easy saveText`
- `SaveImage`
- `ImageScaleBy`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `ImageScaleBy`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `Note`
- `Note`
- `easy int`
- `Note`
- `easy float`
- `Qwen3_VQA`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`easy saveText`、`SaveImage`、`ImageScaleBy`、`VAELoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`WanImageToVideo`、`easy int`、`easy float`、`Qwen3_VQA`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
