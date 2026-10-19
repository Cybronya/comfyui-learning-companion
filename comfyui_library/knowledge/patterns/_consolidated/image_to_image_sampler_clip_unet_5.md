---
name: image_to_image_sampler_clip_unet_5
type: Image To Image
frequency: 3
level: moderate
coverage: 0.844667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, HAIGC_CombineUnits, HAIGC_Layer, HAIGC_SavePSD, KSampler, LatentCutToBatch, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM V2, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss]
members: [图片生成/图生图/2026603437491757058.json, 图片生成/图生图/2091058647039307777.json, 视频生成/图生视频/2011639539646865410.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2026603437491757058.json、图片生成/图生图/2091058647039307777.json、视频生成/图生视频/2011639539646865410.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `HAIGC_CombineUnits`
- `HAIGC_Layer`
- `HAIGC_SavePSD`
- `KSampler`
- `LatentCutToBatch`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `Int` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `PromptBatchQueue` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `RH_Nano_Banana2_Image2Image` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 40 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、SimpleMath+、LayerUtility: ImageScaleByAspectRatio V2、MathExpression|pysssss
