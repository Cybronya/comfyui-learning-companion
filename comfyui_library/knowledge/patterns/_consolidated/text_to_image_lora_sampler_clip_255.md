---
name: text_to_image_lora_sampler_clip_255
type: Text To Image
frequency: 7
level: weak
coverage: 0.942429
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJv2, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RMBG, SAM3_Detect, SaveImage, TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2角色四视图生成工作流｜平替全能图片G2角色设计图生图_2088702240021368834.json, 图片生成/图生图/Krea2角色四视图｜全能图片G2平替角色设计图生图_2089029401555066881.json, 图片生成/图生图/全能图片G2平替｜Krea2角色四视图设计图生图_2096654681908015106.json, 图片生成/图生图/平替全能图片 G2｜Krea2 角色四视图工作流｜图生图_2096833300282306562.json, 图片生成/图生图/平替全能图片G2-角色四视图Krea2工作流_2092142218990669826.json, 图片生成/图生图/平替全能图片G2角色四视图Krea2图生图处理工作流_2102109884312543233.json, 图片生成/图生图/平替全能图片G2角色四视图｜Krea2工作流｜角色设计三视图直出_2101849939633598465.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_255

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Krea2角色四视图生成工作流｜平替全能图片G2角色设计图生图_2088702240021368834.json、图片生成/图生图/Krea2角色四视图｜全能图片G2平替角色设计图生图_2089029401555066881.json、图片生成/图生图/全能图片G2平替｜Krea2角色四视图设计图生图_2096654681908015106.json、图片生成/图生图/平替全能图片 G2｜Krea2 角色四视图工作流｜图生图_2096833300282306562.json、图片生成/图生图/平替全能图片G2-角色四视图Krea2工作流_2092142218990669826.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RMBG`
- `SAM3_Detect`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 6/7 个有
- `solarL_SaveImagesToZip` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `DrawMaskOnImage` —— 2/7 个有
- `MaskFillHoles` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `ResolutionSelector` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 7 | 57% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 69% |
| 采样算法 | er_sde | - | 7 | 86% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 1920 | 7 | 0% |
| 高度 | 80 | 80 - 1080 | 7 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 34/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 86%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1920，7 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1080，7 个样本，取值分散，一致性仅 0%
- 高发问题（34/7 个样本）：Steps较低可能导致细节不足
