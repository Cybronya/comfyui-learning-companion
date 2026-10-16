---
key: 视频生成/图生视频/💨wan2.2_S_Mix_首尾帧旋转动态变装💨_1985423815310254082.json
name: 💨wan2.2_S_Mix_首尾帧旋转动态变装💨_1985423815310254082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1985423815310254082.json
hash: b85bdde6fe2cbd39
coverage: 0.864865
learned_at: 2026-10-15 22:32:51
nodes: [easy int, SimpleMath+, ImageResizeKJv2, easy seed, ImageResizeKJv2, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, WanFirstLastFrameToVideo, VAEDecode, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, wanBlockSwap, SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, MarkdownNote, LoadImage, ImpactInt, easy int, LoadImage, LoadImage, PathchSageAttentionKJ, CLIPLoader, UNETLoader, VAELoader, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, wanBlockSwap]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/💨wan2.2_S_Mix_首尾帧旋转动态变装💨_1985423815310254082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985423815310254082.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `easy int`
- `SimpleMath+`
- `ImageResizeKJv2`
- `easy seed`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoadImage`
- `ImpactInt`
- `easy int`
- `LoadImage`
- `LoadImage`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`easy int`、`SimpleMath+`、`ImageResizeKJv2`、`easy seed`、`CLIPTextEncode`、`KSamplerAdvanced`、`WanFirstLastFrameToVideo`、`VAEDecode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`wanBlockSwap`、`VHS_VideoCombine`、`LoadImage`、`ImpactInt`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`CR Text`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
