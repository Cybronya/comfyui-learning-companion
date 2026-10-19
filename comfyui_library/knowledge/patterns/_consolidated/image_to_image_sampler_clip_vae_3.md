---
name: image_to_image_sampler_clip_vae_3
type: Image To Image
frequency: 6
level: strong
coverage: 0.8485
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Simple Image Compare]
members: [图片生成/图生图/2060639940156940290.json, 图片生成/图生图/2099656538049826818.json, 图片生成/图生图/kontext一键去水印 _ 前后对比_2069314818917625857.json, 图片生成/文生图/1940252363783360514.json, 图片生成/文生图/1942450419496857602.json, 图片生成/文生图/1945286940809732097.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2060639940156940290.json、图片生成/图生图/2099656538049826818.json、图片生成/图生图/kontext一键去水印 _ 前后对比_2069314818917625857.json、图片生成/文生图/1940252363783360514.json、图片生成/文生图/1942450419496857602.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/6 个有
- `ImageStitch` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `LoadImageOutput` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `TeaCache` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `CR Simple Image Compare` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `LoadKontextPresets` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `RepeatLatentBatch` —— 1/6 个有
- `ShowText` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 6 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Simple Image Compare
