---
name: text_to_image_sampler_clip_unet_36
type: Text To Image
frequency: 10
level: strong
coverage: 0.9846
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed]
members: [图片生成/文生图/1901871929287188482.json, 图片生成/文生图/1904463583671980033.json, 图片生成/文生图/1910491843820253185.json, 图片生成/文生图/1910503564932804610.json, 图片生成/文生图/1912760478278348801.json, 图片生成/文生图/1915239700771045377.json, 图片生成/文生图/1976848182871314434.json, 图片生成/文生图/FLUX1文生图260814_2088196242147987458.json, 图片生成/文生图/FLUX工作流_2106376251710722050.json, 图片生成/文生图/Flux文生图工作流_2007992047759790082.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1901871929287188482.json、图片生成/文生图/1904463583671980033.json、图片生成/文生图/1910491843820253185.json、图片生成/文生图/1910503564932804610.json、图片生成/文生图/1912760478278348801.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 6/10 个有
- `DF_Text_Box` —— 5/10 个有
- `FluxLoraLoader` —— 5/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `FluxGuidance` —— 4/10 个有
- `TeaCache` —— 3/10 个有
- `CheckpointLoaderSimple` —— 1/10 个有
- `PMRF` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 8 - 25 | 10 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 50% |
| 调度器 | simple | - | 10 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 768 | 720 - 1024 | 10 | 87% |
| 高度 | 1024 | 768 - 1536 | 10 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22.5，观测区间 8 - 25，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 50%
- 调度器 最常用 simple，10 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 720 - 1024，10 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 768 - 1536，10 个样本，取值集中（一致性 82%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
