---
name: unknown_workflow_video_upscale_latent_upscale_67
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.705333
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LongTextToList, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, RegexExtract, SamplerCustomAdvanced, SetNode, ShowText|pysssss, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy convertAnything, easy indexAnything, easy positive, easy promptLine, easy promptReplace]
problems: []
missing: []
members: [视频生成/图生视频/2063165292641083394.json, 视频生成/图生视频/2062148904468172802.json, 视频生成/图生视频/2065558189625663489.json, 视频生成/图生视频/2064248566633295874.json, 视频生成/图生视频/2047853585928560641.json, 视频生成/图生视频/2047854322393817089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_67

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2063165292641083394.json、视频生成/图生视频/2062148904468172802.json、视频生成/图生视频/2065558189625663489.json、视频生成/图生视频/2064248566633295874.json、视频生成/图生视频/2047853585928560641.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LongTextToList`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RegexExtract`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy convertAnything`
- `easy indexAnything`
- `easy positive`
- `easy promptLine`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `ManualSigmas` —— 5/6 个有
- `ColorMatch` —— 4/6 个有
- `GetImageRangeFromBatch` —— 4/6 个有
- `GetImagesFromBatchIndexed` —— 4/6 个有
- `ImageBatchMulti` —— 4/6 个有
- `ImageInvert` —— 4/6 个有
- `LTXAddVideoICLoRAGuide` —— 4/6 个有
- `LTXICLoRALoaderModelOnly` —— 4/6 个有
- `LTXVAddGuideMulti` —— 4/6 个有
- `LiconMSR` —— 4/6 个有
- `PreviewAny` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `PrimitiveFloat` —— 4/6 个有
- `Text Concatenate` —— 4/6 个有
- `easy imageRemBg` —— 4/6 个有
- `easy mathString` —— 4/6 个有
- `easy promptConcat` —— 4/6 个有
- `easy promptList` —— 4/6 个有
- `easy seed` —— 4/6 个有
- `PrimitiveBoolean` —— 3/6 个有
- `BasicScheduler` —— 2/6 个有
- `Comfly_api_set` —— 2/6 个有
- `Comfly_gpt_image_2_official` —— 2/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `ImageFromBatch` —— 2/6 个有
- `LTXVEnhanceAVideoKJ` —— 2/6 个有
- `LTXVPreprocess` —— 2/6 个有
- `ResizeImageMaskNode` —— 2/6 个有
- `ResizeImagesByLongerEdge` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `easy ifElse` —— 2/6 个有
- `easy imageCount` —— 2/6 个有
- `easy imageInsetCrop` —— 2/6 个有
- `easy imageSplitGrid` —— 2/6 个有
- `easy lengthAnything` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `LTXVLatentUpsampler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 24 - 25 | 6 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，6 个样本，取值集中（一致性 98%）
