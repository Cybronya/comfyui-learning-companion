---
key: 视频生成/文生视频/Wan2.2_Smooth Mix高动态文生视频【官版】_1950112023776550913.json
name: Wan2.2_Smooth Mix高动态文生视频【官版】_1950112023776550913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_Smooth Mix高动态文生视频【官版】_1950112023776550913.json
hash: 0e09c332ba306854
coverage: 0.673913
learned_at: 2026-10-10 23:07:20
nodes: [JWInteger, RH_LLMAPI_NODE, Text Concatenate, RH_LLMAPI_NODE, SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, UNETLoader, ModelSamplingSD3, wanBlockSwap, UNETLoader, ModelSamplingSD3, wanBlockSwap, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, RIFE VFI, CLIPLoader, VAELoader, SetNode, SetNode, GetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, ModelPatchTorchSettings, WanImageToVideo, JWInteger, JWInteger, VHS_VideoCombine, SeedVR2GGUF, VHS_VideoCombine, easy cleanGpuUsed, VAEDecode, CR Text, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, MathExpression|pysssss, SetNode, JWInteger, Wan22PromptSelector, Fast Groups Bypasser (rgthree), easy showAnything, ImpactSwitch]
patterns: []
missing: [CR Text, MathExpression|pysssss, RIFE VFI, Text Concatenate, easy cleanGpuUsed]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2_Smooth Mix高动态文生视频【官版】_1950112023776550913.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2_Smooth Mix高动态文生视频【官版】_1950112023776550913.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（46 个）：
- `JWInteger`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `RH_LLMAPI_NODE`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RIFE VFI`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `SetNode`
- `ModelPatchTorchSettings`
- `WanImageToVideo`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `CR Text`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `SetNode`
- `JWInteger`
- `Wan22PromptSelector`
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `ImpactSwitch`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **67%**（31/46）

**有卡**：`JWInteger`、`RH_LLMAPI_NODE`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`UNETLoader`、`ModelSamplingSD3`、`wanBlockSwap`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ModelPatchTorchSettings`、`WanImageToVideo`、`SeedVR2GGUF`、`VAEDecode`、`KSamplerAdvanced`、`Wan22PromptSelector`

**缺卡**（5）：`CR Text`、`MathExpression|pysssss`、`RIFE VFI`、`Text Concatenate`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SeedVR2BlockSwap、SeedVR2ExtraArgs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
