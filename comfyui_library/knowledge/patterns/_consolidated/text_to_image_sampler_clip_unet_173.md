---
name: text_to_image_sampler_clip_unet_173
type: Text To Image
frequency: 4
level: moderate
coverage: 0.9445
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/榨干Zimage！最强画质Dype原生4K生图，海量细节！_1999459942526484482.json, 图片生成/文生图/法式复古风格的美女_2114250444477394946.json, 图片生成/文生图/流体金属家居产品设计_2022553115676909569.json, 图片生成/文生图/高层住宅立面泛化_2015087544735637505.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_173

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/榨干Zimage！最强画质Dype原生4K生图，海量细节！_1999459942526484482.json、图片生成/文生图/法式复古风格的美女_2114250444477394946.json、图片生成/文生图/流体金属家居产品设计_2022553115676909569.json、图片生成/文生图/高层住宅立面泛化_2015087544735637505.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `Text` —— 3/4 个有
- `ConcatTextOfUtils` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `DyPE_FLUX` —— 1/4 个有
- `Seed Generator` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 4 | 0% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 984 - 1280 | 4 | 89% |
| 高度 | 1280 | 1024 - 1536 | 4 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 984 - 1280，4 个样本，取值集中（一致性 89%）
- 高度 中位数 1280，观测区间 1024 - 1536，4 个样本，取值集中（一致性 86%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
