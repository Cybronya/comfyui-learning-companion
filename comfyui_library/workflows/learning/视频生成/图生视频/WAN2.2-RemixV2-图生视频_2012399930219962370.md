---
key: 视频生成/图生视频/WAN2.2-RemixV2-图生视频_2012399930219962370.json
name: WAN2.2-RemixV2-图生视频_2012399930219962370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2012399930219962370.json
hash: da9f3dda89287076
coverage: 1
learned_at: 2026-10-15 22:34:27
nodes: [UNETLoader, CLIPLoader, VAELoader, wanBlockSwap, easy int, VAEDecode, KSamplerAdvanced, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, wanBlockSwap, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, WanImageToVideo, SimpleMath+, UNETLoader, GetImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, easy int, LoadImage, Textbox, KSamplerAdvanced, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2-RemixV2-图生视频_2012399930219962370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2012399930219962370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `wanBlockSwap`
- `easy int`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `SimpleMath+`
- `UNETLoader` ★核心
- `GetImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `easy int`
- `LoadImage`
- `Textbox`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`wanBlockSwap`、`easy int`、`VAEDecode`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`CLIPTextEncode`、`WanImageToVideo`、`SimpleMath+`、`GetImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Textbox`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ModelPatchTorchSettings
