---
name: unknown_workflow_video_upscale_latent_upscale_17
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.482467
common_nodes: [CFGGuider, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2062349602187210754.json, 视频生成/图生视频/2059029201776369665.json, 视频生成/图生视频/2059821367641600001.json, 视频生成/图生视频/2061007691652362242.json, 视频生成/图生视频/2054550329504608258.json, 视频生成/图生视频/2052700463136555010.json, 视频生成/图生视频/2062395094396919810.json, 视频生成/图生视频/2062346953803001857.json, 视频生成/图生视频/2053130511144497154.json, 视频生成/图生视频/2057471351287537666.json, 视频生成/图生视频/2057110543516921858.json, 视频生成/图生视频/2052419444986654721.json, 视频生成/图生视频/2052622530854301697.json, 视频生成/图生视频/2052685375168102401.json, 视频生成/文生视频/LTX23_5图生视频Gemini+VBVR+PromptRelay_2054601890872209409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_17

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/2062349602187210754.json、视频生成/图生视频/2059029201776369665.json、视频生成/图生视频/2059821367641600001.json、视频生成/图生视频/2061007691652362242.json、视频生成/图生视频/2054550329504608258.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGGuider`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PromptRelayEncodeTimeline` —— 13/15 个有
- `ResizeImagesByLongerEdge` —— 13/15 个有
- `CLIPTextEncode` —— 12/15 个有
- `LTXVEmptyLatentAudio` —— 12/15 个有
- `ResizeImageMaskNode` —— 12/15 个有
- `ComfySwitchNode` —— 10/15 个有
- `LTXVAudioVAEEncode` —— 10/15 个有
- `MelBandRoFormerModelLoader` —— 10/15 个有
- `MelBandRoFormerSampler` —— 10/15 个有
- `PrimitiveInt` —— 10/15 个有
- `SetLatentNoiseMask` —— 10/15 个有
- `SimpleCalculatorKJ` —— 10/15 个有
- `SolidMask` —— 10/15 个有
- `TrimAudioDuration` —— 10/15 个有
- `ConditioningZeroOut` —— 9/15 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 9/15 个有
- `LoadAudio` —— 9/15 个有
- `LoraLoaderModelOnly` —— 9/15 个有
- `PathchSageAttentionKJ` —— 9/15 个有
- `UNETLoader` —— 9/15 个有
- `CheckpointLoaderSimple` —— 6/15 个有
- `Int` —— 6/15 个有
- `LTX2AttentionTunerPatch` —— 6/15 个有
- `LTXVChunkFeedForward` —— 6/15 个有
- `LTXVScheduler` —— 6/15 个有
- `easy loraStack` —— 6/15 个有
- `easy loraStackApply` —— 6/15 个有
- `Fast Groups Muter (rgthree)` —— 5/15 个有
- `easy showAnything` —— 5/15 个有
- `ImageResizeKJv2` —— 2/15 个有
- `Label (rgthree)` —— 2/15 个有
- `PromptRelaySmartEncode` —— 2/15 个有
- `SimpleMath+` —— 2/15 个有
- `1hew_ImageGridSplit` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `JjkConcat` —— 1/15 个有
- `PreviewAudio` —— 1/15 个有
- `PreviewImage` —— 1/15 个有
- `PrimitiveBoolean` —— 1/15 个有
- `RH_LLMAPI_Pro_Node` —— 1/15 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/15 个有
- `ResizeImagesByShorterEdge` —— 1/15 个有
- `ResizeLongestToNode` —— 1/15 个有
- `TextBoxMira` —— 1/15 个有
- `VHS_LoadAudioUpload` —— 1/15 个有
- `easy ifElse` —— 1/15 个有
- `easy mathInt` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 339.5 | 193 - 649 | 12 | 72% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 339.5，观测区间 193 - 649，12 个样本
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
