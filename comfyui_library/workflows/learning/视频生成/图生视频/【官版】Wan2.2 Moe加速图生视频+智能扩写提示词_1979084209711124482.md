---
key: 视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频+智能扩写提示词_1979084209711124482.json
name: 【官版】Wan2.2 Moe加速图生视频+智能扩写提示词_1979084209711124482.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979084209711124482.json
hash: f463a9e70b2b8116
coverage: 0.75
learned_at: 2026-10-15 22:32:21
nodes: [MarkdownNote, MarkdownNote, UNETLoader, wanBlockSwap, wanBlockSwap, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, VAELoader, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, Note, ShowText|pysssss, Text Concatenate, Wan22PromptSelector, RH_LLMAPI_NODE, ShowText|pysssss, PrimitiveInt, MathExpression|pysssss, Reroute, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, RIFE VFI, ModelSamplingSD3, LoraLoaderModelOnly, PrimitiveInt, ImpactSwitch, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, LoadImage, PrimitiveStringMultiline, UNETLoader, CLIPVisionLoader, ModelSamplingSD3, KSamplerAdvanced, WanImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频+智能扩写提示词_1979084209711124482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979084209711124482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `Note`
- `ShowText|pysssss`
- `Text Concatenate`
- `Wan22PromptSelector`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `RIFE VFI`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `ImpactSwitch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoadImage`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（30/40）

**有卡**：`UNETLoader`、`wanBlockSwap`、`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`VAELoader`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`Text Concatenate`、`Wan22PromptSelector`、`RH_LLMAPI_NODE`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`RIFE VFI`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LoadImage`、`CLIPVisionLoader`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
