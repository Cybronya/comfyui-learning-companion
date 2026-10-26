---
name: text_to_image_sampler_clip_unet_176
type: Text To Image
frequency: 3
level: moderate
coverage: 0.892
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext SingalImage_单图修改_Borges_1951605887653851137.json, 图片生成/图生图/Kontext 单图编辑_1954835404466774017.json, 图片生成/图生图/kontext _ 22种风格切换合集_1940781888825147394.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_176

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux Kontext SingalImage_单图修改_Borges_1951605887653851137.json、图片生成/图生图/Kontext 单图编辑_1954835404466774017.json、图片生成/图生图/kontext _ 22种风格切换合集_1940781888825147394.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `FluxResolutionNode` —— 1/3 个有
- `GoogleTranslateTextNode` —— 1/3 个有
- `Image Padding` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `Text String` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 12 - 20 | 3 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 512 - 1080 | 3 | 71% |
| 高度 | 1280 | 512 - 1920 | 3 | 53% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 12 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1080，3 个样本
- 高度 中位数 1280，观测区间 512 - 1920，3 个样本
