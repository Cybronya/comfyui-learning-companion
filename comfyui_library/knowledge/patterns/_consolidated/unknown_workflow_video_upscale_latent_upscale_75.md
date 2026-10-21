---
name: unknown_workflow_video_upscale_latent_upscale_75
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5552
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, ImageScaleBy, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2038845720425402369.json, 视频生成/图生视频/2045564251896553474.json, 视频生成/图生视频/2038864903368347650.json, 视频生成/图生视频/2040980266277146625.json, 视频生成/图生视频/2046788191067312129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_75

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2038845720425402369.json、视频生成/图生视频/2045564251896553474.json、视频生成/图生视频/2038864903368347650.json、视频生成/图生视频/2040980266277146625.json、视频生成/图生视频/2046788191067312129.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVScheduler` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `Seed (rgthree)` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `easy promptConcat` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `RunningHub SeedXPro Translator` —— 2/5 个有
- `easy positive` —— 2/5 个有
- `Any To String (mtb)` —— 1/5 个有
- `FromListGet1Int` —— 1/5 个有
- `GuHaiAutoImageSplit` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `RegexExtract` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有
- `TextBox1` —— 1/5 个有
- `TextGenerateLTX2Prompt` —— 1/5 个有
- `TextListSplit` —— 1/5 个有
- `easy convertAnything` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

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
