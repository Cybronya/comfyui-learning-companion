---
name: text_to_image_sampler_clip_checkpoint_15
type: Text To Image
frequency: 5
level: moderate
coverage: 0.98
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json, 图片生成/文生图/人物立绘_2039073481756774402.json, 图片生成/文生图/元气少女_2044022472999182337.json, 图片生成/文生图/冒险漫画风_2114146613148086273.json, 图片生成/文生图/清新治愈风_2114157669224378370.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_15

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/itools prompt styler x alekpet翻译_1975588560873066498.json、图片生成/文生图/人物立绘_2039073481756774402.json、图片生成/文生图/元气少女_2044022472999182337.json、图片生成/文生图/冒险漫画风_2114146613148086273.json、图片生成/文生图/清新治愈风_2114157669224378370.json）

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
- `LoraSave` —— 2/5 个有
- `GoogleTranslateTextNode` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `iToolsPromptStyler` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 50 | 5 | 67% |
| Prompt 约束强度(CFG) | 7 | 3.5 - 12 | 5 | 53% |
| 采样算法 | euler | - | 5 | 40% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768 | 720 - 1024 | 5 | 87% |
| 高度 | 1024 | 1024 - 1280 | 5 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 3.5 - 12，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 40%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 720 - 1024，5 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1280，5 个样本，取值集中（一致性 90%）
