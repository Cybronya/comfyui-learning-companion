---
key: 视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979519177214038018.json
name: Wan2.2 Smooth Mix文生视频（高动态）_1979519177214038018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979519177214038018.json
hash: 1329a64ec494165b
coverage: 0.688889
learned_at: 2026-10-10 23:06:56
nodes: [Wan22PromptSelector, JWInteger, RH_LLMAPI_NODE, Text Concatenate, RH_LLMAPI_NODE, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VHS_VideoCombine, VHS_VideoCombine, ModelSamplingSD3, wanBlockSwap, ModelSamplingSD3, wanBlockSwap, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, MathExpression|pysssss, RIFE VFI, ImpactSwitch, CLIPLoader, VAELoader, SetNode, SetNode, GetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, SetNode, ModelPatchTorchSettings, GetNode, GetNode, WanImageToVideo, Fast Groups Bypasser (rgthree), easy showAnything, JWInteger, JWInteger, VHS_VideoCombine, VAEDecode, UNETLoader, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, JWInteger, CR Text]
patterns: []
missing: [CR Text, MathExpression|pysssss, RIFE VFI, Text Concatenate]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979519177214038018.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979519177214038018.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（45 个）：
- `Wan22PromptSelector`
- `JWInteger`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `RH_LLMAPI_NODE`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `RIFE VFI`
- `ImpactSwitch`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `SetNode`
- `SetNode`
- `ModelPatchTorchSettings`
- `GetNode`
- `GetNode`
- `WanImageToVideo`
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（31/45）

**有卡**：`Wan22PromptSelector`、`JWInteger`、`RH_LLMAPI_NODE`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`VHS_VideoCombine`、`ModelSamplingSD3`、`wanBlockSwap`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ModelPatchTorchSettings`、`WanImageToVideo`、`VAEDecode`、`UNETLoader`、`KSamplerAdvanced`

**缺卡**（4）：`CR Text`、`MathExpression|pysssss`、`RIFE VFI`、`Text Concatenate`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SeedVR2BlockSwap、SeedVR2ExtraArgs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
