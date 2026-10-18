---
key: 视频生成/图生视频/Ltx2.3--Sulphur2--VBVR--图生视频_2055899428757753858.json
name: Ltx2.3--Sulphur2--VBVR--图生视频_2055899428757753858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3--Sulphur2--VBVR--图生视频_2055899428757753858.json
hash: 9b2a444ec9dfd0d4
coverage: 0.75
learned_at: 2026-10-15 22:37:59
nodes: [SetNode, VisualizeSigmasKJ, LTX2SamplingPreviewOverride, PreviewImage, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVConditioning, KSamplerSelect, ConditioningZeroOut, BasicScheduler, LTXVConcatAVLatent, GetNode, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, LTXVAudioVAEDecode, PromptRelaySmartEncode, PathchSageAttentionKJ, SamplerCustom, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, GetNode, LTXVImgToVideoInplaceKJ, LoadImage, Note, CR Prompt Text, Note, Note, CR Prompt Text, UNETLoader, JWInteger]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3--Sulphur2--VBVR--图生视频_2055899428757753858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055899428757753858.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `SetNode`
- `VisualizeSigmasKJ`
- `LTX2SamplingPreviewOverride`
- `PreviewImage`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `PromptRelaySmartEncode`
- `PathchSageAttentionKJ`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LoadImage`
- `Note`
- `CR Prompt Text`
- `Note`
- `Note`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `JWInteger`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（30/40）

**有卡**：`VisualizeSigmasKJ`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConditioning`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`LTXVConcatAVLatent`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVAudioVAEDecode`、`PromptRelaySmartEncode`、`PathchSageAttentionKJ`、`SamplerCustom`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`CR Prompt Text`、`UNETLoader`、`JWInteger`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
