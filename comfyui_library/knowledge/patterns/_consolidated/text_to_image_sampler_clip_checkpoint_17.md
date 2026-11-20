---
name: text_to_image_sampler_clip_checkpoint_17
type: Text To Image
frequency: 6
level: moderate
coverage: 0.885333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/【尺素】RED-Z-IMAGE-AIO文生图_2074013706979209217.json, 图片生成/文生图/【遇见AI】SDXL基础文生图工作流_2011360598709243906.json, 图片生成/文生图/人物立绘_2039073481756774402.json, 图片生成/文生图/元气少女_2044022472999182337.json, 图片生成/文生图/冒险漫画风_2114146613148086273.json, 图片生成/文生图/清新治愈风_2114157669224378370.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_17

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/【尺素】RED-Z-IMAGE-AIO文生图_2074013706979209217.json、图片生成/文生图/【遇见AI】SDXL基础文生图工作流_2011360598709243906.json、图片生成/文生图/人物立绘_2039073481756774402.json、图片生成/文生图/元气少女_2044022472999182337.json、图片生成/文生图/冒险漫画风_2114146613148086273.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraSave` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 720 - 1024 | 6 | 85% |
| 高度 | 1024 | 1024 - 1904 | 6 | 73% |
| 采样步数 | 22.5 | 10 - 50 | 6 | 52% |
| Prompt 约束强度(CFG) | 5.25 | 1 - 8 | 6 | 49% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | normal | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 720 - 1024，6 个样本，取值集中（一致性 85%）
- 高度 中位数 1024，观测区间 1024 - 1904，6 个样本
- 采样步数 中位数 22.5，观测区间 10 - 50，6 个样本
- Prompt 约束强度(CFG) 中位数 5.25，观测区间 1 - 8，6 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 normal，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
