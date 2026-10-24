---
name: image_to_image_sampler_clip_unet_65
type: Image To Image
frequency: 7
level: weak
coverage: 0.952286
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image线稿控制图生图洗图 原图无限制_2004964164030398466.json, 图片生成/图生图/Z-image线稿控制图生图洗图2.0_2000496629763407873.json, 图片生成/图生图/Z-image线稿控制图生图洗图2.1_2001578550618648578.json, 图片生成/图生图/Z-image线稿控制图生图洗图_1996432211425501185.json, 图片生成/图生图/boogu 图生图_2069055979379060737.json, 图片生成/图生图/krea-2  图生图_2070080986699886593.json, 图片生成/图生图/去AI味洗图真实感_2018210512684720129.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_65

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Z-image线稿控制图生图洗图 原图无限制_2004964164030398466.json、图片生成/图生图/Z-image线稿控制图生图洗图2.0_2000496629763407873.json、图片生成/图生图/Z-image线稿控制图生图洗图2.1_2001578550618648578.json、图片生成/图生图/Z-image线稿控制图生图洗图_1996432211425501185.json、图片生成/图生图/boogu 图生图_2069055979379060737.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 5/7 个有
- `ModelPatchLoader` —— 5/7 个有
- `RH_Captioner` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `QwenImageDiffsynthControlnet` —— 4/7 个有
- `CR Text` —— 2/7 个有
- `PrimitiveFloat` —— 2/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `ZImageFunControlnet` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 50 | 7 | 1% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 27% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 0.2 | 0.16 - 1 | 7 | 9% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 50，7 个样本，取值分散，一致性仅 1%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 0.2，观测区间 0.16 - 1，7 个样本，取值分散，一致性仅 9%
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足
