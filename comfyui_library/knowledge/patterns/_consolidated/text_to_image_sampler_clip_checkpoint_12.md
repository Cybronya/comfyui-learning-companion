---
name: text_to_image_sampler_clip_checkpoint_12
type: Text To Image
frequency: 6
level: moderate
coverage: 0.873
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/【RICK】肖像大师高清版(模特生成)_1906519526463442946.json, 图片生成/文生图/图像细节放大_2012407929160343554.json, 图片生成/文生图/文生图工作流_2090257194913718274.json, 图片生成/文生图/文生图最简版_1990400035454148610.json, 图片生成/文生图/清晰_2013889963875639297.json, 图片生成/文生图/肖像大师-根据提示词生成人物肖像_2061354886461218818.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_12

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/【RICK】肖像大师高清版(模特生成)_1906519526463442946.json、图片生成/文生图/图像细节放大_2012407929160343554.json、图片生成/文生图/文生图工作流_2090257194913718274.json、图片生成/文生图/文生图最简版_1990400035454148610.json、图片生成/文生图/清晰_2013889963875639297.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `LatentUpscaleBy` —— 3/6 个有
- `PortraitMaster_中文版` —— 2/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 768 | 6 | 82% |
| 高度 | 640 | 512 - 1280 | 6 | 58% |
| 采样步数 | 20 | 20 - 40 | 6 | 70% |
| Prompt 约束强度(CFG) | 8 | 6.5 - 8 | 6 | 93% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | normal | - | 6 | 33% |
| 重绘幅度 | 1 | 0.5 - 1 | 6 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 768，6 个样本，取值集中（一致性 82%）
- 高度 中位数 640，观测区间 512 - 1280，6 个样本
- 采样步数 中位数 20，观测区间 20 - 40，6 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 6.5 - 8，6 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 normal，6 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，6 个样本
