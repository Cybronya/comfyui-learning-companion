---
name: text_to_image_sampler_clip_checkpoint_6
type: Text To Image
frequency: 11
level: moderate
coverage: 0.981818
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【遇见AI】SD1.5版LCM lora_2016051847970168833.json, 图片生成/文生图/【遇见AI】SDXL基础文生图工作流_2011360598709243906.json, 图片生成/文生图/【遇见AI】SDXL版LCM lora_2016057417993293826.json, 图片生成/文生图/中西合璧古典美人一键生成_1889372369155448834.json, 图片生成/文生图/冷冬圣诞夜漫画风_2096584608396693506.json, 图片生成/文生图/别墅庭院风_2063986622978420738.json, 图片生成/文生图/动漫_2070124661043716097.json, 图片生成/文生图/动漫女孩_2101663777623207938.json, 图片生成/文生图/动漫美少女_2072470520804761601.json, 图片生成/文生图/咖啡馆漫画风_2101655459567591426.json, 图片生成/文生图/基础文生图_2013094085589999617.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_6

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/【遇见AI】SD1.5版LCM lora_2016051847970168833.json、图片生成/文生图/【遇见AI】SDXL基础文生图工作流_2011360598709243906.json、图片生成/文生图/【遇见AI】SDXL版LCM lora_2016057417993293826.json、图片生成/文生图/中西合璧古典美人一键生成_1889372369155448834.json、图片生成/文生图/冷冬圣诞夜漫画风_2096584608396693506.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Load Lora` —— 2/11 个有
- `JjkText` —— 1/11 个有
- `JoinStrings` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1080 | 11 | 78% |
| 高度 | 1024 | 512 - 1920 | 11 | 66% |
| 采样步数 | 20 | 8 - 50 | 11 | 45% |
| Prompt 约束强度(CFG) | 3.5 | 1.5 - 8 | 11 | 48% |
| 采样算法 | euler | - | 11 | 73% |
| 调度器 | normal | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1080，11 个样本
- 高度 中位数 1024，观测区间 512 - 1920，11 个样本
- 采样步数 中位数 20，观测区间 8 - 50，11 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1.5 - 8，11 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，11 个样本，一致性 73%
- 调度器 最常用 normal，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
