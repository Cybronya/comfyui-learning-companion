---
name: image_to_image_sampler_clip_unet_46
type: Image To Image
frequency: 8
level: strong
coverage: 0.8705
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext-生成产品背景_1943184610207686657.json, 图片生成/图生图/Kontext-生成产品背景_1971036089194553346.json, 图片生成/图生图/Kontext一句话转换风格（主体特征不变）_1942037287171735554.json, 图片生成/图生图/Kontext一键转为动漫风格（主体特征不变）_1991802548898328578.json, 图片生成/图生图/Kontext图像万能编辑_1962166621970305026.json, 图片生成/图生图/Kontext图像编辑_1957981327398203394.json, 图片生成/图生图/ai性别大反转男生转女生_1944259274073604097.json, 图片生成/图生图/flux_kontext 脸部去油，去AI感，真实皮肤_1946634107703947266.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_46

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Kontext-生成产品背景_1943184610207686657.json、图片生成/图生图/Kontext-生成产品背景_1971036089194553346.json、图片生成/图生图/Kontext一句话转换风格（主体特征不变）_1942037287171735554.json、图片生成/图生图/Kontext一键转为动漫风格（主体特征不变）_1991802548898328578.json、图片生成/图生图/Kontext图像万能编辑_1962166621970305026.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
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
- `PreviewImage` —— 6/8 个有
- `FluxKontextImageScale` —— 5/8 个有
- `easy imageConcat` —— 3/8 个有
- `GetNode` —— 2/8 个有
- `GoogleTranslateTextNode` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `LayerUtility: ImageReel` —— 1/8 个有
- `LayerUtility: ImageReelComposit` —— 1/8 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/8 个有
- `TeaCache` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 8 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
