---
key: 视频生成/图生视频/Ltx2.3 Sulphur-2+Prompt Relay分段提示词微动作_2054758964251897857.json
name: Ltx2.3 Sulphur-2+Prompt Relay分段提示词微动作_2054758964251897857.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3 Sulphur-2+Prompt Relay分段提示词微动作_2054758964251897857.json
hash: 75ac7abedad770db
coverage: 0.780488
learned_at: 2026-10-15 22:37:51
nodes: [VAELoaderKJ, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, VHS_VideoCombine, VHS_VideoCombine, CR Prompt Text, Note, Note, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, VHS_VideoCombine, SamplerCustom, ConditioningZeroOut, VisualizeSigmasKJ, BasicScheduler, GetNode, VAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, PreviewImage, LTX2SamplingPreviewOverride, PromptRelaySmartEncode, LTXVConditioning, KSamplerSelect, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, GetNode, LoadImage, EmptyLTXVLatentVideo, GetNode, JWInteger]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3 Sulphur-2+Prompt Relay分段提示词微动作_2054758964251897857.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054758964251897857.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `VAELoaderKJ`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `Note`
- `Note`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `VHS_VideoCombine`
- `SamplerCustom` ★核心
- `ConditioningZeroOut`
- `VisualizeSigmasKJ`
- `BasicScheduler`
- `GetNode`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `PreviewImage`
- `LTX2SamplingPreviewOverride`
- `PromptRelaySmartEncode`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `LoadImage`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `JWInteger`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（32/41）

**有卡**：`VAELoaderKJ`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`SamplerCustom`、`ConditioningZeroOut`、`VisualizeSigmasKJ`、`BasicScheduler`、`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTX2SamplingPreviewOverride`、`PromptRelaySmartEncode`、`LTXVConditioning`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`EmptyLTXVLatentVideo`、`JWInteger`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
