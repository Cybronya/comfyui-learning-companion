---
key: 平台全量/wan2.2 DaSiWa-首尾帧视频_2009443551440019457.json
name: wan2.2 DaSiWa-首尾帧视频_2009443551440019457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 DaSiWa-首尾帧视频_2009443551440019457.json
hash: 4e95be45df8815d2
coverage: 0.773585
learned_at: 2026-11-14 01:19:17
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, RIFE VFI, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, GetNode, GetNode, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, SeedVR2GGUF, CR Text, RH_LLMAPI_NODE, ImageConcanate, CLIPVisionEncode, WanFirstLastFrameToVideo, CLIPVisionEncode, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, ImageConcanate, ImageConcanate, CLIPLoader, VAELoader, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, ImpactSwitch, GetNode, Note, Fast Groups Bypasser (rgthree), UNETLoader, UNETLoader, CLIPVisionLoader, MathExpression|pysssss, SetNode, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, LoadImage, LoadImage, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 平台全量/wan2.2 DaSiWa-首尾帧视频_2009443551440019457.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 DaSiWa-首尾帧视频_2009443551440019457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（53 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `VHS_VideoCombine`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `GetNode`
- `GetNode`
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `SeedVR2GGUF`
- `CR Text`
- `RH_LLMAPI_NODE`
- `ImageConcanate`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `JWInteger`
- `ImpactSwitch`
- `GetNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `MathExpression|pysssss`
- `SetNode`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `easy showAnything`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（41/53）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`RIFE VFI`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`SeedVR2GGUF`、`CR Text`、`RH_LLMAPI_NODE`、`ImageConcanate`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`UNETLoader`、`CLIPVisionLoader`、`MathExpression|pysssss`、`KSamplerAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、UNETLoader、KSamplerAdvanced
