---
key: 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1 浮云_1996401587960561665.json
name: Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1 浮云_1996401587960561665.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1 浮云_1996401587960561665.json
hash: 61c37a96722f5db3
coverage: 0.913043
learned_at: 2026-10-15 22:33:26
nodes: [CLIPTextEncode, VAELoader, Note, ModelSamplingSD3, Note, UNETLoader, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, KSamplerAdvanced, LoraLoaderModelOnly, VHS_VideoCombine, WanImageToVideo, JWInteger, JWInteger, JWInteger, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1 浮云_1996401587960561665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996401587960561665.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（23 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `ModelSamplingSD3`
- `Note`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `WanImageToVideo`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`KSamplerAdvanced`、`VAEDecode`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`WanImageToVideo`、`JWInteger`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
