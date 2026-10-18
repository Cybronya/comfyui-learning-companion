---
key: 视频生成/图生视频/Wan2.1 I2V 3x Faster 图生视频_1930821800060452865.json
name: Wan2.1 I2V 3x Faster 图生视频_1930821800060452865.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 I2V 3x Faster 图生视频_1930821800060452865.json
hash: a885480cd7c90d3d
coverage: 0.947368
learned_at: 2026-10-15 22:30:07
nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPLoader, CLIPTextEncode, PathchSageAttentionKJ, PatchModelPatcherOrder, KSamplerSelect, SplitSigmas, SamplerCustom, UnetLoaderGGUF, BasicScheduler, SamplerCustom, VAEDecode, CLIPVisionLoader, LoadImage, PrimitiveNode, VAELoader, VHS_VideoCombine, WanImageToVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 I2V 3x Faster 图生视频_1930821800060452865.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1930821800060452865.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（19 个）：
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PatchModelPatcherOrder`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `SamplerCustom` ★核心
- `UnetLoaderGGUF` ★核心
- `BasicScheduler`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `LoadImage`
- `PrimitiveNode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`CLIPTextEncode`、`CLIPVisionEncode`、`CLIPLoader`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`KSamplerSelect`、`SplitSigmas`、`SamplerCustom`、`UnetLoaderGGUF`、`BasicScheduler`、`VAEDecode`、`CLIPVisionLoader`、`LoadImage`、`VAELoader`、`VHS_VideoCombine`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、CLIPVisionEncode
