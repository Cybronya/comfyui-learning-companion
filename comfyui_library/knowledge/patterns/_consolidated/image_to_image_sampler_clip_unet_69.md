---
name: image_to_image_sampler_clip_unet_69
type: Image To Image
frequency: 7
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, ImageScaleToTotalPixels, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/土狗0523V42_2055766889799921666.json, 图片生成/图生图/高清生成0509_2052830473717592065.json, 图片生成/图生图/黑兽Klein 9B BFS换脸V1_2036758096441253889.json, 图片生成/图生图/黑兽Klein 9B BFS换脸V1_2038144395391803393.json, 图片生成/图生图/黑兽Klein 9B BFS换脸工作流_2036780449925701634.json, 图片生成/图生图/（N SFW）N版黑兽Klein 9B BFS换脸V1_2038148176439418881.json, 图片生成/图生图/（自用）N版黑兽Klein 9B BFS换脸V1_2036837348155068417.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_69

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/土狗0523V42_2055766889799921666.json、图片生成/图生图/高清生成0509_2052830473717592065.json、图片生成/图生图/黑兽Klein 9B BFS换脸V1_2036758096441253889.json、图片生成/图生图/黑兽Klein 9B BFS换脸V1_2038144395391803393.json、图片生成/图生图/黑兽Klein 9B BFS换脸工作流_2036780449925701634.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/7 个有
- `GetImageSize` —— 5/7 个有
- `ImageConcatMulti` —— 5/7 个有
- `easy imageConcat` —— 4/7 个有
- `DuckHideNode` —— 2/7 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/7 个有
- `TT_img_enc` —— 2/7 个有
- `TT_img_enc_v2` —— 2/7 个有
- `ImageAddNoise` —— 1/7 个有
- `ReActorFaceBoost` —— 1/7 个有
- `ReActorFaceSwapOpt` —— 1/7 个有
- `ReActorOptions` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 20 | 7 | 27% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.35 | 7 | 86% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 20，7 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.35，7 个样本，取值集中（一致性 86%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
