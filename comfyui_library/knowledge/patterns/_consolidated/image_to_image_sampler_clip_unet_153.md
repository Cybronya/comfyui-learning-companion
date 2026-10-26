---
name: image_to_image_sampler_clip_unet_153
type: Image To Image
frequency: 3
level: strong
coverage: 0.980667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ImageScaleToTotalPixels, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/（N SFW）N版黑兽Klein 9B BFS换脸V1_2038148176439418881.json, 图片生成/图生图/（自用）N版黑兽Klein 9B BFS换脸V1_2036837348155068417.json, 视频生成/图生视频/图片人物替换v3_2045799608449769473.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_153

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/（N SFW）N版黑兽Klein 9B BFS换脸V1_2038148176439418881.json、图片生成/图生图/（自用）N版黑兽Klein 9B BFS换脸V1_2036837348155068417.json、视频生成/图生视频/图片人物替换v3_2045799608449769473.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
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
- `CR Prompt Text` —— 2/3 个有
- `DuckHideNode` —— 2/3 个有
- `TT_img_enc` —— 2/3 个有
- `TT_img_enc_v2` —— 2/3 个有
- `FaceHandCrop` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `PowerfulColorAlignment` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RMBG` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
