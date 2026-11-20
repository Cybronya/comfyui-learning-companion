---
key: 平台全量/Wan2.2-Bernini-视频编辑人物替换_2061782097475489794.json
name: Wan2.2-Bernini-视频编辑人物替换_2061782097475489794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Bernini-视频编辑人物替换_2061782097475489794.json
hash: 39fce648c2188fb8
coverage: 0.92
learned_at: 2026-11-14 01:05:57
nodes: [MarkdownNote, PathchSageAttentionKJ, Int, UNETLoader, UNETLoader, CLIPLoader, VAELoader, KSamplerAdvanced, Int, VAEDecode, PathchSageAttentionKJ, Int, Int, SimpleMath+, ComfyNumberConvert, VHS_VideoCombine, MarkdownNote, LoadImage, VHS_LoadVideo, BerniniConditioningReferenceSlots, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "res_multistep", "seed": "enable", "steps": "randomize"}
---

# 平台全量/Wan2.2-Bernini-视频编辑人物替换_2061782097475489794.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Bernini-视频编辑人物替换_2061782097475489794.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（25 个）：
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `Int`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `Int`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `Int`
- `Int`
- `SimpleMath+`
- `ComfyNumberConvert`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoadImage`
- `VHS_LoadVideo`
- `BerniniConditioningReferenceSlots`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `res_multistep`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`PathchSageAttentionKJ`、`Int`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`VAEDecode`、`SimpleMath+`、`ComfyNumberConvert`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`、`BerniniConditioningReferenceSlots`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced
