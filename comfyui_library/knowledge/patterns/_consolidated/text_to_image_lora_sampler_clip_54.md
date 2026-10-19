---
name: text_to_image_lora_sampler_clip_54
type: Text To Image
frequency: 14
level: strong
coverage: 0.899429
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2107209705771851778.json, 视频生成/图生视频/MiniMax H3超自然服装细节展示｜自动优化提示词图生视频_2106947776906088450.json, 视频生成/图生视频/MiniMaxH3四关键帧视频生成｜KeyFrames X4工作流_2094875841221185538.json, 视频生成/图生视频/MiniMax_H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2109460112296464386.json, 视频生成/图生视频/MiniMax_H3超自然服装细节展示｜自动优化提示词图生视频_2107268394373435393.json, 视频生成/图生视频/MiniMax_H3超自然服装细节展示｜自动优化提示词图生视频_2109461085458878466.json, 视频生成/图生视频/二关键帧视频生成｜MiniMaxH3 KeyFarmes X2工作流_2095116824059928577.json, 视频生成/图生视频/四关键帧视频生成｜MiniMaxH3 KeyFarmes X4工作流_2095078270608953346.json, 视频生成/图生视频/复刻短视频爆款同款｜minimax_h3滤镜特效图生视频_2096707939158552577.json, 视频生成/文生视频/FastVideo FastH3 8步加速V2视频生成工作流，文生视频图生视频高效方案_2106078715854802945.json, 视频生成/文生视频/H3高动态打斗场景武术动作二采修复 提示词增强工作流_2099919995085086722.json, 视频生成/文生视频/剑斗多参模式视频生成｜战斗动作多参考一致性_2094543565945921538.json, 视频生成/文生视频/双采首尾帧战斗模式｜文生图生视频特效生成_2094783307044188162.json, 视频生成/文生视频/多参模式剑斗生成｜文生图生视频战斗特效工作流_2094789270803410946.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2107209705771851778.json、视频生成/图生视频/MiniMax H3超自然服装细节展示｜自动优化提示词图生视频_2106947776906088450.json、视频生成/图生视频/MiniMaxH3四关键帧视频生成｜KeyFrames X4工作流_2094875841221185538.json、视频生成/图生视频/MiniMax_H3超自然服装细节展示自动优化提示词，服装展示图生视频方案_2109460112296464386.json、视频生成/图生视频/MiniMax_H3超自然服装细节展示｜自动优化提示词图生视频_2107268394373435393.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
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
- `MiniMaxH3ReferenceToVideo` —— 13/14 个有
- `孤海注释` —— 11/14 个有
- `ModelAttentionBackend` —— 10/14 个有
- `PrimitiveFloat` —— 8/14 个有
- `MiniMaxH3SigmaShift` —— 7/14 个有
- `easy cleanGpuUsed` —— 7/14 个有
- `BlockSparseAttention` —— 6/14 个有
- `MiniMaxH3PromptEnhancerT8` —— 6/14 个有
- `ModelPreviewOverrideKJ` —— 6/14 个有
- `ShowText|pysssss` —— 6/14 个有
- `easy seed` —— 6/14 个有
- `INTConstant` —— 5/14 个有
- `LoraLoaderBypassModelOnly` —— 5/14 个有
- `MiniMaxChunkFeedForward` —— 5/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/14 个有
- `DisableNoise` —— 4/14 个有
- `SaveImage` —— 4/14 个有
- `ExtendIntermediateSigmas` —— 3/14 个有
- `MiniMaxH3AddGuide` —— 3/14 个有
- `PreviewImage` —— 3/14 个有
- `SplitSigmasDenoise` —— 3/14 个有
- `EmptyImage` —— 2/14 个有
- `MiniMaxH3ImageToVideo` —— 1/14 个有
- `SplitSigmas` —— 1/14 个有
- `VHS_LoadVideo` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
