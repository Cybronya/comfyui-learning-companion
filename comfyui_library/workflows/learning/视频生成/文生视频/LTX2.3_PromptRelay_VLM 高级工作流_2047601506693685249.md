---
key: 视频生成/文生视频/LTX2.3_PromptRelay_VLM 高级工作流_2047601506693685249.json
name: LTX2.3_PromptRelay_VLM 高级工作流_2047601506693685249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3_PromptRelay_VLM 高级工作流_2047601506693685249.json
hash: 4c7fba3a1b0ee31f
coverage: 0.627907
learned_at: 2026-10-10 23:00:24
nodes: [GetNode, SetNode, SetNode, PreviewImage, GetNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PathchSageAttentionKJ, LTXVConditioning, LTX2SamplingPreviewOverride, GetNode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VAEDecode, SamplerCustom, MathExpression|pysssss, PrimitiveFloat, LTXVPreprocess, PrimitiveInt, KSamplerSelect, VisualizeSigmasKJ, BasicScheduler, PreviewImage, CR Float To Integer, PrimitiveInt, PrimitiveInt, GetNode, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LoadImage, ConditioningZeroOut, LTXVConcatAVLatent, VHS_VideoCombine, LTXVImgToVideoInplaceKJ, PrimitiveStringMultiline, StringReplace, ShowText|pysssss, AILab_QwenVL, PromptRelayEncode]
patterns: []
missing: [CR Float To Integer, MathExpression|pysssss]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 505}
discoveries: [次要节点 `CR Float To Integer` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3_PromptRelay_VLM 高级工作流_2047601506693685249.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3_PromptRelay_VLM 高级工作流_2047601506693685249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（43 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `PathchSageAttentionKJ`
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `LTXVPreprocess`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `VisualizeSigmasKJ`
- `BasicScheduler`
- `PreviewImage`
- `CR Float To Integer`
- `PrimitiveInt`
- `PrimitiveInt`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoadImage`
- `ConditioningZeroOut`
- `LTXVConcatAVLatent`
- `VHS_VideoCombine`
- `LTXVImgToVideoInplaceKJ`
- `PrimitiveStringMultiline`
- `StringReplace`
- `ShowText|pysssss`
- `AILab_QwenVL`
- `PromptRelayEncode`

## 关键参数

- `width` = `505`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **63%**（27/43）

**有卡**：`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`PathchSageAttentionKJ`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecode`、`SamplerCustom`、`LTXVPreprocess`、`KSamplerSelect`、`VisualizeSigmasKJ`、`BasicScheduler`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoaderKJ`、`LoadImage`、`ConditioningZeroOut`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`LTXVImgToVideoInplaceKJ`、`StringReplace`、`AILab_QwenVL`、`PromptRelayEncode`

**缺卡**（2）：`CR Float To Integer`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Float To Integer` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
