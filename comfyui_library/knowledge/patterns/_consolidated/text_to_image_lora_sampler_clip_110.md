---
name: text_to_image_lora_sampler_clip_110
type: Text To Image
frequency: 13
level: strong
coverage: 0.909462
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2107209705771851778.json, 视频生成/图生视频/MiniMax H3超自然服装细节展示｜自动优化提示词图生视频_2106947776906088450.json, 视频生成/图生视频/MiniMax_H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2109460112296464386.json, 视频生成/图生视频/MiniMax_H3超自然服装细节展示｜自动优化提示词图生视频_2107268394373435393.json, 视频生成/图生视频/MiniMax_H3超自然服装细节展示｜自动优化提示词图生视频_2109461085458878466.json, 视频生成/图生视频/复刻短视频爆款同款｜minimax_h3滤镜特效图生视频_2096707939158552577.json, 视频生成/文生视频/FastVideo FastH3 8步加速V2视频生成工作流，文生视频图生视频高效方案_2106078715854802945.json, 视频生成/文生视频/FastVideo FastH3文生视频工作流，文生视频高效文本到视频生成方案_2107907010388914178.json, 视频生成/文生视频/FastVideo FastH3文生视频｜提示词直出视频不绕路_2107692375844941826.json, 视频生成/文生视频/minmaxH3单采加速三连发｜文生视频图生视频 又快又稳出片神器_2105532532883283969.json, 视频生成/文生视频/minmaxH3单采加速多场景｜文生视频视频生视频图生视频全支持_2105530783984340993.json, 视频生成/文生视频/minmaxH3单采加速｜文生视频图生视频 极速出片小钢炮_2105529286273880065.json, 视频生成/文生视频/极速高质开源版｜MiniMax H3 RE2VA多图参考生视频_2090934908318478338.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_110

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2107209705771851778.json、视频生成/图生视频/MiniMax H3超自然服装细节展示｜自动优化提示词图生视频_2106947776906088450.json、视频生成/图生视频/MiniMax_H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2109460112296464386.json、视频生成/图生视频/MiniMax_H3超自然服装细节展示｜自动优化提示词图生视频_2107268394373435393.json、视频生成/图生视频/MiniMax_H3超自然服装细节展示｜自动优化提示词图生视频_2109461085458878466.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3SigmaShift` —— 12/13 个有
- `LoadImage` —— 11/13 个有
- `MiniMaxH3ReferenceToVideo` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `孤海注释` —— 10/13 个有
- `BlockSparseAttention` —— 8/13 个有
- `PrimitiveFloat` —— 7/13 个有
- `LoraLoaderBypassModelOnly` —— 6/13 个有
- `MiniMaxH3PromptEnhancerT8` —— 6/13 个有
- `ModelPreviewOverrideKJ` —— 6/13 个有
- `ShowText|pysssss` —— 6/13 个有
- `easy seed` —— 6/13 个有
- `INTConstant` —— 5/13 个有
- `MiniMaxChunkFeedForward` —— 5/13 个有
- `SaveImage` —— 4/13 个有
- `VHS_LoadVideo` —— 4/13 个有
- `ExtendIntermediateSigmas` —— 3/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/13 个有
- `LoadAudio` —— 3/13 个有
- `PreviewImage` —— 3/13 个有
- `EmptyImage` —— 2/13 个有
- `MiniMaxH3ImageToVideo` —— 2/13 个有
- `H3SigmaRefiner` —— 1/13 个有
- `Int` —— 1/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
