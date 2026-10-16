---
key: 视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_prompt_2011733044515835905.json
name: video_wan2_2_14B_i2v_moremotion_prompt_2011733044515835905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2011733044515835905.json
hash: c7a1ac67a443eb52
coverage: 0.5
learned_at: 2026-10-15 22:34:24
nodes: [PathchSageAttentionKJ, CFGZeroStar, SetNode, SetNode, CLIPLoader, GetNode, ModelSamplingSD3, GetNode, SetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, CLIPTextEncode, VAELoader, ModelSamplingSD3, GetNode, GetNode, GetNode, CLIPVisionLoader, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, LoraLoaderModelOnly, SetNode, CLIPVisionEncode, WanVideoNAG, INTConstant, INTConstant, ImageResizeKJv2, SetNode, SetNode, SetNode, GetNode, WanImageToVideo, VHS_VideoCombine, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_prompt_2011733044515835905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011733044515835905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（52 个）：
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CLIPVisionEncode`
- `WanVideoNAG`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanImageToVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **50%**（26/52）

**有卡**：`PathchSageAttentionKJ`、`CFGZeroStar`、`CLIPLoader`、`ModelSamplingSD3`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`UNETLoader`、`CLIPVisionEncode`、`WanVideoNAG`、`INTConstant`、`ImageResizeKJv2`、`WanImageToVideo`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
