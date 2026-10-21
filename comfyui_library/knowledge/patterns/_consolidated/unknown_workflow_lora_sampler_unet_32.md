---
name: unknown_workflow_lora_sampler_unet_32
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.83
common_nodes: [AudioConcat, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetImageRangeFromBatch, GetVideoComponents, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3BlockCacheT8, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SpectrumApplyMiniMaxH3, Text Multiline, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy batchAnything]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 fl2v无限长视频_2087006461363843073.json, 视频生成/图生视频/MiniMax-H3 fl2v视频扩展_2086765853382627330.json, 视频生成/图生视频/MiniMax-H3 ref2v无限长视频_2090036967839981569.json, 视频生成/图生视频/MiniMax-H3 无限长视频 提示词优化_2087038665250922498.json, 视频生成/图生视频/MiniMax-H3 无限长视频生成+二采放大_2094089704038821890.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_32

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 fl2v无限长视频_2087006461363843073.json、视频生成/图生视频/MiniMax-H3 fl2v视频扩展_2086765853382627330.json、视频生成/图生视频/MiniMax-H3 ref2v无限长视频_2090036967839981569.json、视频生成/图生视频/MiniMax-H3 无限长视频 提示词优化_2087038665250922498.json、视频生成/图生视频/MiniMax-H3 无限长视频生成+二采放大_2094089704038821890.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioConcat`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetImageRangeFromBatch`
- `GetVideoComponents`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3BlockCacheT8`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SpectrumApplyMiniMaxH3`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy batchAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `LongTextToList` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `SDVN Any Show` —— 4/5 个有
- `String Replace (mtb)` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `easy forLoopEnd` —— 4/5 个有
- `easy forLoopStart` —— 4/5 个有
- `string_util_StrLen` —— 4/5 个有
- `AnySwitch` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `Multi Text Merge` —— 3/5 个有
- `TTP_text_mix` —— 3/5 个有
- `AILab_QwenVL` —— 2/5 个有
- `MiniMaxH3MotionContextSaveLatent` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `LTXVConcatAVLatent` —— 1/5 个有
- `LTXVSeparateAVLatent` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `LoadVideo` —— 1/5 个有
- `ManualSigmas` —— 1/5 个有
- `MiniMaxH3ChainContext` —— 1/5 个有
- `MiniMaxH3ChainExternalVideo` —— 1/5 个有
- `MinimaxH3LatentUpscaler3D` —— 1/5 个有
- `Qwen3VL_Advanced` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有
- `Video Slice` —— 1/5 个有
- `Yuan_H3MotionContext` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
