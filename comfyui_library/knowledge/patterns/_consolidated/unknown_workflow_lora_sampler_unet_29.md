---
name: unknown_workflow_lora_sampler_unet_29
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.571
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyImage, GetImageSizeAndCount, GetNode, H3SigmaRefiner, JWFloatToString, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MemoryCleaner, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, PrimitiveFloat, ResolutionSelector, SaveVideo, SelfLiftAvatarH3Sampler, SetNode, StringFunction|pysssss, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy anythingIndexSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/视频-任意数量参考图(+上一镜头)生视频-Minnimax-H3-官方_2100599809924231170.json, 视频生成/图生视频/视频-任意数量参考生视频-Minnimax-H3-官方_2084309352525164546.json, 视频生成/图生视频/视频-参考图(+上一镜头)生视频-Minnimax-H3-官方_2100599796091416577.json, 视频生成/图生视频/视频-图生视频(+参考上一镜头)-Minnimax-H3-官方_2100602414704447490.json, 视频生成/图生视频/视频-音频歌曲MV-任意数量参考图(+上一镜头)生视频-Minnimax-H3-官方_2100599836948127746.json, 视频生成/图生视频/视频-音频歌曲MV-任意数量参考生视频-Minnimax-H3-官方_2093231781377040385.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_29

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/视频-任意数量参考图(+上一镜头)生视频-Minnimax-H3-官方_2100599809924231170.json、视频生成/图生视频/视频-任意数量参考生视频-Minnimax-H3-官方_2084309352525164546.json、视频生成/图生视频/视频-参考图(+上一镜头)生视频-Minnimax-H3-官方_2100599796091416577.json、视频生成/图生视频/视频-图生视频(+参考上一镜头)-Minnimax-H3-官方_2100602414704447490.json、视频生成/图生视频/视频-音频歌曲MV-任意数量参考图(+上一镜头)生视频-Minnimax-H3-官方_2100599836948127746.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `H3SigmaRefiner`
- `JWFloatToString`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftAvatarH3Sampler`
- `SetNode`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CM_IntUnaryOperation` —— 4/6 个有
- `FL_ImageBatchToGrid` —— 4/6 个有
- `GetVideoComponents` —— 4/6 个有
- `ImageBatchMulti` —— 4/6 个有
- `ImageFromBatch+` —— 4/6 个有
- `ImageLoader` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `ImpactFloat` —— 4/6 个有
- `LoadVideo` —— 4/6 个有
- `PreviewAny` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `RunningHub OmniShotCut Detector` —— 4/6 个有
- `RunningHub OmniShotCut Loader` —— 4/6 个有
- `RunningHub OmniShotCut SaveJson` —— 4/6 个有
- `RunningHub OmniShotCut ShotCount` —— 4/6 个有
- `RunningHub OmniShotCut VideoSplitter` —— 4/6 个有
- `SimpleMath+` —— 4/6 个有
- `Text` —— 4/6 个有
- `easy anythingInversedSwitch` —— 4/6 个有
- `easy batchAnything` —— 4/6 个有
- `easy forLoopEnd` —— 4/6 个有
- `easy forLoopStart` —— 4/6 个有
- `LTXVAudioVAEEncode` —— 2/6 个有
- `LTXVConcatAVLatent` —— 2/6 个有
- `LTXVSeparateAVLatent` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `Make Image Batch` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `Qwen3ASRLoader_DFT` —— 2/6 个有
- `Qwen3ASRTranscribe_DFT` —— 2/6 个有
- `Seed Everywhere` —— 2/6 个有
- `SetLatentNoiseMask` —— 2/6 个有
- `SolidMask` —— 2/6 个有
- `SoundFlow_GetLength` —— 2/6 个有
- `TrimAudioDuration` —— 2/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/6 个有
- `Int` —— 1/6 个有
- `MiniMaxH3ImageToVideo` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `Text Contains` —— 1/6 个有
- `Text Input Switch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
