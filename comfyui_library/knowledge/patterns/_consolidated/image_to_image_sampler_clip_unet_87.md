---
name: image_to_image_sampler_clip_unet_87
type: Image To Image
frequency: 5
level: strong
coverage: 0.873
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX2-LONGCAT图像编辑【教学】工作流_1998921046315126785.json, 图片生成/图生图/Flux  kontext 老照片修复_1940415172613926913.json, 图片生成/图生图/Flux Kontext本地部署_1939329294118338561.json, 图片生成/图生图/Kontext Dev 模型｜多人场景动作融合_1938995027278548994.json, 图片生成/图生图/flux-kontext-生成爆款手办_1964682155462901762.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_87

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX2-LONGCAT图像编辑【教学】工作流_1998921046315126785.json、图片生成/图生图/Flux  kontext 老照片修复_1940415172613926913.json、图片生成/图生图/Flux Kontext本地部署_1939329294118338561.json、图片生成/图生图/Kontext Dev 模型｜多人场景动作融合_1938995027278548994.json、图片生成/图生图/flux-kontext-生成爆款手办_1964682155462901762.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `DeepTranslatorTextNode` —— 3/5 个有
- `FluxKontextImageScale` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `ImageStitch` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `CLIPLoader` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `LayerMask: BiRefNetUltraV2` —— 1/5 个有
- `LayerMask: LoadBiRefNetModel` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LongCatImageEdit` —— 1/5 个有
- `LongCatImageModelLoader` —— 1/5 个有
- `NunchakuFluxDiTLoader` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
