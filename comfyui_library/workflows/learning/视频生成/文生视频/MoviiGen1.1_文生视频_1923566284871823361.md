---
key: 视频生成/文生视频/MoviiGen1.1_文生视频_1923566284871823361.json
name: MoviiGen1.1_文生视频_1923566284871823361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1923566284871823361.json
hash: fc1d306b964c03a6
coverage: 1
learned_at: 2026-10-15 22:43:24
nodes: [VAEDecode, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, TorchCompileModel, CLIPTextEncode, VHS_VideoCombine, KSampler, UNETLoader, PathchSageAttentionKJ, CLIPLoader, VAELoader, EmptyHunyuanLatentVideo, RIFE VFI]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 0, "steps": 30}
---

# 视频生成/文生视频/MoviiGen1.1_文生视频_1923566284871823361.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1923566284871823361.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `TorchCompileModel`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `RIFE VFI`

## 关键参数

- `seed` = `0`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`VAEDecode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`TorchCompileModel`、`VHS_VideoCombine`、`KSampler`、`UNETLoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`、`RIFE VFI`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo
