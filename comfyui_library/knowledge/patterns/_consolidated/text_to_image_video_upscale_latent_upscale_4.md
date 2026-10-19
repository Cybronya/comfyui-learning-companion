---
name: text_to_image_video_upscale_latent_upscale_4
type: Text To Image
frequency: 16
level: strong
coverage: 0.667938
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, ExtendIntermediateSigmas, GetNode, JjkText, JoinStringMulti, KSampler, KSamplerSelect, LTX2AttentionTunerPatch, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3AVDecodeT8, MiniMaxH3HybridLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, PromptRelayEncode, PurgeVRAM_UTK, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, StringConcatenate, StringLength, StringSubstring, ToString, UNETLoader, VAEDecode, VAEEncode, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, string_util_StrFind]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3加LTX2.5多参视频生成 双剑合并工具_2100666204921884673.json, 视频生成/图生视频/LTX2.5 MSR二采放大音频参考｜H3参考生视频自动提示词优化V1.1_2092322003918348290.json, 视频生成/图生视频/LTX2.5 MSR二采放大｜MiniMax H3参考生音频提示词优化V1.1_2090191044980862978.json, 视频生成/图生视频/LTX2.5 MSR二采放大｜MiniMax H3参考生音频提示词优化图生视频_2092187292805984258.json, 视频生成/图生视频/MiniMax H3参考生视频LTX2.5 MSR二采放大｜音频参考自动提示词优化V1.1图生视频_2090468504624521218.json, 视频生成/图生视频/SBAPI MiniMaxH3加LTX25多参视频三分镜角色包匹配 多模态输入_2109783154608394242.json, 视频生成/图生视频/参考生视频V1.1｜MiniMax H3+LTX2.5 MSR二采放大音频参考自动提示词_2092551972753858562.json, 视频生成/图生视频/参考生视频V1｜MiniMax H3 + LTX2.5 MSR二采 音频参考提示词优化_2089311136461189121.json, 视频生成/图生视频/参考生视频V1｜MiniMax H3 + LTX2.5 MSR二采 音频参考提示词优化_2091020777008222210.json, 视频生成/图生视频/参考生音频提示词优化｜MiniMax H3+LTX2.5 MSR二采放大图生视频_2092603343406456834.json, 视频生成/图生视频/双剑合并多参视频生成｜MiniMax_H3加LTX2.5组合_2101166101144104962.json, 视频生成/文生视频/LTX2.5 MSR二采放大｜MiniMax H3参考生音频提示词优化V1.1_2091907695048740866.json, 视频生成/文生视频/SBAPI通道MiniMaxH3加LTX25多参视频｜三分镜角色包匹配_2105221254902013953.json, 视频生成/文生视频/参考生音频提示词优化V1.1｜MiniMax H3+LTX2.5 MSR二采放大_2092131156832641025.json, 视频生成/文生视频/双剑合璧MiniMax H3加LTX2.5多参视频生成 多模态输入方案_2105418867186159617.json, 视频生成/文生视频/双剑合璧MiniMax H3加LTX2.5｜多参视频生成强强联合_2105243547128651778.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_4

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/H3加LTX2.5多参视频生成 双剑合并工具_2100666204921884673.json、视频生成/图生视频/LTX2.5 MSR二采放大音频参考｜H3参考生视频自动提示词优化V1.1_2092322003918348290.json、视频生成/图生视频/LTX2.5 MSR二采放大｜MiniMax H3参考生音频提示词优化V1.1_2090191044980862978.json、视频生成/图生视频/LTX2.5 MSR二采放大｜MiniMax H3参考生音频提示词优化图生视频_2092187292805984258.json、视频生成/图生视频/MiniMax H3参考生视频LTX2.5 MSR二采放大｜音频参考自动提示词优化V1.1图生视频_2090468504624521218.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 16 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `ExtendIntermediateSigmas`
- `GetNode`
- `JjkText`
- `JoinStringMulti`
- `KSampler`
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
- `solarL_SaveImagesToZip`
- `string_util_StrFind`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 14/16 个有
- `LTXAddVideoICLoRAGuide` —— 14/16 个有
- `LTXICLoRALoaderModelOnly` —— 14/16 个有
- `LiconMSR` —— 14/16 个有
- `孤海注释` —— 14/16 个有
- `Fast Groups Bypasser (rgthree)` —— 10/16 个有
- `Label (rgthree)` —— 6/16 个有
- `SaveImage` —— 3/16 个有
- `ComfyUILTX25MSRICLoRALoader` —— 2/16 个有
- `ComfyUILTX25MSRMultiReferenceGuide` —— 2/16 个有
- `DF_String_Concatenate` —— 2/16 个有
- `DF_Text_Box` —— 2/16 个有
- `H3SigmaRefiner` —— 2/16 个有
- `JWStringGetLine` —— 2/16 个有
- `JjkConcat` —— 2/16 个有
- `JjkShowText` —— 2/16 个有
- `LTXVDualCFGGuider` —— 2/16 个有
- `ReplaceString` —— 2/16 个有
- `StringConstant` —— 2/16 个有
- `easy promptReplace` —— 2/16 个有
- `EmptyImage` —— 1/16 个有
- `PreviewImage` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
