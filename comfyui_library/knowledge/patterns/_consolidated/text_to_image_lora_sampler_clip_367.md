---
name: text_to_image_lora_sampler_clip_367
type: Text To Image
frequency: 6
level: strong
coverage: 0.809333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3文生视频｜官方加速版工作流生成_2096331392543191041.json, 视频生成/文生视频/MiniMax H3超级加速文生视频，角色一致性角色表演视频生成方案_2103903431479095298.json, 视频生成/文生视频/MiniMax h3 4步lora2加速版｜文生图生视频直出_2092366496205987842.json, 视频生成/文生视频/MiniMax-4步加速工作流文生视频视频生视频图生视频_2085455891675049986.json, 视频生成/文生视频/MiniMax参考生视频高质量加速版处理工具_2101029961053327362.json, 视频生成/文生视频/Minimax H3文生首尾图参多合一生视频-自用版二采高清放大_2087394737073512450.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_367

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3文生视频｜官方加速版工作流生成_2096331392543191041.json、视频生成/文生视频/MiniMax H3超级加速文生视频，角色一致性角色表演视频生成方案_2103903431479095298.json、视频生成/文生视频/MiniMax h3 4步lora2加速版｜文生图生视频直出_2092366496205987842.json、视频生成/文生视频/MiniMax-4步加速工作流文生视频视频生视频图生视频_2085455891675049986.json、视频生成/文生视频/MiniMax参考生视频高质量加速版处理工具_2101029961053327362.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `LoadImage` —— 4/6 个有
- `MiniMaxH3ImageToVideo` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `MiniMaxH3ReferenceToVideo` —— 3/6 个有
- `PathchSageAttentionKJ` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `Any Switch (rgthree)` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `Int` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxH3BlockCacheT8` —— 1/6 个有
- `MiniMaxLowVRAMAttention` —— 1/6 个有
- `ModelAttentionBackend` —— 1/6 个有
- `PT_H3ConcatAVLatent` —— 1/6 个有
- `PainterVRAM` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `VAEEncode` —— 1/6 个有
- `VAEEncodeAudio` —— 1/6 个有
- `忽略多组孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
