---
key: 视频生成/图生视频/Wan2.2-RemixV2图生视频（加速放大版）_2003147433540558850.json
name: Wan2.2-RemixV2图生视频（加速放大版）_2003147433540558850.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2003147433540558850.json
hash: 20a21fc7fbc53f53
coverage: 0.964286
learned_at: 2026-10-15 22:33:50
nodes: [CLIPTextEncode, ModelPatchTorchSettings, easy showAnything, PathchSageAttentionKJ, easy int, wanBlockSwap, WanImageToVideo, ModelSamplingSD3, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, easy clearCacheAll, easy int, easy int, wanBlockSwap, SimpleMath+, FlashVSRNode, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPLoader, VAELoader, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-RemixV2图生视频（加速放大版）_2003147433540558850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2003147433540558850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `easy int`
- `wanBlockSwap`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `easy clearCacheAll`
- `easy int`
- `easy int`
- `wanBlockSwap`
- `SimpleMath+`
- `FlashVSRNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`CLIPTextEncode`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`easy int`、`wanBlockSwap`、`WanImageToVideo`、`ModelSamplingSD3`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerAdvanced`、`easy clearCacheAll`、`SimpleMath+`、`FlashVSRNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ModelPatchTorchSettings
