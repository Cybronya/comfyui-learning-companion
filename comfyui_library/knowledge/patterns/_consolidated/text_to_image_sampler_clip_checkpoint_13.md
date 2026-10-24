---
name: text_to_image_sampler_clip_checkpoint_13
type: Text To Image
frequency: 6
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FluxDev文生图工作流_1969281537156018177.json, 图片生成/文生图/Kinghere_Z-image卓越美学文生图_1999757899914244098.json, 图片生成/文生图/SDXL+肖像大师-精细化生成人像_1928323196418670594.json, 图片生成/文生图/flux文生图99_1969418975585202177.json, 图片生成/文生图/文生图动漫工作流_2087082317775982593.json, 图片生成/文生图/白玉-AIO模型测试_2045022702641090561.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_13

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/FluxDev文生图工作流_1969281537156018177.json、图片生成/文生图/Kinghere_Z-image卓越美学文生图_1999757899914244098.json、图片生成/文生图/SDXL+肖像大师-精细化生成人像_1928323196418670594.json、图片生成/文生图/flux文生图99_1969418975585202177.json、图片生成/文生图/文生图动漫工作流_2087082317775982593.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/6 个有
- `FluxGuidance` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `Int` —— 1/6 个有
- `PortraitMaster_中文版` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1080 | 6 | 79% |
| 高度 | 1280 | 512 - 1920 | 6 | 61% |
| 采样步数 | 20 | 8 - 25 | 6 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 6 | 0% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1080，6 个样本
- 高度 中位数 1280，观测区间 512 - 1920，6 个样本
- 采样步数 中位数 20，观测区间 8 - 25，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
