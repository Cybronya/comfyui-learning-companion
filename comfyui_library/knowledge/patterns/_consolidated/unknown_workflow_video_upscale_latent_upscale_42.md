---
name: unknown_workflow_video_upscale_latent_upscale_42
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.634556
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/video_ltx2_3_i2v_kijai_three_stage_2041087454286979073.json, 视频生成/图生视频/三图衔接视频生成_2066073219391643650.json, 视频生成/图生视频/图生视频 LTX2.3首尾帧+丝滑转场!加强版!_2041022779121733633.json, 视频生成/图生视频/图生视频plus版丝滑转场+反推提示词_2044978107093884930.json, 视频生成/图生视频/最新3.0首尾帧！首中尾3帧生成视频自动衔接_2065418792381014017.json, 视频生成/图生视频/最新LTX2.6首尾帧！首中尾3帧生成视频_2067259559454007298.json, 视频生成/图生视频/超好用🔥首中尾3帧生成视频-动漫-真人-各种场景_2066446454369112065.json, 视频生成/文生视频/LTX2.3图生视频 优化首尾帧Plus版 版 全自动提示词  丝滑转场 模块化调优版_2054366634822905858.json, 视频生成/文生视频/图生视频 LTX2.3首尾帧Plus版! 丝滑转场+反推提示词_2044281548878385153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_42

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/video_ltx2_3_i2v_kijai_three_stage_2041087454286979073.json、视频生成/图生视频/三图衔接视频生成_2066073219391643650.json、视频生成/图生视频/图生视频 LTX2.3首尾帧+丝滑转场!加强版!_2041022779121733633.json、视频生成/图生视频/图生视频plus版丝滑转场+反推提示词_2044978107093884930.json、视频生成/图生视频/最新3.0首尾帧！首中尾3帧生成视频自动衔接_2065418792381014017.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL_Advanced` —— 8/9 个有
- `Image Stitch` —— 8/9 个有
- `ImageScaleDownToSize` —— 8/9 个有
- `LTX2SamplingPreviewOverride` —— 8/9 个有
- `LTXVAddGuideMulti` —— 8/9 个有
- `LayerUtility: BooleanOperator` —— 8/9 个有
- `LayerUtility: If ` —— 8/9 个有
- `LayerUtility: PurgeVRAM` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `PrimitiveBoolean` —— 8/9 个有
- `SimpleMath+` —— 8/9 个有
- `easy positive` —— 8/9 个有
- `ShowText|pysssss` —— 7/9 个有
- `ResizeImageMaskNode` —— 4/9 个有
- `SaveImage` —— 3/9 个有
- `TT_img_enc` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `LoraLoader` —— 1/9 个有
- `PathchSageAttentionKJ` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `SDVN Load Image Url` —— 1/9 个有
- `String` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 25 - 25 | 9 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
