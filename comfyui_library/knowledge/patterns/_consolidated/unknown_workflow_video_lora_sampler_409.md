---
name: unknown_workflow_video_lora_sampler_409
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.932333
common_nodes: [BasicScheduler, CR Text, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, ImpactInt, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SimpleMath+, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3  sulphur 自用图生视频 15秒 台词自动生成绅士版_2059081258998784002.json, 视频生成/图生视频/LTX2.3  sulphur 自用图生视频 15秒 台词自动生成绅士版_2080902822853435394.json, 视频生成/图生视频/LTX2.3-10Eros 图生视频-台词自动生成_2077018841644888066.json, 视频生成/图生视频/LTX2.3-10Eros 图生视频-台词自动生成【syqiangk】_2067970994802872322.json, 视频生成/图生视频/LTX2.3图生视频_2078005941840207873.json, 视频生成/图生视频/新玩意LTX2.3+sulphur 图生视频_2059322431231324161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_409

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/LTX2.3  sulphur 自用图生视频 15秒 台词自动生成绅士版_2059081258998784002.json、视频生成/图生视频/LTX2.3  sulphur 自用图生视频 15秒 台词自动生成绅士版_2080902822853435394.json、视频生成/图生视频/LTX2.3-10Eros 图生视频-台词自动生成_2077018841644888066.json、视频生成/图生视频/LTX2.3-10Eros 图生视频-台词自动生成【syqiangk】_2067970994802872322.json、视频生成/图生视频/LTX2.3图生视频_2078005941840207873.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImpactInt`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `PromptRelaySmartEncode` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `Dapao_LlamaChat` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `LoaderGGUF` —— 2/6 个有
- `CLIPTextEncode` —— 1/6 个有
- `CR Text Replace` —— 1/6 个有
- `Fast Bypasser (rgthree)` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `easy convertAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 489 - 489 | 6 | 100% |
| 高度 | 25 | 24 - 25 | 6 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 489 - 489，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，6 个样本，取值集中（一致性 98%）
