---
name: image_to_image_sampler_unet_vae_25
type: Image To Image
frequency: 9
level: moderate
coverage: 0.820444
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen去水印_1986102218543824897.json, 图片生成/图生图/Z image 图生图（洗图）_1993888000021037058.json, 图片生成/图生图/Z-IMAGE 快速洗图PS版本_1980163824957427714.json, 图片生成/图生图/Z-Image 图生图细节增强版_2015750867261071362.json, 图片生成/图生图/Z-Image图生图（细节增强版）_2020347508572037121.json, 图片生成/图生图/Z-image 超真实感 洗图_1993895502299283457.json, 图片生成/图生图/Z-image-turbo 图生图 洗图 ai变真人_1982650838457958402.json, 图片生成/图生图/Z-image图生图最强图生图洗图新玩法_1993890648885575682.json, 图片生成/图生图/全能图片2.0+Z-Image图生图（细节增强版）_2033800127114125314.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_25

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen去水印_1986102218543824897.json、图片生成/图生图/Z image 图生图（洗图）_1993888000021037058.json、图片生成/图生图/Z-IMAGE 快速洗图PS版本_1980163824957427714.json、图片生成/图生图/Z-Image 图生图细节增强版_2015750867261071362.json、图片生成/图生图/Z-Image图生图（细节增强版）_2020347508572037121.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 8/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `CR Text` —— 5/9 个有
- `PrimitiveInt` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 9 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 9 | 72% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 56% |
| 重绘幅度 | 0.4 | 0.2 - 1 | 9 | 43% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 56%
- 重绘幅度 中位数 0.4，观测区间 0.2 - 1，9 个样本，取值分散，一致性仅 43%
