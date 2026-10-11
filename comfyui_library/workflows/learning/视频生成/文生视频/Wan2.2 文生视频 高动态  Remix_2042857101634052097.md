---
key: 视频生成/文生视频/Wan2.2 文生视频 高动态  Remix_2042857101634052097.json
name: Wan2.2 文生视频 高动态  Remix_2042857101634052097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频 高动态  Remix_2042857101634052097.json
hash: 0930339d0b2c19f4
coverage: 0.84375
learned_at: 2026-10-11 19:49:43
nodes: [RH_LLMAPI_NODE, easy showAnything, Wan22PromptSelector, RH_LLMAPI_NODE, CR Text Input Switch (4 way), Text Concatenate, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, WanImageToVideo, CLIPTextEncode, MathExpression|pysssss, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPLoader, VAELoader, KSamplerAdvanced, CLIPTextEncode, KSamplerAdvanced, VAEDecode, SeedVR2GGUF, SeedVR2ExtraArgs, SeedVR2BlockSwap, CR Text, JWInteger, JWInteger, JWInteger, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: [CR Text, CR Text Input Switch (4 way), MathExpression|pysssss, Text Concatenate]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2 文生视频 高动态  Remix_2042857101634052097.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频 高动态  Remix_2042857101634052097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（32 个）：
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `Wan22PromptSelector`
- `RH_LLMAPI_NODE`
- `CR Text Input Switch (4 way)`
- `Text Concatenate`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SeedVR2GGUF`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `CR Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`RH_LLMAPI_NODE`、`Wan22PromptSelector`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`WanImageToVideo`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`VAEDecode`、`SeedVR2GGUF`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`JWInteger`、`VHS_VideoCombine`

**缺卡**（4）：`CR Text`、`CR Text Input Switch (4 way)`、`MathExpression|pysssss`、`Text Concatenate`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SeedVR2BlockSwap、SeedVR2ExtraArgs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
