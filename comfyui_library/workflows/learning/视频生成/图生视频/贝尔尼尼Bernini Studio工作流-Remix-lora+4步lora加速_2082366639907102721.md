---
key: 视频生成/图生视频/贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082366639907102721.json
name: 贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082366639907102721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082366639907102721.json
hash: 38ef26eae1efdbb4
coverage: 0.828571
learned_at: 2026-10-15 22:42:30
nodes: [SetNode, LoadImage, UNETLoader, UNETLoader, VAELoader, CLIPLoader, RTXVideoSuperResolution, SimpleMath+, PathchSageAttentionKJ, PathchSageAttentionKJ, VHS_LoadVideo, KSamplerAdvanced, KSamplerAdvanced, GetNode, VAEDecode, GetNode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote, MarkdownNote, Int, VHS_VideoCombine, ImageConcatMulti, BerniniStudio, Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Int, Int, LoadImage, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082366639907102721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082366639907102721.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（35 个）：
- `SetNode`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `RTXVideoSuperResolution`
- `SimpleMath+`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VHS_LoadVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MarkdownNote`
- `MarkdownNote`
- `Int`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `BerniniStudio`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Int`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（29/35）

**有卡**：`LoadImage`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`RTXVideoSuperResolution`、`SimpleMath+`、`PathchSageAttentionKJ`、`VHS_LoadVideo`、`KSamplerAdvanced`、`VAEDecode`、`ImageConcatMulti`、`VHS_VideoCombine`、`Int`、`BerniniStudio`、`Text`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、RTXVideoSuperResolution
