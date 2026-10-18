---
key: 视频生成/图生视频/万相wan2.2首尾帧生视频（2分钟）_1980678850906603522.json
name: 万相wan2.2首尾帧生视频（2分钟）_1980678850906603522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相wan2.2首尾帧生视频（2分钟）_1980678850906603522.json
hash: 62a8dcd18a0acbf8
coverage: 1
learned_at: 2026-10-15 22:32:32
nodes: [UNETLoader, ModelSamplingSD3, JWInteger, ModelSamplingSD3, JWInteger, JWInteger, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, SimpleMath+, CLIPLoader, SimpleMath+, JWInteger, WanFirstLastFrameToVideo, VHS_VideoCombine, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, LoadImage, LoadImage, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/万相wan2.2首尾帧生视频（2分钟）_1980678850906603522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980678850906603522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `JWInteger`
- `ModelSamplingSD3`
- `JWInteger`
- `JWInteger`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SimpleMath+`
- `CLIPLoader`
- `SimpleMath+`
- `JWInteger`
- `WanFirstLastFrameToVideo`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `VAELoader`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`UNETLoader`、`ModelSamplingSD3`、`JWInteger`、`VAEDecode`、`LoraLoaderModelOnly`、`SimpleMath+`、`CLIPLoader`、`WanFirstLastFrameToVideo`、`VHS_VideoCombine`、`CLIPTextEncode`、`KSamplerAdvanced`、`LoadImage`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
