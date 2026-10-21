---
name: unknown_workflow_upscale_latent_upscale_sampler_11
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.852667
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/ltx2.3 文生视频图生视频_2031751863044939777.json, 视频生成/图生视频/2032004087528562690.json, 视频生成/图生视频/2031685383376867330.json, 视频生成/图生视频/2031928343846723586.json, 视频生成/图生视频/2075950096994361345.json, 视频生成/图生视频/2031341831253925890.json, 视频生成/图生视频/2032121353918226434.json, 视频生成/图生视频/2054757610527707137.json, 视频生成/图生视频/2081658308183814145.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_11

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/ltx2.3 文生视频图生视频_2031751863044939777.json、视频生成/图生视频/2032004087528562690.json、视频生成/图生视频/2031685383376867330.json、视频生成/图生视频/2031928343846723586.json、视频生成/图生视频/2075950096994361345.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
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
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `ImageResizeKJv2` —— 7/9 个有
- `PrimitiveBoolean` —— 7/9 个有
- `ResizeImagesByLongerEdge` —— 7/9 个有
- `CheckpointLoaderSimple` —— 6/9 个有
- `Int` —— 6/9 个有
- `LTXAVTextEncoderLoader` —— 6/9 个有
- `LTXVAudioVAELoader` —— 6/9 个有
- `LTXVImgToVideoInplaceKJ` —— 5/9 个有
- `ResizeImageMaskNode` —— 5/9 个有
- `LTX2_NAG` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `LayerUtility: PurgeVRAM V2` —— 4/9 个有
- `DualCLIPLoader` —— 3/9 个有
- `UNETLoader` —— 3/9 个有
- `VAELoaderKJ` —— 3/9 个有
- `BasicScheduler` —— 2/9 个有
- `Float` —— 2/9 个有
- `LTXTiledSampler` —— 2/9 个有
- `LTXVFirstLastFrameControl_TTP` —— 2/9 个有
- `LTXVLatentUpsamplerTiled` —— 2/9 个有
- `LTXVMiddleFrame_TTP` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `ModelSamplingSD3` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `VisualizeSigmasKJ` —— 2/9 个有
- `easy mathInt` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `Text` —— 1/9 个有
- `Vignette` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 25 - 25 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
