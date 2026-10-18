---
key: 视频生成/图生视频/Wan2.2+新版lightx2v加速-4步图生视频【官版】_1950101403698159617.json
name: Wan2.2+新版lightx2v加速-4步图生视频【官版】_1950101403698159617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+新版lightx2v加速-4步图生视频【官版】_1950101403698159617.json
hash: 9c993ab08e81f763
coverage: 0.714286
learned_at: 2026-10-15 22:30:53
nodes: [Wan22PromptSelector, JWInteger, SetNode, GetNode, GetImageSizeAndCount, VAEDecode, GetNode, KSamplerAdvanced, KSamplerAdvanced, RH_LLMAPI_NODE, ImpactSwitch, Note, GetNode, WanImageToVideo, CLIPTextEncode, GetNode, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, MathExpression|pysssss, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, UNETLoader, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, SetNode, wanBlockSwap, SetNode, VAELoader, LoraLoaderModelOnly, CLIPLoader, CR Text, Text Concatenate, ShowText|pysssss, VHS_VideoCombine, LoraLoaderModelOnly, wanBlockSwap, MarkdownNote, MarkdownNote, VHS_VideoCombine, RIFE VFI, easy showAnything, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ModelSamplingSD3]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2+新版lightx2v加速-4步图生视频【官版】_1950101403698159617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950101403698159617.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `Wan22PromptSelector`
- `JWInteger`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `VAEDecode` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `Note`
- `GetNode`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `wanBlockSwap`
- `SetNode`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CR Text`
- `Text Concatenate`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `MarkdownNote`
- `MarkdownNote`
- `VHS_VideoCombine`
- `RIFE VFI`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `ModelSamplingSD3`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **71%**（35/49）

**有卡**：`Wan22PromptSelector`、`JWInteger`、`GetImageSizeAndCount`、`VAEDecode`、`KSamplerAdvanced`、`RH_LLMAPI_NODE`、`WanImageToVideo`、`CLIPTextEncode`、`CLIPVisionEncode`、`CLIPVisionLoader`、`MathExpression|pysssss`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`LoraLoaderModelOnly`、`wanBlockSwap`、`VAELoader`、`CLIPLoader`、`CR Text`、`Text Concatenate`、`VHS_VideoCombine`、`RIFE VFI`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
