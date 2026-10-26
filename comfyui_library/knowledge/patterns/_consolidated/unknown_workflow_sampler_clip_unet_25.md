---
name: unknown_workflow_sampler_clip_unet_25
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.801522
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json, 视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json, 视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json, 视频生成/图生视频/LTX2.5图生视频2608_2095393021843038209.json, 视频生成/图生视频/LTX2.5图生视频_2087332188219068417.json, 视频生成/图生视频/LTX2.5图生视频_2087422859705667585.json, 视频生成/图生视频/LTX2.5图生视频_2087443699126071298.json, 视频生成/图生视频/LTX2.5图生视频_2087526346007339010.json, 视频生成/图生视频/LTX2.5图生视频_2088701698968743938.json, 视频生成/图生视频/LTX2.5图生视频_2089721005475459074.json, 视频生成/图生视频/LTX2.5图生视频_2090891877334736897.json, 视频生成/图生视频/LTX2.5首尾帧_2087368525567582209.json, 视频生成/图生视频/LTX2.5首尾帧_2087526366265827329.json, 视频生成/图生视频/LTX2.5首尾帧_2088696578835046402.json, 视频生成/图生视频/LTX2.5首尾帧生视频2608_2095393045469556738.json, 视频生成/图生视频/LTX2_5_flf2v_2092797961985159170.json, 视频生成/图生视频/video_ltx2_5_flf2v_2087422059310833666.json, 视频生成/文生视频/LTX 2.5 文生视频版_2094317793788383233.json, 视频生成/文生视频/LTX 2.5 首尾帧视频生成_2087469648844513282.json, 视频生成/文生视频/LTX2.5  图生视频 二采高清_2100577700896399362.json, 视频生成/文生视频/LTX2.5 图生视频 视频生成  二次采样_2092076309282381825.json, 视频生成/文生视频/LTX2.5 图生视频 视频生成  二次采样_2092080533667926017.json, 视频生成/文生视频/图生视频 文生视频 首尾帧 极速 LTX2.5全家桶 音画同出_2087552830658924545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json、视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json、视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json、视频生成/图生视频/LTX2.5图生视频2608_2095393021843038209.json、视频生成/图生视频/LTX2.5图生视频_2087332188219068417.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVDualCFGGuider` —— 22/23 个有
- `LTXVPreprocess` —— 22/23 个有
- `LoadImage` —— 22/23 个有
- `PrimitiveInt` —— 22/23 个有
- `ResizeImageMaskNode` —— 22/23 个有
- `PrimitiveBoolean` —— 21/23 个有
- `ComfySwitchNode` —— 20/23 个有
- `TextGenerateLTX2Prompt` —— 20/23 个有
- `PreviewAny` —— 18/23 个有
- `CreateVideo` —— 16/23 个有
- `KSamplerSelect` —— 16/23 个有
- `SaveVideo` —— 16/23 个有
- `LTXVImgToVideoInplace` —— 14/23 个有
- `LTXVLatentUpsampler` —— 14/23 个有
- `LatentUpscaleModelLoader` —— 14/23 个有
- `ResolutionSelector` —— 13/23 个有
- `GetImageSize` —— 9/23 个有
- `LTXVAddGuide` —— 9/23 个有
- `LTXVCropGuides` —— 9/23 个有
- `SamplerEulerAncestral` —— 8/23 个有
- `VHS_VideoCombine` —— 7/23 个有
- `孤海注释` —— 4/23 个有
- `Int` —— 3/23 个有
- `PurgeVRAM_UTK` —— 3/23 个有
- `DF_Get_image_size` —— 2/23 个有
- `FlashVSRNode` —— 2/23 个有
- `LTXFloatToInt` —— 2/23 个有
- `PreviewImage` —— 2/23 个有
- `PrimitiveFloat` —— 2/23 个有
- `CFGGuider` —— 1/23 个有
- `Fast Groups Bypasser (rgthree)` —— 1/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 23 | 93% |
| 高度 | 25 | 25 - 25 | 23 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，23 个样本，取值集中（一致性 93%）
- 高度 中位数 25，观测区间 25 - 25，23 个样本，取值集中（一致性 100%）
