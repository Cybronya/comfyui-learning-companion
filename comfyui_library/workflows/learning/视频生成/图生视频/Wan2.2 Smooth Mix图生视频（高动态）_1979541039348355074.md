---
key: 视频生成/图生视频/Wan2.2 Smooth Mix图生视频（高动态）_1979541039348355074.json
name: Wan2.2 Smooth Mix图生视频（高动态）_1979541039348355074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979541039348355074.json
hash: b731977de5de92ad
coverage: 0.734694
learned_at: 2026-10-15 22:32:24
nodes: [Note, Wan22PromptSelector, JWInteger, ImpactSwitch, GetNode, RH_LLMAPI_NODE, CLIPVisionLoader, CLIPVisionEncode, SeedVR2BlockSwap, SeedVR2ExtraArgs, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, RIFE VFI, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, LoadImage, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, Text Concatenate, ModelPatchTorchSettings, UNETLoader, UNETLoader, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, GetNode, CLIPLoader, VAELoader, SetNode, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, VHS_VideoCombine, easy showAnything, WanImageToVideo, SeedVR2GGUF, CR Text, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), ShowText|pysssss, MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Smooth Mix图生视频（高动态）_1979541039348355074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979541039348355074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `Note`
- `Wan22PromptSelector`
- `JWInteger`
- `ImpactSwitch`
- `GetNode`
- `RH_LLMAPI_NODE`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Text Concatenate`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `VHS_VideoCombine`
- `easy showAnything`
- `WanImageToVideo`
- `SeedVR2GGUF`
- `CR Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `ShowText|pysssss`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **73%**（36/49）

**有卡**：`Wan22PromptSelector`、`JWInteger`、`RH_LLMAPI_NODE`、`CLIPVisionLoader`、`CLIPVisionEncode`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`wanBlockSwap`、`PathchSageAttentionKJ`、`RIFE VFI`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text Concatenate`、`UNETLoader`、`KSamplerAdvanced`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`VHS_VideoCombine`、`WanImageToVideo`、`SeedVR2GGUF`、`CR Text`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、SeedVR2BlockSwap
