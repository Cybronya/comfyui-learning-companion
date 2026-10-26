---
name: text_to_image_video_lora_sampler_170
type: Text To Image
frequency: 4
level: strong
coverage: 0.47175
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, ModelPassThrough, PT_H3ConcatAVLatent, PathchSageAttentionKJ, PlaySound|pysssss, PreviewAny, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), SetNode, SomethingToString, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy clearCacheAll, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_unload_model, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax H3五合一8.19版｜加速反推双采多参文图首尾帧_2092372050458537985.json, 视频生成/文生视频/Minimax_H3五合一工作流｜双采多参文生图生首尾帧_2094570805253464066.json, 视频生成/文生视频/五合一8.19带KJ预览｜Minimax_H3加速反推双采多参全模态_2094761663563124737.json, 视频生成/文生视频/五合一（加速+双采+反推+文Minimax_H3_生+图生+首尾帧+多参）ENG_2087113095792648193.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_170

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/Minimax H3五合一8.19版｜加速反推双采多参文图首尾帧_2092372050458537985.json、视频生成/文生视频/Minimax_H3五合一工作流｜双采多参文生图生首尾帧_2094570805253464066.json、视频生成/文生视频/五合一8.19带KJ预览｜Minimax_H3加速反推双采多参全模态_2094761663563124737.json、视频生成/文生视频/五合一（加速+双采+反推+文Minimax_H3_生+图生+首尾帧+多参）ENG_2087113095792648193.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `ModelPassThrough`
- `PT_H3ConcatAVLatent`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SetNode`
- `SomethingToString`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_unload_model`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `ExtendIntermediateSigmas` —— 3/4 个有
- `MiniMaxH3SigmaShift` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `ModelPreviewOverrideKJ` —— 3/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
