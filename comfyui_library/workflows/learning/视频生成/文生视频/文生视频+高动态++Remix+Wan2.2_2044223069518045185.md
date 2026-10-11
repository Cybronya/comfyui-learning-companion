---
key: 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2044223069518045185.json
name: 文生视频+高动态++Remix+Wan2.2_2044223069518045185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2044223069518045185.json
hash: 34d20deb138dec62
coverage: 0.697674
learned_at: 2026-10-11 19:49:49
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, RIFE VFI, KSamplerAdvanced, WanImageToVideo, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, VAELoader, KSamplerAdvanced, PathchSageAttentionKJ, VHS_VideoCombine, JWInteger, GetNode, GetNode, CLIPLoader, Wan22PromptSelector, CLIPTextEncode, CLIPTextEncode, SetNode, RH_LLMAPI_NODE, easy showAnything, JWInteger, JWInteger, UNETLoader, UNETLoader, SetNode, SetNode, RH_LLMAPI_NODE, GetNode, Note, VAEDecode, CR Text Input Switch (4 way), Text Concatenate, wanBlockSwap, wanBlockSwap, ModelSamplingSD3, ModelSamplingSD3, CR Text]
patterns: []
missing: [CR Text, CR Text Input Switch (4 way), MathExpression|pysssss, RIFE VFI, Text Concatenate]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2044223069518045185.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2044223069518045185.json`

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
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `JWInteger`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `Wan22PromptSelector`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `JWInteger`
- `JWInteger`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `RH_LLMAPI_NODE`
- `GetNode`
- `Note`
- `VAEDecode` ★核心
- `CR Text Input Switch (4 way)`
- `Text Concatenate`
- `wanBlockSwap`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **70%**（30/43）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`VHS_VideoCombine`、`KSamplerAdvanced`、`WanImageToVideo`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`VAELoader`、`JWInteger`、`CLIPLoader`、`Wan22PromptSelector`、`CLIPTextEncode`、`RH_LLMAPI_NODE`、`UNETLoader`、`VAEDecode`、`wanBlockSwap`、`ModelSamplingSD3`

**缺卡**（5）：`CR Text`、`CR Text Input Switch (4 way)`、`MathExpression|pysssss`、`RIFE VFI`、`Text Concatenate`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SeedVR2BlockSwap、SeedVR2ExtraArgs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
