---
name: unknown_workflow_sampler_clip_unet_138
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.777222
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json, 视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json, 视频生成/图生视频/LTX2.5首尾帧_2087368525567582209.json, 视频生成/图生视频/LTX2.5首尾帧_2087526366265827329.json, 视频生成/图生视频/LTX2.5首尾帧_2088696578835046402.json, 视频生成/图生视频/LTX2.5首尾帧生视频2608_2095393045469556738.json, 视频生成/图生视频/LTX2_5_flf2v_2092797961985159170.json, 视频生成/图生视频/video_ltx2_5_flf2v_2087422059310833666.json, 视频生成/图生视频/【开源】LTX2.5 首尾帧生视频_2087467308766814210.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_138

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json、视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json、视频生成/图生视频/LTX2.5首尾帧_2087368525567582209.json、视频生成/图生视频/LTX2.5首尾帧_2087526366265827329.json、视频生成/图生视频/LTX2.5首尾帧_2088696578835046402.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVAddGuide` —— 8/9 个有
- `LTXVCropGuides` —— 8/9 个有
- `LTXVDualCFGGuider` —— 8/9 个有
- `ComfySwitchNode` —— 7/9 个有
- `GetImageSize` —— 7/9 个有
- `PrimitiveBoolean` —— 7/9 个有
- `SamplerEulerAncestral` —— 7/9 个有
- `TextGenerateLTX2Prompt` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `PreviewAny` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `DF_Get_image_size` —— 2/9 个有
- `Int` —— 2/9 个有
- `KSamplerSelect` —— 2/9 个有
- `LTXFloatToInt` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `PrimitiveFloat` —— 2/9 个有
- `CFGGuider` —— 1/9 个有
- `FlashVSRNode` —— 1/9 个有
- `LTXVImgToVideoInplace` —— 1/9 个有
- `ResolutionSelector` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `easy showAnything` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 9 | 90% |
| 高度 | 25 | 25 - 25 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，9 个样本，取值集中（一致性 90%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
