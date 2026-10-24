---
name: text_to_image_sampler_clip_unet_198
type: Text To Image
frequency: 3
level: strong
coverage: 0.926
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, Text, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/榨干Zimage！最强画质Dype原生4K生图，海量细节！_1999459942526484482.json, 图片生成/文生图/流体金属家居产品设计_2022553115676909569.json, 图片生成/文生图/高层住宅立面泛化_2015087544735637505.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_198

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/榨干Zimage！最强画质Dype原生4K生图，海量细节！_1999459942526484482.json、图片生成/文生图/流体金属家居产品设计_2022553115676909569.json、图片生成/文生图/高层住宅立面泛化_2015087544735637505.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConcatTextOfUtils` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `DyPE_FLUX` —— 1/3 个有
- `Seed Generator` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 9 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 984 - 1280 | 3 | 88% |
| 高度 | 1280 | 1280 - 1536 | 3 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 9，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 984 - 1280，3 个样本，取值集中（一致性 88%）
- 高度 中位数 1280，观测区间 1280 - 1536，3 个样本，取值集中（一致性 91%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
