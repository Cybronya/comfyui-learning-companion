---
name: unknown_workflow_video_upscale_latent_upscale_42
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.609667
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ExtendIntermediateSigmas, GetNode, JoinStringMulti, KSamplerSelect, LTX2AttentionTunerPatch, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3AVDecodeT8, MiniMaxH3HybridLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, PromptRelayEncode, PurgeVRAM_UTK, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, StringConcatenate, StringLength, StringSubstring, ToString, UNETLoader, VAEDecode, VAEEncode, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, string_util_StrFind]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3参考生视频-LTX2.5 MSR二采放大-音频参考-自动提示词优化-V1.1_2088533956374384642.json, 视频生成/图生视频/MiniMax_H3_+_LTX2.5_多参视频生成_2100857766603747330.json, 视频生成/图生视频/MiniMax_H3_+_LTX2.5_多参视频生成_2101128738648973314.json, 视频生成/图生视频/双剑合并 MiniMax H3 + LTX2.5 多参视频生成_2100072493146005505.json, 视频生成/图生视频/双剑合并_MiniMax_H3_+_LTX2.5_多参视频生成_2100190663353655298.json, 视频生成/图生视频/双剑合并_MiniMax_H3_+_LTX2.5_多参视频生成_2100922356238733313.json, 视频生成/图生视频/双剑合璧_MiniMax_H3_+_LTX2.5_多参视频生成_2105108981030146049.json, 视频生成/文生视频/(SBAPI)MiniMaxH3+LTX25多参视频(三分镜角色包匹配)_2104882747050389505.json, 视频生成/文生视频/双剑合璧 MiniMax H3 + LTX2.5 多参视频生成_2102770042948644866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_42

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3参考生视频-LTX2.5 MSR二采放大-音频参考-自动提示词优化-V1.1_2088533956374384642.json、视频生成/图生视频/MiniMax_H3_+_LTX2.5_多参视频生成_2100857766603747330.json、视频生成/图生视频/MiniMax_H3_+_LTX2.5_多参视频生成_2101128738648973314.json、视频生成/图生视频/双剑合并 MiniMax H3 + LTX2.5 多参视频生成_2100072493146005505.json、视频生成/图生视频/双剑合并_MiniMax_H3_+_LTX2.5_多参视频生成_2100190663353655298.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 9 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ExtendIntermediateSigmas`
- `GetNode`
- `JoinStringMulti`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3HybridLoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `PromptRelayEncode`
- `PurgeVRAM_UTK`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `StringConcatenate`
- `StringLength`
- `StringSubstring`
- `ToString`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `string_util_StrFind`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 8/9 个有
- `LTXAddVideoICLoRAGuide` —— 8/9 个有
- `LTXICLoRALoaderModelOnly` —— 8/9 个有
- `LiconMSR` —— 8/9 个有
- `EmptyImage` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `ComfyUILTX25MSRICLoRALoader` —— 1/9 个有
- `ComfyUILTX25MSRMultiReferenceGuide` —— 1/9 个有
- `DF_String_Concatenate` —— 1/9 个有
- `DF_Text_Box` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `H3SigmaRefiner` —— 1/9 个有
- `JWStringGetLine` —— 1/9 个有
- `JjkConcat` —— 1/9 个有
- `JjkShowText` —— 1/9 个有
- `LTXVDualCFGGuider` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `ReplaceString` —— 1/9 个有
- `StringConstant` —— 1/9 个有
- `easy promptReplace` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
