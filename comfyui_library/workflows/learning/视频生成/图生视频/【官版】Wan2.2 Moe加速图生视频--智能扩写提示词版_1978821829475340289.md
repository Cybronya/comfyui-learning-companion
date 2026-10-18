---
key: 视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频--智能扩写提示词版_1978821829475340289.json
name: 【官版】Wan2.2 Moe加速图生视频--智能扩写提示词版_1978821829475340289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频--智能扩写提示词版_1978821829475340289.json
hash: 074fb99a5454c925
coverage: 0.708333
learned_at: 2026-10-15 22:32:20
nodes: [Note, ShowText|pysssss, Wan22PromptSelector, Text Concatenate, JWInteger, JWInteger, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, SetNode, SetNode, VAELoader, SetNode, CLIPLoader, SetNode, ImpactSwitch, GetNode, LoadImage, CLIPTextEncode, CLIPTextEncode, GetNode, MarkdownNote, MarkdownNote, GetImageSizeAndCount, GetNode, RIFE VFI, RH_LLMAPI_NODE, CLIPVisionLoader, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, WanImageToVideo, VAEDecode, GetNode, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, PathchSageAttentionKJ, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, wanBlockSwap, wanBlockSwap, CR Text, easy showAnything, MathExpression|pysssss, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频--智能扩写提示词版_1978821829475340289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978821829475340289.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（48 个）：
- `Note`
- `ShowText|pysssss`
- `Wan22PromptSelector`
- `Text Concatenate`
- `JWInteger`
- `JWInteger`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `ImpactSwitch`
- `GetNode`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `GetImageSizeAndCount`
- `GetNode`
- `RIFE VFI`
- `RH_LLMAPI_NODE`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `CR Text`
- `easy showAnything`
- `MathExpression|pysssss`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **71%**（34/48）

**有卡**：`Wan22PromptSelector`、`Text Concatenate`、`JWInteger`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`LoadImage`、`CLIPTextEncode`、`GetImageSizeAndCount`、`RIFE VFI`、`RH_LLMAPI_NODE`、`CLIPVisionLoader`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanImageToVideo`、`VAEDecode`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`UNETLoader`、`VHS_VideoCombine`、`wanBlockSwap`、`CR Text`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
