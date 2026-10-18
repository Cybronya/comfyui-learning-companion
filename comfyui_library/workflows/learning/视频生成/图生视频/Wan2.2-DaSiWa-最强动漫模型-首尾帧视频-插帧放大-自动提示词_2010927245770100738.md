---
key: 视频生成/图生视频/Wan2.2-DaSiWa-最强动漫模型-首尾帧视频-插帧放大-自动提示词_2010927245770100738.json
name: Wan2.2-DaSiWa-最强动漫模型-首尾帧视频-插帧放大-自动提示词_2010927245770100738.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-DaSiWa-最强动漫模型-首尾帧视频-插帧放大-自动提示词_2010927245770100738.json
hash: cdc8ffb5b413bd38
coverage: 0.777778
learned_at: 2026-10-15 22:34:19
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, RIFE VFI, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, GetNode, GetNode, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, SeedVR2GGUF, RH_LLMAPI_NODE, ImageConcanate, CLIPVisionEncode, WanFirstLastFrameToVideo, CLIPVisionEncode, VHS_VideoCombine, VAEDecode, ImageConcanate, ImageConcanate, CLIPLoader, VAELoader, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, GetNode, UNETLoader, UNETLoader, CLIPVisionLoader, MathExpression|pysssss, SetNode, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, JWInteger, LoadImage, LoadImage, CR Text, ImpactSwitch, MarkdownNote, easy showAnything, VHS_VideoCombine, AddLabel, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-DaSiWa-最强动漫模型-首尾帧视频-插帧放大-自动提示词_2010927245770100738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010927245770100738.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（54 个）：
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
- `RH_LLMAPI_NODE`
- `ImageConcanate`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
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
- `GetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `MathExpression|pysssss`
- `SetNode`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `ImpactSwitch`
- `MarkdownNote`
- `easy showAnything`
- `VHS_VideoCombine`
- `AddLabel`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（42/54）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`RIFE VFI`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`SeedVR2GGUF`、`RH_LLMAPI_NODE`、`ImageConcanate`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`UNETLoader`、`CLIPVisionLoader`、`MathExpression|pysssss`、`KSamplerAdvanced`、`LoadImage`、`CR Text`、`AddLabel`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
