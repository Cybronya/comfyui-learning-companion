---
key: 视频生成/图生视频/wan2.1 图生视频低显存高速度_1950857599925288961.json
name: wan2.1 图生视频低显存高速度_1950857599925288961.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1 图生视频低显存高速度_1950857599925288961.json
hash: 104e9588abf7dd68
coverage: 1
learned_at: 2026-10-15 22:30:56
nodes: [TrimVideoLatent, VAEDecode, CreateVideo, CLIPTextEncode, SaveVideo, ModelSamplingSD3, PatchModelPatcherOrder, PathchSageAttentionKJ, CFGZeroStar, LoadImage, VAELoader, CLIPLoader, UNETLoader, WanVaceToVideo, CLIPTextEncode, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 341762680335228, "steps": 10}
---

# 视频生成/图生视频/wan2.1 图生视频低显存高速度_1950857599925288961.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950857599925288961.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `LoadImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `341762680335228`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`CreateVideo`、`CLIPTextEncode`、`SaveVideo`、`ModelSamplingSD3`、`PatchModelPatcherOrder`、`PathchSageAttentionKJ`、`CFGZeroStar`、`LoadImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`WanVaceToVideo`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStar
