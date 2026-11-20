---
name: unknown_workflow_video_upscale_latent_upscale_113
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.873
common_nodes: [AILab_QwenVL, AudioTrim, BasicScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, ImpactInt, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PathchSageAttentionKJ, PreviewAudio, PrimitiveStringMultiline, RHHiddenNodes, RandomNoise, RunningHub Deepcleaner, SamplerCustomAdvanced, SetLatentNoiseMask, ShowText|pysssss, SolidMask, VAEDecodeTiled, VHS_VideoCombine, ttN text7BOX_concat]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/LTX2.3数字人工作流_2084560796100681730.json, 视频生成/图生视频/[🛫书墨]ltx2.3音频驱动图转视频(无字幕)—synvow书墨-建议plus运行_2034829717416714242.json, 视频生成/图生视频/ltx2.3音频驱动图转视频_2036704302705680386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_113

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3数字人工作流_2084560796100681730.json、视频生成/图生视频/[🛫书墨]ltx2.3音频驱动图转视频(无字幕)—synvow书墨-建议plus运行_2034829717416714242.json、视频生成/图生视频/ltx2.3音频驱动图转视频_2036704302705680386.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `AudioTrim`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `ImpactInt`
- `KSampler`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `RandomNoise`
- `RunningHub Deepcleaner`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `ttN text7BOX_concat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
