---
key: 视频生成/图生视频/Wan2.1图生视频加速版_1931946637348765697.json
name: Wan2.1图生视频加速版_1931946637348765697.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1图生视频加速版_1931946637348765697.json
hash: 50c1b3148daa56e8
coverage: 0.947368
learned_at: 2026-10-15 22:30:10
nodes: [LoadImage, UnetLoaderGGUF, PathchSageAttentionKJ, PatchModelPatcherOrder, BasicScheduler, SplitSigmas, CLIPLoader, CLIPVisionLoader, CLIPTextEncode, VAEDecode, VAELoader, KSamplerSelect, SamplerCustom, SamplerCustom, WanImageToVideo, CLIPVisionEncode, PrimitiveNode, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1图生视频加速版_1931946637348765697.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1931946637348765697.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（19 个）：
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `PatchModelPatcherOrder`
- `BasicScheduler`
- `SplitSigmas`
- `CLIPLoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **95%**（18/19）

**有卡**：`LoadImage`、`UnetLoaderGGUF`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`BasicScheduler`、`SplitSigmas`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`KSamplerSelect`、`SamplerCustom`、`WanImageToVideo`、`CLIPVisionEncode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、CLIPVisionEncode
