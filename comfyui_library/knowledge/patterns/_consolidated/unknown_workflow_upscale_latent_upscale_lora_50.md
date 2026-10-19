---
name: unknown_workflow_upscale_latent_upscale_lora_50
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.699
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, ComfyMathExpression, EmptyLTXVLatentVideo, JoinStrings, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, MemoryCleaner, PrimitiveFloat, Qwen3_VQA, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SeedGenerator, ShowText|pysssss, SimpleCalculatorKJ, VAEDecodeTiled, easy cleanGpuUsed, easy showAnything, ttN concat]
problems: []
missing: []
members: [视频生成/图生视频/2049390145010409474.json, 视频生成/图生视频/2052747841218596866.json, 视频生成/图生视频/2044451540315938817.json, 视频生成/文生视频/LTX 2.3 复杂动作版｜文生视频 & 图生视频 ｜V1.1版（人脸一致性）+ VBVR 理解复杂_2044309375526899714.json, 视频生成/文生视频/图生视频 & 文生视频｜+ HDR + 工业级自动调色（避免死黑过曝）｜LTX2.3_2047750461792460802.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_50

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2049390145010409474.json、视频生成/图生视频/2052747841218596866.json、视频生成/图生视频/2044451540315938817.json、视频生成/文生视频/LTX 2.3 复杂动作版｜文生视频 & 图生视频 ｜V1.1版（人脸一致性）+ VBVR 理解复杂_2044309375526899714.json、视频生成/文生视频/图生视频 & 文生视频｜+ HDR + 工业级自动调色（避免死黑过曝）｜LTX2.3_2047750461792460802.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `JoinStrings`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MemoryCleaner`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SeedGenerator`
- `ShowText|pysssss`
- `SimpleCalculatorKJ`
- `VAEDecodeTiled`
- `easy cleanGpuUsed`
- `easy showAnything`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 4/5 个有
- `CreateVideo` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `LTXAVTextEncoderLoader` —— 4/5 个有
- `LTXVAudioVAELoader` —— 4/5 个有
- `LTXVCropGuides` —— 4/5 个有
- `LTXVImgToVideoInplace` —— 4/5 个有
- `CM_FloatToInt` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `LTXVChunkFeedForward` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `ModelPatchTorchSettings` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `ImageLoader` —— 2/5 个有
- `ImageStitch` —— 2/5 个有
- `LTXVImgToVideoInplaceKJ` —— 2/5 个有
- `PrimitiveBoolean` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `PromptRelayEncode` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `Image Levels Adjustment` —— 1/5 个有
- `ImageSharpen` —— 1/5 个有
- `LTX2SamplingPreviewOverride` —— 1/5 个有
- `LTXVAddGuideMulti` —— 1/5 个有
- `LTXVEnhanceAVideoKJ` —— 1/5 个有
- `LTXVHDRDecodePostprocess` —— 1/5 个有
- `LTXVImgToVideoConditionOnly` —— 1/5 个有
- `MultiplePathsInput` —— 1/5 个有
- `ResizeImageMaskNode` —— 1/5 个有
- `UNETLoader` —— 1/5 个有
- `VAELoaderKJ` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

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
