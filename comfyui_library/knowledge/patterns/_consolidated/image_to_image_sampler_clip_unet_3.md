---
name: image_to_image_sampler_clip_unet_3
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8664
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LatentCutToBatch, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM V2, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss]
members: [图片生成/图生图/2026603437491757058.json, 图片生成/图生图/2091058647039307777.json, 图片生成/文生图/Qwen Layered 加强版_2073294146231685121.json, 图片生成/文生图/国内商品详情页生成（PSD分层保存）_2008783090499461121.json, 视频生成/图生视频/2011639539646865410.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2026603437491757058.json、图片生成/图生图/2091058647039307777.json、图片生成/文生图/Qwen Layered 加强版_2073294146231685121.json、图片生成/文生图/国内商品详情页生成（PSD分层保存）_2008783090499461121.json、视频生成/图生视频/2011639539646865410.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
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
- `GetImageSize` —— 4/5 个有
- `HAIGC_CombineUnits` —— 4/5 个有
- `HAIGC_Layer` —— 4/5 个有
- `HAIGC_SavePSD` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `Int` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `CR Text` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `PromptBatchQueue` —— 2/5 个有
- `RH_LLMAPI_Pro_Node` —— 2/5 个有
- `RH_Nano_Banana2_Image2Image` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `ShowText` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 40 | 5 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 37% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、SimpleMath+、LayerUtility: ImageScaleByAspectRatio V2、MathExpression|pysssss
