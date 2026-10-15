---
key: 视频生成/文生视频/Wan2.2 文生视频 Smooth Mix 动态丝滑_1979834834325508097.json
name: Wan2.2 文生视频 Smooth Mix 动态丝滑_1979834834325508097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频 Smooth Mix 动态丝滑_1979834834325508097.json
hash: 40469237d23a6e47
coverage: 0.945946
learned_at: 2026-10-15 22:47:11
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, UNETLoader, KSamplerAdvanced, WanImageToVideo, JWInteger, ModelSamplingSD3, ModelPatchTorchSettings, UNETLoader, wanBlockSwap, JWInteger, PathchSageAttentionKJ, Wan22PromptSelector, RH_LLMAPI_NODE, RH_LLMAPI_NODE, ImpactSwitch, JWInteger, easy showAnything, JWInteger, CR Text, VAEDecode, VHS_VideoCombine, Text Concatenate, CLIPLoader, VAELoader, ModelSamplingSD3, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, MathExpression|pysssss, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2 文生视频 Smooth Mix 动态丝滑_1979834834325508097.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频 Smooth Mix 动态丝滑_1979834834325508097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（37 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RIFE VFI`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `JWInteger`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `JWInteger`
- `PathchSageAttentionKJ`
- `Wan22PromptSelector`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `JWInteger`
- `easy showAnything`
- `JWInteger`
- `CR Text`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `Text Concatenate`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`VHS_VideoCombine`、`RIFE VFI`、`UNETLoader`、`KSamplerAdvanced`、`WanImageToVideo`、`JWInteger`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`wanBlockSwap`、`PathchSageAttentionKJ`、`Wan22PromptSelector`、`RH_LLMAPI_NODE`、`CR Text`、`VAEDecode`、`Text Concatenate`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SeedVR2BlockSwap、SeedVR2ExtraArgs
