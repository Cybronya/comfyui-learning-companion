---
key: 视频生成/图生视频/LTX2.3  sulphur 自用图生视频 15秒 台词自动生成绅士版_2059081258998784002.json
name: LTX2.3  sulphur 自用图生视频 15秒 台词自动生成绅士版_2059081258998784002.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2059081258998784002.json
hash: c4088f7c7ddacd2b
coverage: 0.918919
learned_at: 2026-10-15 22:38:36
nodes: [KSamplerSelect, LTXVConditioning, VisualizeSigmasKJ, UNETLoader, DualCLIPLoader, ConditioningZeroOut, VAELoaderKJ, VAEDecode, BasicScheduler, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoaderKJ, SamplerCustom, EmptyLTXVLatentVideo, LTX2SamplingPreviewOverride, VHS_VideoCombine, PromptRelaySmartEncode, LayerUtility: ImageScaleByAspectRatio V2, 孤海注释, CR Text, ImpactInt, SimpleMath+, CR Text, ShowText|pysssss, CR Text, MarkdownNote, Note Plus (mtb), LoadImage, Dapao_LlamaChat, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LTXVPreprocess, LTXVImgToVideoInplaceKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/LTX2.3  sulphur 自用图生视频 15秒 台词自动生成绅士版_2059081258998784002.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059081258998784002.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（37 个）：
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `VAELoaderKJ`
- `VAEDecode` ★核心
- `BasicScheduler`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAELoaderKJ`
- `SamplerCustom` ★核心
- `EmptyLTXVLatentVideo`
- `LTX2SamplingPreviewOverride`
- `VHS_VideoCombine`
- `PromptRelaySmartEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`
- `CR Text`
- `ImpactInt`
- `SimpleMath+`
- `CR Text`
- `ShowText|pysssss`
- `CR Text`
- `MarkdownNote`
- `Note Plus (mtb)`
- `LoadImage`
- `Dapao_LlamaChat`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXVPreprocess`
- `LTXVImgToVideoInplaceKJ`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`KSamplerSelect`、`LTXVConditioning`、`VisualizeSigmasKJ`、`UNETLoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`VAELoaderKJ`、`VAEDecode`、`BasicScheduler`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`SamplerCustom`、`EmptyLTXVLatentVideo`、`LTX2SamplingPreviewOverride`、`VHS_VideoCombine`、`PromptRelaySmartEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`ImpactInt`、`SimpleMath+`、`Note Plus (mtb)`、`LoadImage`、`Dapao_LlamaChat`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVPreprocess`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
