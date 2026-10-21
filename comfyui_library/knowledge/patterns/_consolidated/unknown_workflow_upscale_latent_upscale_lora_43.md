---
name: unknown_workflow_upscale_latent_upscale_lora_43
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.901143
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/（生产环境）LTX2.3图生视频_2045796352663228418.json, 视频生成/图生视频/2010979976224448513.json, 视频生成/图生视频/2014646400780345345.json, 视频生成/图生视频/2073311336997675009.json, 视频生成/图生视频/2073311138300911617.json, 视频生成/图生视频/2011488577225494530.json, 视频生成/文生视频/LTX2.3数字人音频驱动视频生成_2031965741934714882.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_43

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/（生产环境）LTX2.3图生视频_2045796352663228418.json、视频生成/图生视频/2010979976224448513.json、视频生成/图生视频/2014646400780345345.json、视频生成/图生视频/2073311336997675009.json、视频生成/图生视频/2073311138300911617.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 6/7 个有
- `GetImageSize` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `ImageScaleBy` —— 6/7 个有
- `ManualSigmas` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `LTXVScheduler` —— 5/7 个有
- `LTXVAudioVAEEncode` —— 4/7 个有
- `LTXVEmptyLatentAudio` —— 4/7 个有
- `LoadAudio` —— 4/7 个有
- `MelBandRoFormerModelLoader` —— 4/7 个有
- `MelBandRoFormerSampler` —— 4/7 个有
- `SetLatentNoiseMask` —— 4/7 个有
- `SolidMask` —— 4/7 个有
- `TrimAudioDuration` —— 4/7 个有
- `VAEDecode` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `LTXVAudioVAEDecode` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `VAEDecodeTiled` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `GetNode` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `ComfyMathExpression` —— 1/7 个有
- `KSampler` —— 1/7 个有
- `PreviewAudio` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `ResizeImageMaskNode` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `SimpleCalculatorKJ` —— 1/7 个有
- `ToInt` —— 1/7 个有
- `easy int` —— 1/7 个有
- `easy mathInt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.35 | - | 1 | 100% |
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
