---
name: text_to_image_video_lora_sampler_181
type: Text To Image
frequency: 3
level: strong
coverage: 0.819333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/minimax_h3_i2vw4a8-0810超低显存ENGENG_2087115217783316482.json, 视频生成/文生视频/minimax阿里8步加速三合一｜文生视频图生视频全能参考_2095568310212587522.json, 视频生成/文生视频/多合一加速修复｜MiniMax H3热门IP模糊视频高清处理_2090232166843240449.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_181

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/minimax_h3_i2vw4a8-0810超低显存ENGENG_2087115217783316482.json、视频生成/文生视频/minimax阿里8步加速三合一｜文生视频图生视频全能参考_2095568310212587522.json、视频生成/文生视频/多合一加速修复｜MiniMax H3热门IP模糊视频高清处理_2090232166843240449.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `Display Any (rgthree)` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImpactConditionalBranch` —— 1/3 个有
- `LoraLoaderBypassModelOnly` —— 1/3 个有
- `MiniMaxH3BlockCacheT8` —— 1/3 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/3 个有
- `MiniMaxH3ReferenceToVideo` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `SolAttnPatch` —— 1/3 个有
- `easy boolean` —— 1/3 个有

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
