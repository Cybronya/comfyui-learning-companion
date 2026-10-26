---
name: image_to_image_sampler_unet_vae_27
type: Image To Image
frequency: 7
level: strong
coverage: 0.818286
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2-洗图流-无需反推_2110759558145732609.json, 图片生成/图生图/Krea2洗图高质量4K_2077211215461441537.json, 图片生成/图生图/Krea2洗图高质量4K_2077214400984997890.json, 图片生成/图生图/Qwen 2509图像编辑模型-单图-自用_1989178834048126978.json, 图片生成/图生图/Qwen Image Edit 2511图生图_2026496059094077441.json, 图片生成/图生图/洗图Krea2-高质量4K_2076643574732640258.json, 图片生成/图生图/洗图Krea2-高质量4K_2088257533755613186.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_27

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Krea2-洗图流-无需反推_2110759558145732609.json、图片生成/图生图/Krea2洗图高质量4K_2077211215461441537.json、图片生成/图生图/Krea2洗图高质量4K_2077214400984997890.json、图片生成/图生图/Qwen 2509图像编辑模型-单图-自用_1989178834048126978.json、图片生成/图生图/Qwen Image Edit 2511图生图_2026496059094077441.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `TextEncodeKrea2OstrisEdit` —— 5/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `PrimitiveFloat` —— 4/7 个有
- `easy ifElse` —— 4/7 个有
- `TextEncodeQwenImageEditPlus` —— 2/7 个有
- `MuyeTextEditOutput` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler_ancestral | - | 7 | 57% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 0.7 | 0.6 - 1 | 7 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 0.7，观测区间 0.6 - 1，7 个样本，取值集中（一致性 81%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
