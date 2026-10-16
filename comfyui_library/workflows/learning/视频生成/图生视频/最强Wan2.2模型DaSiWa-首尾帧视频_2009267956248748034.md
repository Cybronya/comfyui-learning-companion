---
key: 视频生成/图生视频/最强Wan2.2模型DaSiWa-首尾帧视频_2009267956248748034.json
name: 最强Wan2.2模型DaSiWa-首尾帧视频_2009267956248748034.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2009267956248748034.json
hash: 69af65feb4567ecc
coverage: 0.763636
learned_at: 2026-10-15 22:34:12
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, RIFE VFI, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, GetNode, GetNode, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, SeedVR2GGUF, CR Text, RH_LLMAPI_NODE, ImageConcanate, CLIPVisionEncode, WanFirstLastFrameToVideo, CLIPVisionEncode, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, ImageConcanate, ImageConcanate, CLIPLoader, VAELoader, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, ImpactSwitch, GetNode, Note, easy showAnything, UNETLoader, UNETLoader, CLIPVisionLoader, MathExpression|pysssss, SetNode, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/最强Wan2.2模型DaSiWa-首尾帧视频_2009267956248748034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009267956248748034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
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
- `easy showAnything`
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
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **76%**（42/55）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`RIFE VFI`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`SeedVR2GGUF`、`CR Text`、`RH_LLMAPI_NODE`、`ImageConcanate`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`UNETLoader`、`CLIPVisionLoader`、`MathExpression|pysssss`、`KSamplerAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
