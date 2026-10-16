---
key: 视频生成/图生视频/丝滑首尾帧视频生成（Wan2.2 Smooth）_2033421738389803009.json
name: 丝滑首尾帧视频生成（Wan2.2 Smooth）_2033421738389803009.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033421738389803009.json
hash: e95206a7da8199ad
coverage: 0.875
learned_at: 2026-10-15 22:35:39
nodes: [VAEDecode, wanBlockSwap, KSamplerAdvanced, wanBlockSwap, UNETLoader, UNETLoader, WanFirstLastFrameToVideo, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, ImageLoader, ImageLoader, Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, INTConstant, INTConstant, TextInput_, Int, Note, Int, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/丝滑首尾帧视频生成（Wan2.2 Smooth）_2033421738389803009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033421738389803009.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `VAEDecode` ★核心
- `wanBlockSwap`
- `KSamplerAdvanced` ★核心
- `wanBlockSwap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageLoader`
- `ImageLoader`
- `Note`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `TextInput_`
- `Int`
- `Note`
- `Int`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`VAEDecode`、`wanBlockSwap`、`KSamplerAdvanced`、`UNETLoader`、`WanFirstLastFrameToVideo`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`INTConstant`、`TextInput_`、`Int`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
