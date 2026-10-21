---
name: unknown_workflow_video_sampler_unet_20
type: Unknown Workflow
frequency: 16
level: weak
coverage: 0.766625
common_nodes: [ComfyMathExpression, DualCLIPLoader, EmptyImage, GetImagesFromBatchIndexed, GetNode, INTConstant, ImageAddMulti, ImageBatchMulti, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, RegexExtract, ResizeImageMaskNode, ResizeImagesByLongerEdge, SetNode, UNETLoader, VAELoaderKJ, VHS_VideoCombine, easy convertAnything, easy imageRemBg, easy indexAnything, easy positive, easy promptLine, easy promptList, easy promptReplace]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2039346074971807746.json, 视频生成/图生视频/2046808351366979586.json, 视频生成/图生视频/LTX2.3全栈式漫剧短剧生成（参考图生成版）图生视频漫剧短剧版短剧分镜版_2055237155726864386.json, 视频生成/图生视频/2046212690837774338.json, 视频生成/图生视频/2050042685750300673.json, 视频生成/图生视频/2052747730749009921.json, 视频生成/图生视频/2055880245324066818.json, 视频生成/图生视频/LTX2.3全栈式短剧生成V6（参考图生成版）图生视频短剧版短剧分镜版_2037962228107845633.json, 视频生成/图生视频/2037870072148008962.json, 视频生成/图生视频/2038288723439263746.json, 视频生成/图生视频/LTX2.3全栈式短剧生成V8（参考图生成版）图生视频短剧版短剧分镜版_2040445885619900417.json, 视频生成/图生视频/2064338058337673217.json, 视频生成/图生视频/2040059200792961026.json, 视频生成/图生视频/2038110146437586946.json, 视频生成/图生视频/LTX2.3全栈式短剧生成（参考图生成版）图生视频短剧版短剧分镜版_2044736578437783554.json, 视频生成/图生视频/2049005393069740034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_20

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/2039346074971807746.json、视频生成/图生视频/2046808351366979586.json、视频生成/图生视频/LTX2.3全栈式漫剧短剧生成（参考图生成版）图生视频漫剧短剧版短剧分镜版_2055237155726864386.json、视频生成/图生视频/2046212690837774338.json、视频生成/图生视频/2050042685750300673.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 16 个 workflow 都包含：
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyImage`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `INTConstant`
- `ImageAddMulti`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `UNETLoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy convertAnything`
- `easy imageRemBg`
- `easy indexAnything`
- `easy positive`
- `easy promptLine`
- `easy promptList`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 15/16 个有
- `CLIPTextEncode` —— 15/16 个有
- `EmptyLTXVLatentVideo` —— 15/16 个有
- `LatentUpscaleModelLoader` —— 15/16 个有
- `ManualSigmas` —— 15/16 个有
- `RandomNoise` —— 15/16 个有
- `SamplerCustomAdvanced` —— 15/16 个有
- `VAEDecodeTiled` —— 15/16 个有
- `PreviewImage` —— 14/16 个有
- `ShowText|pysssss` —— 14/16 个有
- `LTXVCropGuides` —— 13/16 个有
- `LTXVLatentUpsampler` —— 13/16 个有
- `LTXVImgToVideoInplace` —— 12/16 个有
- `LoraLoaderModelOnly` —— 12/16 个有
- `easy promptConcat` —— 12/16 个有
- `TrimVideoLatent` —— 11/16 个有
- `easy batchAnything` —— 11/16 个有
- `easy forLoopEnd` —— 11/16 个有
- `easy forLoopStart` —— 11/16 个有
- `LTXAddVideoICLoRAGuideAdvanced` —— 8/16 个有
- `LTXICLoRALoaderModelOnly` —— 8/16 个有
- `LTXVAddGuideMulti` —— 8/16 个有
- `LongTextToList` —— 7/16 个有
- `ImageInvert` —— 4/16 个有
- `LTXVEnhanceAVideoKJ` —— 4/16 个有
- `CLIPLoader` —— 2/16 个有
- `ModelSamplingSD3` —— 2/16 个有
- `VAEDecode` —— 2/16 个有
- `VAELoader` —— 2/16 个有
- `AudioEncoderEncode` —— 1/16 个有
- `AudioEncoderLoader` —— 1/16 个有
- `BasicScheduler` —— 1/16 个有
- `ColorMatch` —— 1/16 个有
- `ConditioningZeroOut` —— 1/16 个有
- `ContextWindowsManual` —— 1/16 个有
- `GetImageRangeFromBatch` —— 1/16 个有
- `KSampler` —— 1/16 个有
- `KSamplerAdvanced` —— 1/16 个有
- `LTXAddVideoICLoRAGuide` —— 1/16 个有
- `PreviewAny` —— 1/16 个有
- `PreviewAudio` —— 1/16 个有
- `PromptRelayEncode` —— 1/16 个有
- `RIFE VFI` —— 1/16 个有
- `RTXVideoSuperResolution` —— 1/16 个有
- `SamplerCustom` —— 1/16 个有
- `Text Concatenate` —— 1/16 个有
- `VAEEncode` —— 1/16 个有
- `WanHuMoImageToVideo` —— 1/16 个有
- `WanImageToVideo` —— 1/16 个有
- `WanVideoNAG` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 385 | 16 | 39% |
| 高度 | 25 | 24 - 25 | 16 | 99% |
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 385，16 个样本，取值分散，一致性仅 39%
- 高度 中位数 25，观测区间 24 - 25，16 个样本，取值集中（一致性 99%）
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 调度器 最常用 simple，2 个样本，一致性 50%
