---
name: text_to_image_sampler_clip_unet_12
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8526
common_nodes: [CLIPTextEncode, DeepTranslatorTextNode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/01动漫人物+场景FLUX文生图_1947078298218455041.json, 图片生成/文生图/1938437078218641410.json, 图片生成/文生图/1942946111835291650.json, 图片生成/文生图/1943306363688939521.json, 图片生成/文生图/1959457037811920898.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/01动漫人物+场景FLUX文生图_1947078298218455041.json、图片生成/文生图/1938437078218641410.json、图片生成/文生图/1942946111835291650.json、图片生成/文生图/1943306363688939521.json、图片生成/文生图/1959457037811920898.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewTextNode` —— 3/5 个有
- `Any Switch (rgthree)` —— 2/5 个有
- `ConcatTextOfUtils` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `ReferenceLatent` —— 2/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 512 - 1280 | 5 | 62% |
| 高度 | 720 | 512 - 1920 | 5 | 40% |
| 采样步数 | 20 | 20 - 30 | 5 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 512 - 1280，5 个样本
- 高度 中位数 720，观测区间 512 - 1920，5 个样本，取值分散，一致性仅 40%
- 采样步数 中位数 20，观测区间 20 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
