---
key: 视频生成/图生视频/史上最快！Wan2.2高质量图生视频工作流81帧50秒（官方+KJ）_1952381519627259905.json
name: 史上最快！Wan2.2高质量图生视频工作流81帧50秒（官方+KJ）_1952381519627259905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/史上最快！Wan2.2高质量图生视频工作流81帧50秒（官方+KJ）_1952381519627259905.json
hash: 5ecb8609f1501cef
coverage: 0.92
learned_at: 2026-10-15 22:31:01
nodes: [VAELoader, Note, ModelSamplingSD3, LayerUtility: PurgeVRAM, Note, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, JWInteger, JWInteger, UNETLoader, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, JWInteger, CLIPLoader, WanImageToVideo, LoadImage, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/史上最快！Wan2.2高质量图生视频工作流81帧50秒（官方+KJ）_1952381519627259905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952381519627259905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `VAELoader`
- `Note`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `Note`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `JWInteger`
- `JWInteger`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `CLIPLoader`
- `WanImageToVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`VAELoader`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`PathchSageAttentionKJ`、`VAEDecode`、`JWInteger`、`CLIPLoader`、`WanImageToVideo`、`LoadImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
