---
name: image_to_image_sampler_clip_unet_47
type: Image To Image
frequency: 10
level: weak
coverage: 0.9562
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image线稿控制图生图洗图 原图无限制_2004964164030398466.json, 图片生成/图生图/Z-image线稿控制图生图洗图2.0_2000496629763407873.json, 图片生成/图生图/Z-image线稿控制图生图洗图2.1_2001578550618648578.json, 图片生成/图生图/Z-image线稿控制图生图洗图_1996432211425501185.json, 图片生成/图生图/boogu 图生图_2069055979379060737.json, 图片生成/图生图/krea-2  图生图_2070080986699886593.json, 图片生成/图生图/去AI味洗图真实感_2018210512684720129.json, 平台全量/Qwen Cn控制工作流！_1958890669618180097.json, 平台全量/Qwen inpaint局部重绘工作流_1959239225361248258.json, 平台全量/Qwen 毛坯转效果图_1959992091625598977.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_47

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Z-image线稿控制图生图洗图 原图无限制_2004964164030398466.json、图片生成/图生图/Z-image线稿控制图生图洗图2.0_2000496629763407873.json、图片生成/图生图/Z-image线稿控制图生图洗图2.1_2001578550618648578.json、图片生成/图生图/Z-image线稿控制图生图洗图_1996432211425501185.json、图片生成/图生图/boogu 图生图_2069055979379060737.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelPatchLoader` —— 8/10 个有
- `AIO_Preprocessor` —— 7/10 个有
- `ConditioningZeroOut` —— 7/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `QwenImageDiffsynthControlnet` —— 7/10 个有
- `RH_Captioner` —— 5/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `CFGNorm` —— 3/10 个有
- `ModelSamplingAuraFlow` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `Mask Fill Holes` —— 1/10 个有
- `ZImageFunControlnet` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 6 - 50 | 10 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 31% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 50% |
| 重绘幅度 | 0.55 | 0.16 - 1 | 10 | 30% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 6 - 50，10 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 50%
- 重绘幅度 中位数 0.55，观测区间 0.16 - 1，10 个样本，取值分散，一致性仅 30%
- 高发问题（13/10 个样本）：Steps较低可能导致细节不足
