---
key: 视频生成/文生视频/Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505.json
name: Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505.json
hash: 0e5c60e3ce489c7e
coverage: 0.954545
learned_at: 2026-10-15 22:44:27
nodes: [ModelSamplingSD3, easy cleanGpuUsed, MarkdownNote, VAEDecode, easy cleanGpuUsed, ModelSamplingSD3, PathchSageAttentionKJ, CLIPTextEncode, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, INTConstant, INTConstant, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `MarkdownNote`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`ModelSamplingSD3`、`easy cleanGpuUsed`、`VAEDecode`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`KSamplerAdvanced`、`VHS_VideoCombine`、`INTConstant`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
