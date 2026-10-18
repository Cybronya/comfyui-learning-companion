---
key: 视频生成/图生视频/大丝袜ltx2.3卡通人物绝佳一致性_2071039400221433858.json
name: 大丝袜ltx2.3卡通人物绝佳一致性_2071039400221433858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/大丝袜ltx2.3卡通人物绝佳一致性_2071039400221433858.json
hash: abed1fad82ef08d6
coverage: 0.744186
learned_at: 2026-10-15 22:40:43
nodes: [RegexExtract, RegexExtract, PreviewAny, RH_Captioner, StringReplace, LayerUtility: ImageScaleByAspectRatio V2, EmptyLTXVLatentVideo, PreviewAny, PreviewAny, SetNode, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LTX2SamplingPreviewOverride, LTXVConditioning, KSamplerSelect, VisualizeSigmasKJ, BasicScheduler, ConditioningZeroOut, LTXVConcatAVLatent, LTXVImgToVideoInplaceKJ, GetNode, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, SetNode, LTXVPreprocess, LTXVEmptyLatentAudio, GetNode, PromptRelaySmartEncode, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, GetNode, GetNode, PreviewImage, Text, JWInteger, SamplerCustom, Text, VHS_VideoCombine, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/大丝袜ltx2.3卡通人物绝佳一致性_2071039400221433858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2071039400221433858.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `RegexExtract`
- `RegexExtract`
- `PreviewAny`
- `RH_Captioner`
- `StringReplace`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLTXVLatentVideo`
- `PreviewAny`
- `PreviewAny`
- `SetNode`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LTX2SamplingPreviewOverride`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `VisualizeSigmasKJ`
- `BasicScheduler`
- `ConditioningZeroOut`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `LTXVPreprocess`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `PromptRelaySmartEncode`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `PreviewImage`
- `Text`
- `JWInteger`
- `SamplerCustom` ★核心
- `Text`
- `VHS_VideoCombine`
- `LoadImage`
- `PreviewImage`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`RegexExtract`、`RH_Captioner`、`StringReplace`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`VAELoaderKJ`、`DualCLIPLoader`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`KSamplerSelect`、`VisualizeSigmasKJ`、`BasicScheduler`、`ConditioningZeroOut`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplaceKJ`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`PromptRelaySmartEncode`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`Text`、`JWInteger`、`SamplerCustom`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
