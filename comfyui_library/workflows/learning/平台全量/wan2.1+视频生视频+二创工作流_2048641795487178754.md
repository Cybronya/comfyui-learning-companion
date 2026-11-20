---
key: 平台全量/wan2.1+视频生视频+二创工作流_2048641795487178754.json
name: wan2.1+视频生视频+二创工作流_2048641795487178754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1+视频生视频+二创工作流_2048641795487178754.json
hash: 3669311834018672
coverage: 1
learned_at: 2026-11-14 01:19:08
nodes: [CLIPLoader, VAELoader, VAEEncodeTiled, VAEDecode, UNETLoader, ModelSamplingSD3, PathchSageAttentionKJ, PatchModelPatcherOrder, KSampler, CLIPTextEncode, ImageResizeKJ, VHS_VideoCombine, VHS_LoadVideo, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 0.75, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 637602861195863, "steps": 30}
---

# 平台全量/wan2.1+视频生视频+二创工作流_2048641795487178754.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1+视频生视频+二创工作流_2048641795487178754.json`

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
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `637602861195863`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.75`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEEncodeTiled`、`VAEDecode`、`UNETLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`KSampler`、`CLIPTextEncode`、`ImageResizeKJ`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、VAEEncodeTiled、ImageResizeKJ
