---
name: unknown_workflow_upscale_sampler_unet_21
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8675
common_nodes: [ArgosTranslateTextNode, CR Text, ComfyNumberConvert, ComfySwitchNode, ConstrainImage|pysssss, CreateVideo, GetImageSize, GetVideoComponents, ImageResize+, ImageUpscaleWithModel, ImpactSwitch, InspyrenetRembg, Int, JoinImageWithAlpha, KSampler, LoadImage, PreviewImage, PrimitiveBoolean, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAFirstFrameCondition, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, ResizeImageMaskNode, SaveVideo, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SeedVR2TemporalChunk, SeedVR2TemporalMerge, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, Video Slice]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/MiniMax H3 首尾帧生视频_2084117471975526402.json, 视频生成/图生视频/MiniMax H3首帧视频_2084124493726965762.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 首尾帧生视频_2084117471975526402.json、视频生成/图生视频/MiniMax H3首帧视频_2084124493726965762.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `ArgosTranslateTextNode`
- `CR Text`
- `ComfyNumberConvert`
- `ComfySwitchNode`
- `ConstrainImage|pysssss`
- `CreateVideo`
- `GetImageSize`
- `GetVideoComponents`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `ImpactSwitch`
- `InspyrenetRembg`
- `Int`
- `JoinImageWithAlpha`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `PrimitiveBoolean`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3FL2VAEncode`
- `RHMiniMaxH3FL2VAFirstFrameCondition`
- `RHMiniMaxH3FL2VAModelLoader`
- `RHMiniMaxH3FL2VATarget`
- `RHMiniMaxH3FL2VATextEncoderLoader`
- `RHMiniMaxH3FL2VAVAELoader`
- `ResizeImageMaskNode`
- `SaveVideo`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SeedVR2TemporalChunk`
- `SeedVR2TemporalMerge`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `Video Slice`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
