---
name: image_to_image_video_upscale_latent_upscale
type: Image To Image
frequency: 3
level: strong
coverage: 0.858667
common_nodes: [CFGGuider, CFGNorm, CLIPLoader, CLIPTextEncode, CM_FloatToInt, CM_IntToFloat, CR Prompt Text, CheckpointLoaderSimple, ConditioningZeroOut, DualCLIPLoaderGGUF, EmptyLTXVLatentVideo, FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, GetImageRangeFromBatch, GetImageSize, GetImageSize+, GetNode, GuiderParameters, INTConstant, ImageConcatMulti, ImagePadForOutpaint, ImageResizeKJv2, InsertImagesToBatchIndexed, KSampler, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultimodalGuider, PreviewImage, PrimitiveFloat, RandomNoise, RepeatImageBatch, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, SetNode, SigmasPreview, SimpleCalculatorKJ, SolidMask, TextEncodeQwenImageEditPlus, TrimAudioDuration, UnetLoaderGGUF, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/(自用-Aio V23 N+BFS Qwen 2511 )Ltx-2视频换脸V1_2019460055539654657.json, 视频生成/图生视频/Ltx-2视频换脸图生视频工作流_2037476698400231425.json, 视频生成/图生视频/（BFS Qwen2511版）Ltx-2视频换脸V1_2019457673309200386.json]
source: knowledge_consolidation
---

# image_to_image_video_upscale_latent_upscale

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/(自用-Aio V23 N+BFS Qwen 2511 )Ltx-2视频换脸V1_2019460055539654657.json、视频生成/图生视频/Ltx-2视频换脸图生视频工作流_2037476698400231425.json、视频生成/图生视频/（BFS Qwen2511版）Ltx-2视频换脸V1_2019457673309200386.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DualCLIPLoaderGGUF`
- `EmptyLTXVLatentVideo`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetImageSize+`
- `GetNode`
- `GuiderParameters`
- `INTConstant`
- `ImageConcatMulti`
- `ImagePadForOutpaint`
- `ImageResizeKJv2`
- `InsertImagesToBatchIndexed`
- `KSampler`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultimodalGuider`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `SetNode`
- `SigmasPreview`
- `SimpleCalculatorKJ`
- `SolidMask`
- `TextEncodeQwenImageEditPlus`
- `TrimAudioDuration`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `DuckHideNode` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `TT_img_enc` —— 1/3 个有
- `TT_img_enc_v2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
