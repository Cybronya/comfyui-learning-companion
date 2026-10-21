---
name: text_to_image_lora_sampler_clip_327
type: Text To Image
frequency: 3
level: strong
coverage: 0.542333
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CM_IntUnaryOperation, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyImage, EmptyLatentImage, GetImageSizeAndCount, GetNode, H3SigmaRefiner, ImageLoader, ImageResizeKJv2, ImpactFloat, JWFloatToString, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MemoryCleaner, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, PreviewAudio, PrimitiveFloat, Qwen3ASRLoader_DFT, Qwen3ASRTranscribe_DFT, ResolutionSelector, SaveVideo, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, SoundFlow_GetLength, StringFunction|pysssss, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VRGDG_MiniMaxH3AudioDrive, easy anythingIndexSwitch, easy anythingInversedSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/音频歌曲MV参考生视频官方版｜任意数量参考Minnimax-H3_2101154129300254722.json, 视频生成/图生视频/音频歌曲MV多参考生视频MiniMax H3处理生成工具_2101361082567843841.json, 视频生成/图生视频/音频歌曲MV生视频官方版｜任意数量参考图加上一镜头Minnimax-H3_2101175084877705218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_327

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/音频歌曲MV参考生视频官方版｜任意数量参考Minnimax-H3_2101154129300254722.json、视频生成/图生视频/音频歌曲MV多参考生视频MiniMax H3处理生成工具_2101361082567843841.json、视频生成/图生视频/音频歌曲MV生视频官方版｜任意数量参考图加上一镜头Minnimax-H3_2101175084877705218.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_IntUnaryOperation`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyImage`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `GetNode`
- `H3SigmaRefiner`
- `ImageLoader`
- `ImageResizeKJv2`
- `ImpactFloat`
- `JWFloatToString`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `PreviewAudio`
- `PrimitiveFloat`
- `Qwen3ASRLoader_DFT`
- `Qwen3ASRTranscribe_DFT`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `SoundFlow_GetLength`
- `StringFunction|pysssss`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VRGDG_MiniMaxH3AudioDrive`
- `easy anythingIndexSwitch`
- `easy anythingInversedSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Make Image Batch` —— 2/3 个有
- `FL_ImageBatchToGrid` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RunningHub OmniShotCut Detector` —— 1/3 个有
- `RunningHub OmniShotCut Loader` —— 1/3 个有
- `RunningHub OmniShotCut SaveJson` —— 1/3 个有
- `RunningHub OmniShotCut ShotCount` —— 1/3 个有
- `RunningHub OmniShotCut VideoSplitter` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
