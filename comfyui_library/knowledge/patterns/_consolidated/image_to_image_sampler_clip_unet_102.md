---
name: image_to_image_sampler_clip_unet_102
type: Image To Image
frequency: 5
level: moderate
coverage: 0.93
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, RH_Translator, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/开源版Kontext [dev]，一句话精准改图，省算力！_1938559267488063489.json, 图片生成/图生图/换背景kontext_1989633808280506369.json, 图片生成/图生图/提取产品-生成三视图（FLUX_Kontext）_1958816743533785089.json, 图片生成/图生图/老照片修复+上色kontext dev_1946791542956941313.json, 图片生成/图生图/老照片修复及上色-kontext dev开源_1939192628053229569.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_102

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/开源版Kontext [dev]，一句话精准改图，省算力！_1938559267488063489.json、图片生成/图生图/换背景kontext_1989633808280506369.json、图片生成/图生图/提取产品-生成三视图（FLUX_Kontext）_1958816743533785089.json、图片生成/图生图/老照片修复+上色kontext dev_1946791542956941313.json、图片生成/图生图/老照片修复及上色-kontext dev开源_1939192628053229569.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `Preview from image [Crystools]` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `easy imageConcat` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 5 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
