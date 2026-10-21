---
name: unknown_workflow_sampler_clip_unet_107
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.726833
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR SDXL Aspect Ratio]
members: [图片生成/文生图/01 Qwen image 批量文生图 亚马逊平台外国儿童模特_2009990778717741058.json, 图片生成/文生图/1954857769355534338.json, 图片生成/文生图/1955157274396430337.json, 图片生成/文生图/1963484613191749634.json, 图片生成/文生图/Qwen-Image-2512基础文生图 T2I_2065613919451963393.json, 图片生成/文生图/Qwen-Image-2512基础文生图 T2I_2076908888892469249.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_107

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/01 Qwen image 批量文生图 亚马逊平台外国儿童模特_2009990778717741058.json、图片生成/文生图/1954857769355534338.json、图片生成/文生图/1955157274396430337.json、图片生成/文生图/1963484613191749634.json、图片生成/文生图/Qwen-Image-2512基础文生图 T2I_2065613919451963393.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `CR SDXL Aspect Ratio` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `Int` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `Text` —— 2/6 个有
- `CR Prompt List` —— 1/6 个有
- `EmptyUnitGenerator_UTK` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 6 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 55% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR SDXL Aspect Ratio
