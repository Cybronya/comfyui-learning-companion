---
key: 视频生成/图生视频/wan2.2图生视频加速流_1950004160121978881.json
name: wan2.2图生视频加速流_1950004160121978881.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频加速流_1950004160121978881.json
hash: 52df01de6b703b83
coverage: 1
learned_at: 2026-10-15 22:30:51
nodes: [CLIPLoader, easy int, easy int, VHS_VideoCombine, VAEDecode, easy int, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAELoader, UNETLoader, LoadImage, CLIPTextEncode, WanImageToVideo, CLIPTextEncode, LoraLoaderModelOnly, SimpleMath+, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2图生视频加速流_1950004160121978881.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950004160121978881.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `CLIPLoader`
- `easy int`
- `easy int`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `easy int`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`CLIPLoader`、`easy int`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerAdvanced`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`VAELoader`、`LoadImage`、`CLIPTextEncode`、`WanImageToVideo`、`LoraLoaderModelOnly`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
