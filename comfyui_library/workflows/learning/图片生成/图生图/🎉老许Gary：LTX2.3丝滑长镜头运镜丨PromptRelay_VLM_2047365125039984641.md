---
key: 图片生成/图生图/🎉老许Gary：LTX2.3丝滑长镜头运镜丨PromptRelay_VLM_2047365125039984641.json
name: 🎉老许Gary：LTX2.3丝滑长镜头运镜丨PromptRelay_VLM_2047365125039984641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🎉老许Gary：LTX2.3丝滑长镜头运镜丨PromptRelay_VLM_2047365125039984641.json
hash: 83522d4d68b9e982
coverage: 0.688889
learned_at: 2026-10-23 13:39:03
nodes: [GetNode, SetNode, SetNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, GetNode, PathchSageAttentionKJ, LTXVConditioning, LTX2SamplingPreviewOverride, ConditioningZeroOut, ShowText|pysssss, GetNode, LTXVSeparateAVLatent, SamplerCustom, VHS_VideoCombine, PrimitiveFloat, LTXVPreprocess, KSamplerSelect, VisualizeSigmasKJ, BasicScheduler, PreviewImage, CR Float To Integer, GetNode, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, PromptRelayEncode, StringReplace, AILab_QwenVL_Advanced, MathExpression|pysssss, LoadImage, CR Text, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, PrimitiveInt, PreviewImage, LTXVImgToVideoInplaceKJ, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 505}
---

# 图片生成/图生图/🎉老许Gary：LTX2.3丝滑长镜头运镜丨PromptRelay_VLM_2047365125039984641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🎉老许Gary：LTX2.3丝滑长镜头运镜丨PromptRelay_VLM_2047365125039984641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `ConditioningZeroOut`
- `ShowText|pysssss`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustom` ★核心
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `VisualizeSigmasKJ`
- `BasicScheduler`
- `PreviewImage`
- `CR Float To Integer`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `PromptRelayEncode`
- `StringReplace`
- `AILab_QwenVL_Advanced`
- `MathExpression|pysssss`
- `LoadImage`
- `CR Text`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PreviewImage`
- `LTXVImgToVideoInplaceKJ`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `505`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **69%**（31/45）

**有卡**：`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`ConditioningZeroOut`、`LTXVSeparateAVLatent`、`SamplerCustom`、`VHS_VideoCombine`、`LTXVPreprocess`、`KSamplerSelect`、`VisualizeSigmasKJ`、`BasicScheduler`、`CR Float To Integer`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoaderKJ`、`PromptRelayEncode`、`StringReplace`、`AILab_QwenVL_Advanced`、`MathExpression|pysssss`、`LoadImage`、`CR Text`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
