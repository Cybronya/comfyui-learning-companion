---
name: text_to_image_sampler_clip_checkpoint_14
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8882
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/controlnet文生图SD_2106555235891245058.json, 图片生成/文生图/flux文生图99_1969418975585202177.json, 图片生成/文生图/【遇见AI】SDXL基础文生图工作流_2011360598709243906.json, 图片生成/文生图/【遇见AI】基础放大方法之像素空间放大_2011366127523336193.json, 图片生成/文生图/基础CG图片高清放大工作流_2016839532573892610.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/controlnet文生图SD_2106555235891245058.json、图片生成/文生图/flux文生图99_1969418975585202177.json、图片生成/文生图/【遇见AI】SDXL基础文生图工作流_2011360598709243906.json、图片生成/文生图/【遇见AI】基础放大方法之像素空间放大_2011366127523336193.json、图片生成/文生图/基础CG图片高清放大工作流_2016839532573892610.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/5 个有
- `ImageUpscaleWithModel` —— 2/5 个有
- `UpscaleModelLoader` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `FluxGuidance` —— 1/5 个有
- `LatentPixelScale` —— 1/5 个有
- `UltimateSDUpscale` —— 1/5 个有
- `VAELoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 7.53 | 1 - 8 | 5 | 57% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1000 | 512 - 1024 | 5 | 77% |
| 高度 | 1024 | 512 - 1536 | 5 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 7.53，观测区间 1 - 8，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1000，观测区间 512 - 1024，5 个样本
- 高度 中位数 1024，观测区间 512 - 1536，5 个样本
