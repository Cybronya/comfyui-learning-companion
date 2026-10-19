---
name: unknown_workflow_video_upscale_latent_upscale_148
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8795
common_nodes: [CFGGuider, CLIPTextEncode, CR Value, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RH_LLMAPI_Pro_Node, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SimpleCalculatorKJ, String Literal, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/ltx2_i2v去蒸馏图到视频一致性60帧1080p_2019396485409939457.json, 视频生成/文生视频/ltx2_i2v蒸馏图到视频一致性60帧1080p_2019439198570287106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_148

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/ltx2_i2v去蒸馏图到视频一致性60帧1080p_2019396485409939457.json、视频生成/文生视频/ltx2_i2v蒸馏图到视频一致性60帧1080p_2019439198570287106.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Value`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SimpleCalculatorKJ`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `ImageLoader` —— 1/2 个有
- `LTXVScheduler` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
