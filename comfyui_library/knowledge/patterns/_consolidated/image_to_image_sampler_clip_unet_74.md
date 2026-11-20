---
name: image_to_image_sampler_clip_unet_74
type: Image To Image
frequency: 6
level: moderate
coverage: 0.834333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, ImageConcanate, ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingAuraFlow, PrimitiveBoolean, RH_Captioner, SaveImage, TextBox, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-最强洗图，图片反推_1955627326294802433.json, 图片生成/图生图/Qwen-image-最强洗图，图片反推_2072636991648391169.json, 图片生成/图生图/Qwen-image-洗图，图片反推，海报反推_1953660779788685313.json, 图片生成/图生图/Qwen-image-洗图，图片反推，海报反推_1953677808759394305.json, 图片生成/图生图/Qwen-image-洗图，图片反推，海报反推_1954523307045470210.json, 图片生成/图生图/Qwen-image洗图，图片反推，海报反推-4步极速出图_1957647598595272705.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_74

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-image-最强洗图，图片反推_1955627326294802433.json、图片生成/图生图/Qwen-image-最强洗图，图片反推_2072636991648391169.json、图片生成/图生图/Qwen-image-洗图，图片反推，海报反推_1953660779788685313.json、图片生成/图生图/Qwen-image-洗图，图片反推，海报反推_1953677808759394305.json、图片生成/图生图/Qwen-image-洗图，图片反推，海报反推_1954523307045470210.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `ImageConcanate`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PrimitiveBoolean`
- `RH_Captioner`
- `SaveImage`
- `TextBox`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 6 | 63% |
| Prompt 约束强度(CFG) | 3.7 | 1 - 4 | 6 | 68% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.46 - 1 | 6 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，6 个样本
- Prompt 约束强度(CFG) 中位数 3.7，观测区间 1 - 4，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.46 - 1，6 个样本
