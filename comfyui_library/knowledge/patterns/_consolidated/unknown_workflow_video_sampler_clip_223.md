---
name: unknown_workflow_video_sampler_clip_223
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9335
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAudio, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, ShowText|pysssss, SolidMask, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy cleanGpuUsed, easy convertAnything, easy downloadIndexTTSAndLoadModel, easy indexTTSEmotionAudio, easy indexTTSGenerateSimple, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/反推提示词/LTX2.3人物动作迁移V1_2031355634699997185.json, 视频生成/图生视频/LTX2.3人物动作迁移V2_2031367576470687746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_223

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/LTX2.3人物动作迁移V1_2031355634699997185.json、视频生成/图生视频/LTX2.3人物动作迁移V2_2031367576470687746.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTX2_NAG`
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
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSEmotionAudio`
- `easy indexTTSGenerateSimple`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/2 个有
- `LTXAddVideoICLoRAGuide` —— 1/2 个有
- `LTXICLoRALoaderModelOnly` —— 1/2 个有
- `LTXVAddGuideMulti` —— 1/2 个有
- `LTXVImgToVideoConditionOnly` —— 1/2 个有
- `Qwen3ASRLoader` —— 1/2 个有
- `Qwen3ASRTranscribe` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy imageSizeBySide` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
