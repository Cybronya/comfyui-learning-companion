---
key: 视频生成/文生视频/LTX2.3全自动_手动提示词 图生视频  低消耗 人物一致 精准版_2057632019441602562.json
name: LTX2.3全自动_手动提示词 图生视频  低消耗 人物一致 精准版_2057632019441602562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3全自动_手动提示词 图生视频  低消耗 人物一致 精准版_2057632019441602562.json
hash: 841068ef7713427b
coverage: 0.884615
learned_at: 2026-10-11 19:49:38
nodes: [KSamplerSelect, ModelPatchTorchSettings, RandomNoise, LTXVChunkFeedForward, RandomNoise, INTConstant, INTConstant, PrimitiveFloat, CFGGuider, KSamplerSelect, ManualSigmas, VAEDecodeTiled, INTConstant, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, CFGGuider, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVImgToVideoConditionOnly, ManualSigmas, LTXVAudioVAEDecode, LoraLoaderModelOnly, PathchSageAttentionKJ, CM_FloatToInt, LTXVPreprocess, LTXVAudioVAELoader, LatentUpscaleModelLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, EmptyLTXVLatentVideo, PrimitiveBoolean, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVConditioning, VHS_VideoCombine, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, LTXAVTextEncoderLoader, CR Text, CLIPTextEncode, Fast Groups Bypasser (rgthree), RH_LLMAPI_Pro_Node, PreviewAny, INTConstant, LoadImage]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3全自动_手动提示词 图生视频  低消耗 人物一致 精准版_2057632019441602562.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3全自动_手动提示词 图生视频  低消耗 人物一致 精准版_2057632019441602562.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（52 个）：
- `KSamplerSelect` ★核心
- `ModelPatchTorchSettings`
- `RandomNoise`
- `LTXVChunkFeedForward`
- `RandomNoise`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `INTConstant`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoConditionOnly`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CM_FloatToInt`
- `LTXVPreprocess`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXAVTextEncoderLoader`
- `CR Text`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `RH_LLMAPI_Pro_Node`
- `PreviewAny`
- `INTConstant`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **88%**（46/52）

**有卡**：`KSamplerSelect`、`ModelPatchTorchSettings`、`RandomNoise`、`LTXVChunkFeedForward`、`INTConstant`、`CFGGuider`、`ManualSigmas`、`VAEDecodeTiled`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LTXVImgToVideoConditionOnly`、`LTXVAudioVAEDecode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CM_FloatToInt`、`LTXVPreprocess`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`LTXVConditioning`、`VHS_VideoCombine`、`LTXAVTextEncoderLoader`、`RH_LLMAPI_Pro_Node`、`LoadImage`

**缺卡**（2）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
