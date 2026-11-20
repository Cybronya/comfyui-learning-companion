---
name: unknown_workflow_video_sampler_clip_150
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8195
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [图片生成/反推提示词/LTX2.3人物动作迁移V1_2031355634699997185.json, 平台全量/LTX2.3_自定义音频+人物动作迁移V3（单采IDLoRA）_2044017351640748034.json, 平台全量/LTX2.3_自定义音频+人物动作迁移V4（三采IDLoRA）_2044022005221036033.json, 视频生成/图生视频/LTX2.3人物动作迁移V2_2031367576470687746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_150

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/LTX2.3人物动作迁移V1_2031355634699997185.json、平台全量/LTX2.3_自定义音频+人物动作迁移V3（单采IDLoRA）_2044017351640748034.json、平台全量/LTX2.3_自定义音频+人物动作迁移V4（三采IDLoRA）_2044022005221036033.json、视频生成/图生视频/LTX2.3人物动作迁移V2_2031367576470687746.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 3/4 个有
- `LTXAddVideoICLoRAGuide` —— 3/4 个有
- `LTXICLoRALoaderModelOnly` —— 3/4 个有
- `LTXVImgToVideoConditionOnly` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `Qwen3ASRLoader` —— 3/4 个有
- `Qwen3ASRTranscribe` —— 3/4 个有
- `easy ifElse` —— 3/4 个有
- `easy imageSizeBySide` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `LTX2_NAG` —— 2/4 个有
- `LTXVEmptyLatentAudio` —— 2/4 个有
- `LTXVReferenceAudio` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `ResizeImagesByLongerEdge` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy convertAnything` —— 2/4 个有
- `easy downloadIndexTTSAndLoadModel` —— 2/4 个有
- `easy indexTTSEmotionAudio` —— 2/4 个有
- `easy indexTTSGenerateSimple` —— 2/4 个有
- `easy positive` —— 2/4 个有
- `easy promptReplace` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `LTXVAddGuideMulti` —— 1/4 个有
- `LTXVImgToVideoInplace` —— 1/4 个有
- `LTXVLatentUpsampler` —— 1/4 个有
- `LatentUpscaleModelLoader` —— 1/4 个有

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
