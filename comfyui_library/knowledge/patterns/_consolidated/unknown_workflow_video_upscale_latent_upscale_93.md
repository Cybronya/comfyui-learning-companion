---
name: unknown_workflow_video_upscale_latent_upscale_93
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.982
common_nodes: [1hew_AudioDuration, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, Float, Int, KSamplerSelect, LTXVAddGuide, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, ManualSigmas, RandomNoise, ResizeImageMaskNode, ResolutionSelector, SamplerCustomAdvanced, SetLatentNoiseMask, SimpleMath+, SolidMask, TrimAudio, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/ltx2.5_工作流全集_-1_2115619638640992257.json, 图片生成/图生图/ltx2.5_工作流全集_-1_2115667358995013633.json, 数字人/数字人/ltx2.5 工作流全集 -1_2114542977581408258.json, 视频生成/图生视频/ltx2.5_工作流全集_-1_2114876908914696193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_93

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/ltx2.5_工作流全集_-1_2115619638640992257.json、图片生成/图生图/ltx2.5_工作流全集_-1_2115667358995013633.json、数字人/数字人/ltx2.5 工作流全集 -1_2114542977581408258.json、视频生成/图生视频/ltx2.5_工作流全集_-1_2114876908914696193.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `1hew_AudioDuration`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `Float`
- `Int`
- `KSamplerSelect`
- `LTXVAddGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `TrimAudio`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
