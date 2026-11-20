---
name: unknown_workflow_video_upscale_latent_upscale_67
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.584667
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/ltx2.3_无导演台-参考音频_纯参数_2085178800698118146.json, 视频生成/图生视频/ltx2.3_无导演台_纯参数_2076920722613686273.json, 视频生成/图生视频/ltx单视频_2061788937559040002.json, 视频生成/图生视频/四宫格_2050405484393447425.json, 视频生成/图生视频/小Seedance， 连环画视频，短视频 Ltx2.3 自带音效_2037892741253832706.json, 视频生成/图生视频/短剧制作，图生视频，四宫格+ Ltx2.3 Prompt Relay V3版本_2052550289055596546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_67

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/ltx2.3_无导演台-参考音频_纯参数_2085178800698118146.json、视频生成/图生视频/ltx2.3_无导演台_纯参数_2076920722613686273.json、视频生成/图生视频/ltx单视频_2061788937559040002.json、视频生成/图生视频/四宫格_2050405484393447425.json、视频生成/图生视频/小Seedance， 连环画视频，短视频 Ltx2.3 自带音效_2037892741253832706.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Float To Integer` —— 5/6 个有
- `LTXVEmptyLatentAudio` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `GuHaiAutoImageSplit` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `ImageFromBatch+` —— 4/6 个有
- `SimpleMath+` —— 4/6 个有
- `TTResolutionSelector` —— 4/6 个有
- `Text` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `Int` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `PromptRelayEncode` —— 3/6 个有
- `RH_LLMAPI_Pro_Node` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `BasicScheduler` —— 2/6 个有
- `Float` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `LTXVAudioVAEEncode` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `SetLatentNoiseMask` —— 2/6 个有
- `SolidMask` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `GetObjectFromJson` —— 1/6 个有
- `GetTextFromJson` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `LTXICLoRALoaderModelOnly` —— 1/6 个有
- `Light-Tool: DeserializeJsonString` —— 1/6 个有
- `PromptRelayEncodeTimeline` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `SaveVideoNode` —— 1/6 个有
- `TwoWaySwitch` —— 1/6 个有
- `easy indexAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
