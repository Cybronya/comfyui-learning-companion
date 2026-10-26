---
name: text_to_image_lora_sampler_clip_487
type: Text To Image
frequency: 4
level: strong
coverage: 0.80975
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, ModelAttentionBackend, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/单采导演台版H3工作流 场景特效文生图生视频处理工具_2112986609460269058.json, 视频生成/图生视频/最强单采导演台版｜接入搅拌手导演台插件场景大片直出_2112915223085674498.json, 视频生成/文生视频/H3开源版海螺视频导演台全合集工作流多段生成_2100657814959116289.json, 视频生成/文生视频/MiniMax H3开源版海螺视频导演台全合集处理工作流_2102158377316085761.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_487

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/单采导演台版H3工作流 场景特效文生图生视频处理工具_2112986609460269058.json、视频生成/图生视频/最强单采导演台版｜接入搅拌手导演台插件场景大片直出_2112915223085674498.json、视频生成/文生视频/H3开源版海螺视频导演台全合集工作流多段生成_2100657814959116289.json、视频生成/文生视频/MiniMax H3开源版海螺视频导演台全合集处理工作流_2102158377316085761.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `ModelAttentionBackend`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 3/4 个有
- `BlockSparseAttention` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ManualSigmas` —— 2/4 个有
- `MiniMaxChunkFeedForward` —— 2/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `MiniMaxLowVRAMAttention` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `MiniMaxH3DirectorSelfLift` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有

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
