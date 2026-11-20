---
name: text_to_image_lora_sampler_clip_423
type: Text To Image
frequency: 4
level: strong
coverage: 0.865
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, ImageLoader, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, RHHiddenNodes, SaveImage, UNETLoader, VAEDecode, VAELoader, WujiCleaner, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI表情包九宫格一键生成｜角色一致性表演图生图九连拍_2088693202395164673.json, 图片生成/图生图/AI表情包九宫格角色一致性角色表演图生图_2087478710202101761.json, 图片生成/图生图/IP写真九宫格变现｜Krea2影楼图生图全类型角色设计_2091310452017025025.json, 图片生成/图生图/旅游网红打卡写真九宫格｜Krea2影楼图生图全类型变现_2091278642277085186.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_423

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI表情包九宫格一键生成｜角色一致性表演图生图九连拍_2088693202395164673.json、图片生成/图生图/AI表情包九宫格角色一致性角色表演图生图_2087478710202101761.json、图片生成/图生图/IP写真九宫格变现｜Krea2影楼图生图全类型角色设计_2091310452017025025.json、图片生成/图生图/旅游网红打卡写真九宫格｜Krea2影楼图生图全类型变现_2091278642277085186.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageLoader`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `RHHiddenNodes`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WujiCleaner`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `WujiStyleSelector` —— 3/4 个有
- `AutoCropFaces` —— 2/4 个有
- `Krea2EditGroundedEncode` —— 2/4 个有
- `Krea2EditModelPatch` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `TextEncodeQwenImageEdit` —— 2/4 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `WujiSampler` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
