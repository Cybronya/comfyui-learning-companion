---
key: 视频生成/文生视频/wan2.1 sageattension 文生视频基础工作流_1903963257324085250.json
name: wan2.1 sageattension 文生视频基础工作流_1903963257324085250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1903963257324085250.json
hash: ad90d8e6c5654fd7
coverage: 1
learned_at: 2026-10-15 22:43:21
nodes: [PatchModelPatcherOrder, VAEDecode, VAELoader, ModelSamplingSD3, VHS_VideoCombine, CLIPTextEncode, KSampler, UnetLoaderGGUF, CLIPLoader, UNETLoader, PathchSageAttentionKJ, CLIPTextEncode, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 452880652404662, "steps": 30}
---

# 视频生成/文生视频/wan2.1 sageattension 文生视频基础工作流_1903963257324085250.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1903963257324085250.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（13 个）：
- `PatchModelPatcherOrder`
- `VAEDecode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `452880652404662`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`PatchModelPatcherOrder`、`VAEDecode`、`VAELoader`、`ModelSamplingSD3`、`VHS_VideoCombine`、`CLIPTextEncode`、`KSampler`、`UnetLoaderGGUF`、`CLIPLoader`、`UNETLoader`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、ModelSamplingSD3
