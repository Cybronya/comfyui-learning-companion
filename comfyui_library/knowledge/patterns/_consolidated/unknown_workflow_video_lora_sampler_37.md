---
name: unknown_workflow_video_lora_sampler_37
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.825696
common_nodes: [BasicScheduler, CLIPVisionLoader, ConditioningZeroOut, DrawViTPose, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, PreviewAny, PreviewImage, PromptRelayEncode, RegexExtract, SamplerCustom, SetNode, Text, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/2059924358973444098.json, 视频生成/图生视频/LTX+animate画质提升.图生视频_2102924118780895233.json, 视频生成/图生视频/LTX+animate画质提升1_2059941259988525057.json, 视频生成/图生视频/LTX+animate画质提升1_2104383276361281538.json, 视频生成/图生视频/LTX+animate画质提升1_2104756378995879937.json, 视频生成/图生视频/2070320545694052354.json, 视频生成/图生视频/服装模特图生视频_2064706422297944066.json, 视频生成/图生视频/2065030289491062785.json, 视频生成/图生视频/2061684800922144769.json, 视频生成/图生视频/2061696818274201601.json, 视频生成/图生视频/2061750723561480193.json, 视频生成/图生视频/2061756832443621377.json, 视频生成/图生视频/2061684766914727937.json, 视频生成/图生视频/2060377595157499905.json, 视频生成/图生视频/2060378166706921473.json, 视频生成/图生视频/2060476263445393409.json, 视频生成/图生视频/2061765735965356034.json, 视频生成/图生视频/2068868335923712001.json, 视频生成/图生视频/2068991926904377346.json, 视频生成/图生视频/2069004536680898562.json, 视频生成/图生视频/电商服装带货视频_2059941210411851777.json, 视频生成/图生视频/电商服装带货视频_2103296732867158018.json, 视频生成/文生视频/服装店带货视频生成【图生视频】_2064728584866066434.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/2059924358973444098.json、视频生成/图生视频/LTX+animate画质提升.图生视频_2102924118780895233.json、视频生成/图生视频/LTX+animate画质提升1_2059941259988525057.json、视频生成/图生视频/LTX+animate画质提升1_2104383276361281538.json、视频生成/图生视频/LTX+animate画质提升1_2104756378995879937.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicScheduler`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DrawViTPose`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `PreviewAny`
- `PreviewImage`
- `PromptRelayEncode`
- `RegexExtract`
- `SamplerCustom`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 16/23 个有
- `StringReplace` —— 16/23 个有
- `Int` —— 14/23 个有
- `EnhancedLoadDiffusionModel` —— 3/23 个有
- `ImagePadKJ` —— 3/23 个有
- `LoadAudio` —— 2/23 个有
- `CR Prompt Text` —— 1/23 个有
- `SaveImage` —— 1/23 个有
- `TT_img_enc` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 489 - 489 | 23 | 100% |
| 高度 | 24 | 24 - 24 | 23 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 489 - 489，23 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，23 个样本，取值集中（一致性 100%）
