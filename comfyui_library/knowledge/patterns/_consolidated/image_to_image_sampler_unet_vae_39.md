---
name: image_to_image_sampler_unet_vae_39
type: Image To Image
frequency: 6
level: strong
coverage: 0.804333
common_nodes: [CLIPLoader, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, TextEncodeKrea2OstrisEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2-洗图流-无需反推_2110759558145732609.json, 图片生成/图生图/Krea2洗图高质量4K_2077211215461441537.json, 图片生成/图生图/Krea2洗图高质量4K_2077214400984997890.json, 图片生成/图生图/krea2无需反推的洗图工作流_2081773404809682946.json, 图片生成/图生图/洗图Krea2-高质量4K_2076643574732640258.json, 图片生成/图生图/洗图Krea2-高质量4K_2088257533755613186.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_39

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea2-洗图流-无需反推_2110759558145732609.json、图片生成/图生图/Krea2洗图高质量4K_2077211215461441537.json、图片生成/图生图/Krea2洗图高质量4K_2077214400984997890.json、图片生成/图生图/krea2无需反推的洗图工作流_2081773404809682946.json、图片生成/图生图/洗图Krea2-高质量4K_2076643574732640258.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeKrea2OstrisEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `PrimitiveBoolean` —— 4/6 个有
- `PrimitiveFloat` —— 4/6 个有
- `easy ifElse` —— 4/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `String Literal` —— 1/6 个有
- `StringMergeNode` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.7 | 0.6 - 0.8 | 6 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.6 - 0.8，6 个样本，取值集中（一致性 92%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
