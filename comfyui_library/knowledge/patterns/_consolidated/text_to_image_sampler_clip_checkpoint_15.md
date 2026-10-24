---
name: text_to_image_sampler_clip_checkpoint_15
type: Text To Image
frequency: 6
level: moderate
coverage: 0.983333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json, 图片生成/文生图/jiami_test_2040045480884838401.json, 图片生成/文生图/new01_2046592687888928769.json, 图片生成/文生图/【遇见AI】SD1.5文生图基础工作流_2011308014015352833.json, 图片生成/文生图/【遇见AI】SD1.5版LCM lora_2016051847970168833.json, 图片生成/文生图/【遇见AI】SDXL版LCM lora_2016057417993293826.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_15

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json、图片生成/文生图/jiami_test_2040045480884838401.json、图片生成/文生图/new01_2046592687888928769.json、图片生成/文生图/【遇见AI】SD1.5文生图基础工作流_2011308014015352833.json、图片生成/文生图/【遇见AI】SD1.5版LCM lora_2016051847970168833.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Load Lora` —— 2/6 个有
- `GoogleTranslateTextNode` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `iToolsPromptStyler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 6 | 56% |
| Prompt 约束强度(CFG) | 8 | 1.5 - 12 | 6 | 41% |
| 采样算法 | euler | - | 6 | 33% |
| 调度器 | normal | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 640 | 512 - 1024 | 6 | 68% |
| 高度 | 768 | 512 - 1024 | 6 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1.5 - 12，6 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，6 个样本，一致性 33%
- 调度器 最常用 normal，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 640，观测区间 512 - 1024，6 个样本
- 高度 中位数 768，观测区间 512 - 1024，6 个样本
