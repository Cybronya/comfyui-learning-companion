---
key: 图片生成/图生图/YJ-APP-首尾帧  Wan 2.2_2041525838901940226.json
name: YJ-APP-首尾帧  Wan 2.2_2041525838901940226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/YJ-APP-首尾帧  Wan 2.2_2041525838901940226.json
hash: 8458887536c440ad
coverage: 1
learned_at: 2026-10-23 11:28:49
nodes: [wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, VAEDecode, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, WanFirstLastFrameToVideo, KSamplerAdvanced, CLIPVisionEncode, CLIPVisionLoader, CLIPVisionEncode, SimpleMath+, ImageResizeKJv2, ImageResizeKJv2, LoadImage, LoadImage, ModelSamplingSD3, ModelSamplingSD3, ImpactInt, ImpactInt, ImpactInt, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Switch, UNETLoader, UNETLoader, Switch, UNETLoader, UNETLoader, VHS_VideoCombine, Text, Int]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/YJ-APP-首尾帧  Wan 2.2_2041525838901940226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/YJ-APP-首尾帧  Wan 2.2_2041525838901940226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `SimpleMath+`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Switch`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Switch`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `Text`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAEDecode`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`CLIPVisionLoader`、`SimpleMath+`、`ImageResizeKJv2`、`LoadImage`、`ModelSamplingSD3`、`ImpactInt`、`LoraLoaderModelOnly`、`Switch`、`UNETLoader`、`VHS_VideoCombine`、`Text`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
