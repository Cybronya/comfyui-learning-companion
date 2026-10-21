---
name: unknown_workflow_lora_sampler_clip_24
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7558
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveStringMultiline, PromptRelaySmartEncode, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecodeTiled, VAELoader, easy forLoopEnd, easy forLoopStart, easy ifElse, easy int, easy lengthAnything, easy timelineEditor, easy timelineInfoOutput, easy timelineSegmentOutput]
problems: []
missing: []
members: [视频生成/图生视频/2063654070711312385.json, 视频生成/图生视频/2079411345166004225.json, 视频生成/图生视频/2079411679590445058.json, 视频生成/图生视频/2054441916867063810.json, 视频生成/图生视频/2063617666866302978.json, 视频生成/图生视频/2064600495154618369.json, 视频生成/图生视频/2063620743581229058.json, 视频生成/图生视频/2068353923278270465.json, 视频生成/图生视频/2072320192541192193.json, 视频生成/图生视频/2076688851497742338.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2063654070711312385.json、视频生成/图生视频/2079411345166004225.json、视频生成/图生视频/2079411679590445058.json、视频生成/图生视频/2054441916867063810.json、视频生成/图生视频/2063617666866302978.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `PromptRelaySmartEncode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy int`
- `easy lengthAnything`
- `easy timelineEditor`
- `easy timelineInfoOutput`
- `easy timelineSegmentOutput`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 8/10 个有
- `LTXAddVideoICLoRAGuide` —— 8/10 个有
- `LTXVMakeRefVideo` —— 8/10 个有
- `PreviewAny` —— 8/10 个有
- `PrimitiveInt` —— 8/10 个有
- `SimpleMath+` —— 8/10 个有
- `StringReplace` —— 8/10 个有
- `easy batchAnything` —— 8/10 个有
- `easy compare` —— 8/10 个有
- `easy indexAnything` —— 8/10 个有
- `easy mergeVideosFromPaths` —— 8/10 个有
- `easy promptLine` —— 8/10 个有
- `easy saveVideo` —— 8/10 个有
- `easy string` —— 8/10 个有
- `easy timelineSegmentCount` —— 8/10 个有
- `LTX2SamplingPreviewOverride` —— 7/10 个有
- `VAELoaderKJ` —— 7/10 个有
- `1hew_MultiStringJoin` —— 6/10 个有
- `GetImageRangeFromBatch` —— 5/10 个有
- `LoadImage` —— 5/10 个有
- `easy makeImageList` —— 5/10 个有
- `Anything Everywhere` —— 3/10 个有
- `ComfyMathExpression` —— 3/10 个有
- `GetNode` —— 3/10 个有
- `LTXVChunkFeedForward` —— 3/10 个有
- `MelBandRoFormerModelLoader` —— 3/10 个有
- `MelBandRoFormerSampler` —— 3/10 个有
- `ModelPatchTorchSettings` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `LTX2_NAG` —— 2/10 个有
- `LTXFaceDetector` —— 2/10 个有
- `LTXLatentAnchorAware` —— 2/10 个有
- `LTXLikenessAnchor` —— 2/10 个有
- `LTXLikenessGuide` —— 2/10 个有
- `LTXTiledSampler` —— 2/10 个有
- `LTXVImgToVideoInplace` —— 2/10 个有
- `LTXVLatentUpsamplerTiled` —— 2/10 个有
- `LatentUpscaleModelLoader` —— 2/10 个有
- `LoadAudio` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `Text Concatenate` —— 2/10 个有
- `easy makeAudioList` —— 2/10 个有
- `Any Switch (rgthree)` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 24 | 24 - 24 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，10 个样本，取值集中（一致性 100%）
