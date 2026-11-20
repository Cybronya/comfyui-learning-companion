---
name: text_to_image_lora_sampler_clip_143
type: Text To Image
frequency: 12
level: strong
coverage: 0.89875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2107209705771851778.json, 视频生成/图生视频/MiniMax H3超自然服装细节展示｜自动优化提示词图生视频_2106947776906088450.json, 视频生成/图生视频/MiniMaxH3四关键帧视频生成｜KeyFrames X4工作流_2094875841221185538.json, 视频生成/图生视频/MiniMax_H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2109460112296464386.json, 视频生成/图生视频/MiniMax_H3超自然服装细节展示｜自动优化提示词图生视频_2107268394373435393.json, 视频生成/图生视频/MiniMax_H3超自然服装细节展示｜自动优化提示词图生视频_2109461085458878466.json, 视频生成/图生视频/二关键帧视频生成｜MiniMaxH3 KeyFarmes X2工作流_2095116824059928577.json, 视频生成/图生视频/四关键帧视频生成｜MiniMaxH3 KeyFarmes X4工作流_2095078270608953346.json, 视频生成/图生视频/复刻短视频爆款同款｜minimax_h3滤镜特效图生视频_2096707939158552577.json, 视频生成/文生视频/FastVideo FastH3 8步加速V2视频生成工作流，文生视频图生视频高效方案_2106078715854802945.json, 视频生成/文生视频/参考加速工作流｜Minmax H3文生图生视频直出_2091671424758009858.json, 视频生成/文生视频/极速高质开源版｜MiniMax H3 RE2VA多图参考生视频_2090934908318478338.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_143

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2107209705771851778.json、视频生成/图生视频/MiniMax H3超自然服装细节展示｜自动优化提示词图生视频_2106947776906088450.json、视频生成/图生视频/MiniMaxH3四关键帧视频生成｜KeyFrames X4工作流_2094875841221185538.json、视频生成/图生视频/MiniMax_H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2109460112296464386.json、视频生成/图生视频/MiniMax_H3超自然服装细节展示｜自动优化提示词图生视频_2107268394373435393.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
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
- `孤海注释` —— 9/12 个有
- `MiniMaxH3SigmaShift` —— 8/12 个有
- `BlockSparseAttention` —— 6/12 个有
- `LoraLoaderBypassModelOnly` —— 6/12 个有
- `MiniMaxH3PromptEnhancerT8` —— 6/12 个有
- `ModelPreviewOverrideKJ` —— 6/12 个有
- `PrimitiveFloat` —— 6/12 个有
- `ShowText|pysssss` —— 6/12 个有
- `easy seed` —— 6/12 个有
- `INTConstant` —— 5/12 个有
- `MiniMaxChunkFeedForward` —— 5/12 个有
- `easy cleanGpuUsed` —— 4/12 个有
- `MiniMaxH3AddGuide` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `SaveImage` —— 3/12 个有
- `EmptyImage` —— 2/12 个有
- `H3SigmaRefiner` —— 2/12 个有
- `Int` —— 2/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/12 个有
- `VHS_LoadVideo` —— 2/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `LoadAudio` —— 1/12 个有
- `SigmasPreview` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
