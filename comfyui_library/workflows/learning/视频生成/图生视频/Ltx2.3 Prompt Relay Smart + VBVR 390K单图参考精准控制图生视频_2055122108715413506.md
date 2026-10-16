---
key: 视频生成/图生视频/Ltx2.3 Prompt Relay Smart + VBVR 390K单图参考精准控制图生视频_2055122108715413506.json
name: Ltx2.3 Prompt Relay Smart + VBVR 390K单图参考精准控制图生视频_2055122108715413506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2055122108715413506.json
hash: c97362b30cd70c0c
coverage: 0.756757
learned_at: 2026-10-15 22:37:54
nodes: [LTXVAudioVAEDecode, GetNode, SetNode, VisualizeSigmasKJ, LTX2SamplingPreviewOverride, PreviewImage, LTXVSeparateAVLatent, VAEDecode, VHS_VideoCombine, GetNode, SamplerCustom, LTXVConditioning, KSamplerSelect, ConditioningZeroOut, PathchSageAttentionKJ, BasicScheduler, LTXVConcatAVLatent, GetNode, GetNode, VAELoaderKJ, VAELoaderKJ, UNETLoader, DualCLIPLoader, LTXVImgToVideoInplaceKJ, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoraLoaderModelOnly, PromptRelaySmartEncode, LoadImage, CR Prompt Text, JWInteger, Note, CR Prompt Text, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3 Prompt Relay Smart + VBVR 390K单图参考精准控制图生视频_2055122108715413506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055122108715413506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `VisualizeSigmasKJ`
- `LTX2SamplingPreviewOverride`
- `PreviewImage`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `SamplerCustom` ★核心
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LTXVImgToVideoInplaceKJ`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `PromptRelaySmartEncode`
- `LoadImage`
- `CR Prompt Text`
- `JWInteger`
- `Note`
- `CR Prompt Text`
- `Note`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`LTXVAudioVAEDecode`、`VisualizeSigmasKJ`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`VHS_VideoCombine`、`SamplerCustom`、`LTXVConditioning`、`KSamplerSelect`、`ConditioningZeroOut`、`PathchSageAttentionKJ`、`BasicScheduler`、`LTXVConcatAVLatent`、`VAELoaderKJ`、`UNETLoader`、`DualCLIPLoader`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`PromptRelaySmartEncode`、`LoadImage`、`CR Prompt Text`、`JWInteger`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
