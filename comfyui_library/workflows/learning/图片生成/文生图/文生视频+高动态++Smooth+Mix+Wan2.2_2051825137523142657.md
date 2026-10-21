---
key: 图片生成/文生图/文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657.json
name: 文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657.json
hash: 2342db20b52d2223
coverage: 0.813953
learned_at: 2026-10-21 03:01:11
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, RIFE VFI, UNETLoader, KSamplerAdvanced, WanImageToVideo, ModelSamplingSD3, ModelPatchTorchSettings, UNETLoader, ModelSamplingSD3, wanBlockSwap, PathchSageAttentionKJ, wanBlockSwap, ModelPatchTorchSettings, VAELoader, KSamplerAdvanced, PathchSageAttentionKJ, VAEDecode, VHS_VideoCombine, JWInteger, JWInteger, JWInteger, GetNode, GetNode, GetNode, CLIPLoader, Wan22PromptSelector, Text Concatenate, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, SetNode, Note, CR Text Input Switch (4 way), easy showAnything, RH_LLMAPI_NODE, RH_LLMAPI_NODE, CR Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（43 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `RIFE VFI`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `Wan22PromptSelector`
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `CR Text Input Switch (4 way)`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（35/43）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`VHS_VideoCombine`、`MathExpression|pysssss`、`RIFE VFI`、`UNETLoader`、`KSamplerAdvanced`、`WanImageToVideo`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`wanBlockSwap`、`PathchSageAttentionKJ`、`VAELoader`、`VAEDecode`、`JWInteger`、`CLIPLoader`、`Wan22PromptSelector`、`Text Concatenate`、`CLIPTextEncode`、`CR Text Input Switch (4 way)`、`RH_LLMAPI_NODE`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SeedVR2BlockSwap、SeedVR2ExtraArgs
