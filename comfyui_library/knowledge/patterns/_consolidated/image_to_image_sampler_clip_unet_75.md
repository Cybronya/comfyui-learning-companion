---
name: image_to_image_sampler_clip_unet_75
type: Image To Image
frequency: 7
level: strong
coverage: 0.870714
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/04.Z-image+Qwen反推生图_2021191050152382465.json, 图片生成/反推提示词/一次性批量反推提示词+洗图_2053023047048802306.json, 图片生成/图生图/251207-04.Z-image+Qwen反推生图_1997712839517343745.json, 图片生成/图生图/LH-DMT版本-2.生图片类-024.Z-image+Qwen反推生图_2016484501077102593.json, 图片生成/图生图/YJ-APP-z-image-图生图_2031308137252265985.json, 图片生成/图生图/干问3反推洗图_1999295995408154626.json, 平台全量/【去AI感】增强细节反推工作流_2072519528290021377.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/04.Z-image+Qwen反推生图_2021191050152382465.json、图片生成/反推提示词/一次性批量反推提示词+洗图_2053023047048802306.json、图片生成/图生图/251207-04.Z-image+Qwen反推生图_1997712839517343745.json、图片生成/图生图/LH-DMT版本-2.生图片类-024.Z-image+Qwen反推生图_2016484501077102593.json、图片生成/图生图/YJ-APP-z-image-图生图_2031308137252265985.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ImpactInt` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `Qwen3_VQA` —— 4/7 个有
- `AILab_QwenVL` —— 3/7 个有
- `LayerUtility: ImageReel` —— 3/7 个有
- `LayerUtility: ImageReelComposit` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `Float` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `ImpactMakeAnyList` —— 1/7 个有
- `JoinStrings` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `TextInput_` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.7 - 1 | 7 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，7 个样本，取值集中（一致性 89%）
