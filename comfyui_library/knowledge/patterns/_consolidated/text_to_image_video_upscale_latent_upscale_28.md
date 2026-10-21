---
name: text_to_image_video_upscale_latent_upscale_28
type: Text To Image
frequency: 2
level: weak
coverage: 0.593
common_nodes: [CFGGuider, CFGNorm, CLIPLoader, CLIPTextEncode, CR Text, ComfyMathExpression, DirectorAudioScriptLoader, DirectorCasting, DirectorSceneIterator, DirectorVideoPromptLoader, DirectorVisualStoryboardLoader, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, INTConstant, JoinStringMulti, KSampler, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, PrimitiveStringMultiline, RTXVideoSuperResolution, RandomNoise, RegexExtract, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, Text Concatenate, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy boolean, easy ifElse, easy indexAnything, easy positive, easy promptConcat, easy promptLine, easy promptReplace, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2033039341546639361.json, 视频生成/图生视频/2032623759688998914.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2033039341546639361.json、视频生成/图生视频/2032623759688998914.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ComfyMathExpression`
- `DirectorAudioScriptLoader`
- `DirectorCasting`
- `DirectorSceneIterator`
- `DirectorVideoPromptLoader`
- `DirectorVisualStoryboardLoader`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `JoinStringMulti`
- `KSampler`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `RegexExtract`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy boolean`
- `easy ifElse`
- `easy indexAnything`
- `easy positive`
- `easy promptConcat`
- `easy promptLine`
- `easy promptReplace`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 1/2 个有
- `DirectorOrderGate` —— 1/2 个有
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `FB_Qwen3TTSDialogueInference` —— 1/2 个有
- `FB_Qwen3TTSRoleBank` —— 1/2 个有
- `FB_Qwen3TTSVoiceClonePrompt` —— 1/2 个有
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `Qwen3ASRLoader` —— 1/2 个有
- `Qwen3ASRTranscribe` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `VRAM_Debug` —— 1/2 个有
- `easy convertAnything` —— 1/2 个有
- `easy mathString` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 304.5 | - | 2 | 32% |
| 高度 | 268.5 | - | 2 | 9% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.2 | - | 2 | 100% |
| 采样算法 | lcm | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 304.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 32%
- 高度 中位数 268.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 9%
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
