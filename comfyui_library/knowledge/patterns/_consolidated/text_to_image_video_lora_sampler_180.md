---
name: text_to_image_video_lora_sampler_180
type: Text To Image
frequency: 3
level: strong
coverage: 0.887333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ComfyMathExpression, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageResizeKJv2, ImageScaleBy, JjkText, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadImage, Lora Loader Stack (rgthree), LoraLoaderModelOnly, MiniMaxH3ConcatAVLatent, MiniMaxH3ContextIR, MiniMaxH3HybridLoader, MiniMaxH3ImageToVideo, MiniMaxH3MediaLoaderFantastic, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceSplitter, MiniMaxH3ReferenceToVideo, MiniMaxH3ResolutionSelector, MiniMaxH3TurboLoRA, MiniMaxH3TurboSampler, MiniMaxH3UnifiedToVideo, Minimax_H3_Context_IR, PreviewAny, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, Seed (rgthree), UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/开源MiniMax H3全能工作流，文生视频图生视频首尾帧参考生视频极速兼容_2103178748689477634.json, 视频生成/图生视频/开源版MiniMaxH3全能精品工作流｜文生图生参考极速生视频_2101930241441755137.json, 视频生成/图生视频/开源版MiniMaxH3全能精品｜文生图到参考视频极速一条龙_2103044074793160706.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_180

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/开源MiniMax H3全能工作流，文生视频图生视频首尾帧参考生视频极速兼容_2103178748689477634.json、视频生成/图生视频/开源版MiniMaxH3全能精品工作流｜文生图生参考极速生视频_2101930241441755137.json、视频生成/图生视频/开源版MiniMaxH3全能精品｜文生图到参考视频极速一条龙_2103044074793160706.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `LoraLoaderModelOnly`
- `MiniMaxH3ConcatAVLatent`
- `MiniMaxH3ContextIR`
- `MiniMaxH3HybridLoader`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MediaLoaderFantastic`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceSplitter`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ResolutionSelector`
- `MiniMaxH3TurboLoRA`
- `MiniMaxH3TurboSampler`
- `MiniMaxH3UnifiedToVideo`
- `Minimax_H3_Context_IR`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
