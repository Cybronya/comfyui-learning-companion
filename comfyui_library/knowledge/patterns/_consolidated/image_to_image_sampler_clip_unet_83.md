---
name: image_to_image_sampler_clip_unet_83
type: Image To Image
frequency: 5
level: strong
coverage: 0.8506
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/一次性批量反推提示词+洗图_2053023047048802306.json, 图片生成/图生图/251207-04.Z-image+Qwen反推生图_1997712839517343745.json, 图片生成/图生图/LH-DMT版本-2.生图片类-024.Z-image+Qwen反推生图_2016484501077102593.json, 图片生成/图生图/YJ-APP-z-image-图生图_2031308137252265985.json, 图片生成/图生图/干问3反推洗图_1999295995408154626.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_83

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/一次性批量反推提示词+洗图_2053023047048802306.json、图片生成/图生图/251207-04.Z-image+Qwen反推生图_1997712839517343745.json、图片生成/图生图/LH-DMT版本-2.生图片类-024.Z-image+Qwen反推生图_2016484501077102593.json、图片生成/图生图/YJ-APP-z-image-图生图_2031308137252265985.json、图片生成/图生图/干问3反推洗图_1999295995408154626.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `AILab_QwenVL` —— 3/5 个有
- `Float` —— 2/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `Qwen3_VQA` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `ImpactMakeAnyList` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 5 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，5 个样本，取值集中（一致性 95%）
