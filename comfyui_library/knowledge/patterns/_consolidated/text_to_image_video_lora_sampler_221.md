---
name: text_to_image_video_lora_sampler_221
type: Text To Image
frequency: 2
level: weak
coverage: 0.7315
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ComfyMathExpression, EmptyLatentImage, ExtractAndCombineLines, Fast Groups Bypasser (rgthree), ImageBatchMulti, JWFloatToString, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, PixaromaGetNode, PixaromaSetNode, PreviewAny, PreviewImage, PrimitiveFloat, ProcessString, RHHiddenNodes, RHLLMChatNode, RHSettingsNode, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, Text, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy seed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 20加步战斗镜头SKILL一键4镜版工作流 武戏生成_2105398514657349633.json, 视频生成/图生视频/战斗镜头4镜版一键生成｜MiniMax H3 LORA双采8步加速SKILL工作流_2095477346882117634.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_221

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 20加步战斗镜头SKILL一键4镜版工作流 武戏生成_2105398514657349633.json、视频生成/图生视频/战斗镜头4镜版一键生成｜MiniMax H3 LORA双采8步加速SKILL工作流_2095477346882117634.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `ExtractAndCombineLines`
- `Fast Groups Bypasser (rgthree)`
- `ImageBatchMulti`
- `JWFloatToString`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PixaromaGetNode`
- `PixaromaSetNode`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveFloat`
- `ProcessString`
- `RHHiddenNodes`
- `RHLLMChatNode`
- `RHSettingsNode`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy seed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Image Lucy Sharpen` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `LatentUpscale` —— 1/2 个有
- `MiniMaxH3BlockCacheT8` —— 1/2 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/2 个有
- `ModelPreviewOverrideKJ` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PT_H3ConcatAVLatent` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `VAEEncodeAudio` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
