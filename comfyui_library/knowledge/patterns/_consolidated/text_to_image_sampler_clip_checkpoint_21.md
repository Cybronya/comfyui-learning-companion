---
name: text_to_image_sampler_clip_checkpoint_21
type: Text To Image
frequency: 3
level: moderate
coverage: 0.883333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/多角色场景图_2024871142439264257.json, 图片生成/文生图/图生图、局部重绘教学_1891856460194942978.json, 图片生成/文生图/多组脸部参考文生图ipadapter_faceid_batch_1916140739846410242.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/多角色场景图_2024871142439264257.json、图片生成/文生图/图生图、局部重绘教学_1891856460194942978.json、图片生成/文生图/多组脸部参考文生图ipadapter_faceid_batch_1916140739846410242.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `IPAdapter` —— 2/3 个有
- `IPAdapterUnifiedLoaderFaceID` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `IPAdapterFaceID` —— 1/3 个有
- `IPAdapterUnifiedLoader` —— 1/3 个有
- `ImageBatch` —— 1/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `VAEEncodeForInpaint` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 7 | 6.5 - 8 | 3 | 91% |
| 采样算法 | euler | - | 3 | 33% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 1024 | 3 | 65% |
| 高度 | 768 | 512 - 1024 | 3 | 73% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 6.5 - 8，3 个样本，取值集中（一致性 91%）
- 采样算法 最常用 euler，3 个样本，一致性 33%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 1024，3 个样本
- 高度 中位数 768，观测区间 512 - 1024，3 个样本
