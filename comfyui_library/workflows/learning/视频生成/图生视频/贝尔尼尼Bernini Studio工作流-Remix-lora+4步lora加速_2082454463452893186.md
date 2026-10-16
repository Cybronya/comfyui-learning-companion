---
key: 视频生成/图生视频/贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082454463452893186.json
name: 贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082454463452893186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2082454463452893186.json
hash: fd4c7e3aa60bb3f4
coverage: 0.823529
learned_at: 2026-10-15 22:42:32
nodes: [SetNode, LoadImage, UNETLoader, UNETLoader, VAELoader, CLIPLoader, RTXVideoSuperResolution, SimpleMath+, Int, PathchSageAttentionKJ, PathchSageAttentionKJ, VHS_LoadVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, GetNode, VAEDecode, GetNode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, LoadImage, VHS_VideoCombine, MarkdownNote, MarkdownNote, BerniniStudio, MarkdownNote, LoadImage, Int, Int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082454463452893186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082454463452893186.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（34 个）：
- `SetNode`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `RTXVideoSuperResolution`
- `SimpleMath+`
- `Int`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VHS_LoadVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `LoadImage`
- `VHS_VideoCombine`
- `MarkdownNote`
- `MarkdownNote`
- `BerniniStudio`
- `MarkdownNote`
- `LoadImage`
- `Int`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`LoadImage`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`RTXVideoSuperResolution`、`SimpleMath+`、`Int`、`PathchSageAttentionKJ`、`VHS_LoadVideo`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VAEDecode`、`ImageConcatMulti`、`VHS_VideoCombine`、`BerniniStudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、RTXVideoSuperResolution
