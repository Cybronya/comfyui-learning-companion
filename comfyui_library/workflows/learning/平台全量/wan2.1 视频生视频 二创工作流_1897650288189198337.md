---
key: 平台全量/wan2.1 视频生视频 二创工作流_1897650288189198337.json
name: wan2.1 视频生视频 二创工作流_1897650288189198337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1 视频生视频 二创工作流_1897650288189198337.json
hash: fc37f370d5bd6832
coverage: 1
learned_at: 2026-11-14 01:19:06
nodes: [CLIPLoader, VAELoader, VAEEncodeTiled, VAEDecode, UNETLoader, ModelSamplingSD3, PathchSageAttentionKJ, PatchModelPatcherOrder, KSampler, CLIPTextEncode, CLIPTextEncode, ImageResizeKJ, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 0.75, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 801156349364285, "steps": 30}
---

# 平台全量/wan2.1 视频生视频 二创工作流_1897650288189198337.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1 视频生视频 二创工作流_1897650288189198337.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEEncodeTiled` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PatchModelPatcherOrder`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `801156349364285`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.75`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEEncodeTiled`、`VAEDecode`、`UNETLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`KSampler`、`CLIPTextEncode`、`ImageResizeKJ`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、VAEEncodeTiled、ImageResizeKJ
