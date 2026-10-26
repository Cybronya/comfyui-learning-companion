---
name: unknown_workflow_upscale_latent_upscale_lora_54
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.901333
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/（生产环境）LTX2.3图生视频_2045796352663228418.json, 视频生成/图生视频/20260113LTX2.0 图生视频工作流（48G）_2010979976224448513.json, 视频生成/图生视频/LTX+2.0+音画同步-数字人，唱歌_2014646400780345345.json, 视频生成/图生视频/LTX-2 数字人对口型720P_2073311336997675009.json, 视频生成/图生视频/LTX-2 数字人对口型蒸馏版1080P_2073311138300911617.json, 视频生成/文生视频/LTX2.3数字人音频驱动视频生成_2031965741934714882.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_54

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/（生产环境）LTX2.3图生视频_2045796352663228418.json、视频生成/图生视频/20260113LTX2.0 图生视频工作流（48G）_2010979976224448513.json、视频生成/图生视频/LTX+2.0+音画同步-数字人，唱歌_2014646400780345345.json、视频生成/图生视频/LTX-2 数字人对口型720P_2073311336997675009.json、视频生成/图生视频/LTX-2 数字人对口型蒸馏版1080P_2073311138300911617.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
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
- `EmptyImage` —— 5/6 个有
- `GetImageSize` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `ImageScaleBy` —— 5/6 个有
- `ManualSigmas` —— 5/6 个有
- `PrimitiveInt` —— 5/6 个有
- `LTXVAudioVAEEncode` —— 4/6 个有
- `LTXVScheduler` —— 4/6 个有
- `LoadAudio` —— 4/6 个有
- `MelBandRoFormerModelLoader` —— 4/6 个有
- `MelBandRoFormerSampler` —— 4/6 个有
- `SetLatentNoiseMask` —— 4/6 个有
- `SolidMask` —— 4/6 个有
- `TrimAudioDuration` —— 4/6 个有
- `CreateVideo` —— 3/6 个有
- `LTXVEmptyLatentAudio` —— 3/6 个有
- `SaveVideo` —— 3/6 个有
- `VAEDecode` —— 3/6 个有
- `VAEDecodeTiled` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `LTXVAudioVAEDecode` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `PrimitiveFloat` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `ComfyMathExpression` —— 1/6 个有
- `KSampler` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `ResizeImageMaskNode` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `SimpleCalculatorKJ` —— 1/6 个有
- `ToInt` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy mathInt` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.35 | - | 1 | 100% |
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
