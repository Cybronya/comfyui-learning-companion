---
name: text_to_image_video_lora_sampler_110
type: Text To Image
frequency: 6
level: moderate
coverage: 0.672
common_nodes: [CFGGuider, CFGNorm, CLIPLoader, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, GetNode, INTConstant, KSampler, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, PrimitiveStringMultiline, RandomNoise, RegexExtract, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy indexAnything, easy positive, easy promptConcat, easy promptLine, easy promptReplace]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全栈式 短视频生成 简单上手效果好_2036074082332053505.json, 视频生成/图生视频/LTX2.3全栈式短剧生成V3（残血版）_2034616876847861762.json, 视频生成/图生视频/LTX2.3全栈式短剧生成V4（残血版）_2035986971947962370.json, 视频生成/图生视频/LTX2.3全栈式短剧生成V5（残血版）_2037414383898337282.json, 视频生成/图生视频/LTX2.3全栈式短视频生成V2.0_2033039341546639361.json, 视频生成/图生视频/LTX2.3全栈式短视频生成_2032623759688998914.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_110

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/全栈式 短视频生成 简单上手效果好_2036074082332053505.json、视频生成/图生视频/LTX2.3全栈式短剧生成V3（残血版）_2034616876847861762.json、视频生成/图生视频/LTX2.3全栈式短剧生成V4（残血版）_2035986971947962370.json、视频生成/图生视频/LTX2.3全栈式短剧生成V5（残血版）_2037414383898337282.json、视频生成/图生视频/LTX2.3全栈式短视频生成V2.0_2033039341546639361.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `GetNode`
- `INTConstant`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RegexExtract`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy indexAnything`
- `easy positive`
- `easy promptConcat`
- `easy promptLine`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 5/6 个有
- `LTXVCropGuides` —— 5/6 个有
- `LTXVLatentUpsampler` —— 5/6 个有
- `LatentUpscaleModelLoader` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `PrimitiveBoolean` —— 4/6 个有
- `RTXVideoSuperResolution` —— 4/6 个有
- `easy convertAnything` —— 4/6 个有
- `easy ifElse` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `DirectorAudioScriptLoader` —— 3/6 个有
- `DirectorCasting` —— 3/6 个有
- `DirectorSceneIterator` —— 3/6 个有
- `DirectorVideoPromptLoader` —— 3/6 个有
- `DirectorVisualStoryboardLoader` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `GetImagesFromBatchIndexed` —— 3/6 个有
- `ImageBatchMulti` —— 3/6 个有
- `JoinStringMulti` —— 3/6 个有
- `LTX2_NAG` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `PrimitiveInt` —— 3/6 个有
- `Text Concatenate` —— 3/6 个有
- `easy batchAnything` —— 3/6 个有
- `easy boolean` —— 3/6 个有
- `easy forLoopEnd` —— 3/6 个有
- `easy forLoopStart` —— 3/6 个有
- `easy mathString` —— 3/6 个有
- `easy promptList` —— 3/6 个有
- `llama_cpp_instruct_adv` —— 3/6 个有
- `llama_cpp_model_loader` —— 3/6 个有
- `DirectorOrderGate` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `Audio Duration (mtb)` —— 1/6 个有
- `DualCLIPLoaderGGUF` —— 1/6 个有
- `FB_Qwen3TTSDialogueInference` —— 1/6 个有
- `FB_Qwen3TTSRoleBank` —— 1/6 个有
- `FB_Qwen3TTSVoiceClonePrompt` —— 1/6 个有
- `LTXAddVideoICLoRAGuideAdvanced` —— 1/6 个有
- `LTXICLoRALoaderModelOnly` —— 1/6 个有
- `LTXVAudioVAEEncode` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `Qwen3ASRLoader` —— 1/6 个有
- `Qwen3ASRTranscribe` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `SetLatentNoiseMask` —— 1/6 个有
- `SolidMask` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `VRAM_Debug` —— 1/6 个有
- `easy lengthAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 97 - 1280 | 6 | 29% |
| 高度 | 616 | 25 - 720 | 6 | 31% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1.2 | 1.2 - 1.2 | 6 | 100% |
| 采样算法 | lcm | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 896，观测区间 97 - 1280，6 个样本，取值分散，一致性仅 29%
- 高度 中位数 616，观测区间 25 - 720，6 个样本，取值分散，一致性仅 31%
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.2，观测区间 1.2 - 1.2，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
