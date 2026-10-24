---
name: image_to_image_sampler_unet_vae_10
type: Image To Image
frequency: 13
level: moderate
coverage: 0.898154
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_image_Edit千问图片局部重绘2509版_1970742241134321665.json, 图片生成/图生图/Qwen一句话改变图片 单图编辑_1991781423713562626.json, 图片生成/图生图/ywt低价版1.0_2059986818820567041.json, 图片生成/图生图/ywt低价版2.0_2059997662291779585.json, 图片生成/图生图/ywt低价版3.0_2060024511612936194.json, 图片生成/图生图/ywt低价版4.0_2060256743405473793.json, 图片生成/图生图/ywt低价版5.0_2060394577848258561.json, 图片生成/图生图/☯️千问Edit_单图编辑_1972192308055764994.json, 图片生成/图生图/千问Edit 2509版 单图编辑_1983858753294471169.json, 图片生成/图生图/千问Edit-Plus局部精准编辑_1970474938392059905.json, 图片生成/图生图/千问Edit局部精准编辑_1965034120084602882.json, 图片生成/图生图/千问图片修改_2007817860055310337.json, 图片生成/图生图/🥯千问Edit 2509版 单图编辑【强化版】🥯_1971749678851289089.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen_image_Edit千问图片局部重绘2509版_1970742241134321665.json、图片生成/图生图/Qwen一句话改变图片 单图编辑_1991781423713562626.json、图片生成/图生图/ywt低价版1.0_2059986818820567041.json、图片生成/图生图/ywt低价版2.0_2059997662291779585.json、图片生成/图生图/ywt低价版3.0_2060024511612936194.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 12/13 个有
- `PreviewImage` —— 12/13 个有
- `TextEncodeQwenImageEditPlus` —— 11/13 个有
- `Image Comparer (rgthree)` —— 10/13 个有
- `CR Text` —— 9/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `TextEncodeQwenImageEdit` —— 6/13 个有
- `RH_Nano_Banana_Image2Image` —— 5/13 个有
- `LayerUtility: ImageReel` —— 4/13 个有
- `LayerUtility: ImageReelComposit` —— 4/13 个有
- `RH_RhartImageG2ImageToImage` —— 4/13 个有
- `CR Text Concatenate` —— 3/13 个有
- `INPAINT_MaskedFill` —— 3/13 个有
- `Mask Fill Holes` —— 3/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `RH_LLMAPI_NODE` —— 2/13 个有
- `MuyeTextEditOutput` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `easy promptConcat` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 13 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 13 | 53% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 0.72 - 1 | 13 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 0.72 - 1，13 个样本，取值集中（一致性 85%）
- 高发问题（19/13 个样本）：Steps较低可能导致细节不足
