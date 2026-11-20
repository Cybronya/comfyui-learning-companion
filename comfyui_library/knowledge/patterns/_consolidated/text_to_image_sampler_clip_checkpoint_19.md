---
name: text_to_image_sampler_clip_checkpoint_19
type: Text To Image
frequency: 5
level: moderate
coverage: 0.98
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json, 图片生成/文生图/【琉梦】基础文生图__光辉illustrious文生图__动漫文生图__极简_2044808427158904833.json, 图片生成/文生图/【遇见AI】SD1.5文生图基础工作流_2011308014015352833.json, 图片生成/文生图/【遇见AI】SD1.5版LCM lora_2016051847970168833.json, 图片生成/文生图/【遇见AI】SDXL版LCM lora_2016057417993293826.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_19

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json、图片生成/文生图/【琉梦】基础文生图__光辉illustrious文生图__动漫文生图__极简_2044808427158904833.json、图片生成/文生图/【遇见AI】SD1.5文生图基础工作流_2011308014015352833.json、图片生成/文生图/【遇见AI】SD1.5版LCM lora_2016051847970168833.json、图片生成/文生图/【遇见AI】SDXL版LCM lora_2016057417993293826.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Load Lora` —— 2/5 个有
- `GoogleTranslateTextNode` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `iToolsPromptStyler` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 5 | 51% |
| Prompt 约束强度(CFG) | 6 | 1.5 - 12 | 5 | 31% |
| 采样算法 | dpmpp_2m | - | 5 | 40% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 960 | 512 - 1024 | 5 | 70% |
| 高度 | 1024 | 512 - 1280 | 5 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 1.5 - 12，5 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 40%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 960，观测区间 512 - 1024，5 个样本
- 高度 中位数 1024，观测区间 512 - 1280，5 个样本
