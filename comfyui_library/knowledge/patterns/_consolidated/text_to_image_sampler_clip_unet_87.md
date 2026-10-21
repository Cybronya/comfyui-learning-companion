---
name: text_to_image_sampler_clip_unet_87
type: Text To Image
frequency: 5
level: strong
coverage: 0.8496
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM]
members: [图片生成/文生图/1907792965371371522.json, 图片生成/文生图/1910971389912805378.json, 图片生成/文生图/1911939065036636162.json, 图片生成/文生图/nunchaku_flux1对比未加速_2005576570435764226.json, 视频生成/图生视频/1910971389912805378.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_87

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1907792965371371522.json、图片生成/文生图/1910971389912805378.json、图片生成/文生图/1911939065036636162.json、图片生成/文生图/nunchaku_flux1对比未加速_2005576570435764226.json、视频生成/图生视频/1910971389912805378.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `NunchakuFluxDiTLoader` —— 4/5 个有
- `CFGZeroStarAndInit` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `NunchakuFluxLoraLoader` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1280 | 5 | 90% |
| 高度 | 1024 | 720 - 1024 | 5 | 87% |
| 采样步数 | 25 | 20 - 25 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1280，5 个样本，取值集中（一致性 90%）
- 高度 中位数 1024，观测区间 720 - 1024，5 个样本，取值集中（一致性 87%）
- 采样步数 中位数 25，观测区间 20 - 25，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM
