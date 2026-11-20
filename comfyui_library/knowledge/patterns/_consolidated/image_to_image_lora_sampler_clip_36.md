---
name: image_to_image_lora_sampler_clip_36
type: Image To Image
frequency: 9
level: strong
coverage: 0.831889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LatentCutToBatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Layerd极速图像分层图生文生图二合一_2002311197057773569.json, 图片生成/图生图/Qwen-Image-Layered-图生图图像分层_2006004426303295489.json, 图片生成/图生图/Qwen-Image-layered图像分层(加速版)_2002561305687015425.json, 图片生成/图生图/Qwen_Image_Layerd加速分层图像【图生图】_2003447063511744514.json, 图片生成/图生图/图像分层QL_2008368744363466753.json, 图片生成/图生图/图像分层保存png格式-qwen-_2031997380366700546.json, 图片生成/图生图/图片分层Qwen Image Layered 八步加速·灵活切换层数_2004201844559806465.json, 图片生成/图生图/图片分层Qwen Image Layered 八步加速·灵活切换层数_2004436577822666753.json, 图片生成/图生图/图片前后分层Qwen Image Layered_2052023284954349569.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Layerd极速图像分层图生文生图二合一_2002311197057773569.json、图片生成/图生图/Qwen-Image-Layered-图生图图像分层_2006004426303295489.json、图片生成/图生图/Qwen-Image-layered图像分层(加速版)_2002561305687015425.json、图片生成/图生图/Qwen_Image_Layerd加速分层图像【图生图】_2003447063511744514.json、图片生成/图生图/图像分层QL_2008368744363466753.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LatentCutToBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 7/9 个有
- `MathExpression|pysssss` —— 7/9 个有
- `JWInteger` —— 6/9 个有
- `GetNode` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `VHS_VideoCombine` —— 4/9 个有
- `PrimitiveFloat` —— 3/9 个有
- `CR Text` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `LatentFromBatch` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 9 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
