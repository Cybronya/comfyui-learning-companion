---
name: text_to_image_lora_sampler_clip_149
type: Text To Image
frequency: 11
level: strong
coverage: 0.808091
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2角色四视图一键出图｜漫剧真人资产4步加速SeedVR2放大_2103036736904450049.json, 图片生成/图生图/Krea2角色漫剧真人资产四视图一键生成4步加速版 角色设定批量产出_2109007283790376962.json, 图片生成/图生图/Krea2角色漫剧真人资产四视图一键生成4步加速版 角色设定批量产出_2109012115167203329.json, 图片生成/图生图/Krea2角色漫剧真人资产四视图一键生成4步加速版 角色设定批量产出_2109065387508846593.json, 图片生成/图生图/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100678526088335362.json, 图片生成/图生图/Krea2角色资产四视图一键生成4步加速版｜漫剧真人通用，图生图设定图秒出_2100523405962465281.json, 图片生成/图生图/Krea2角色资产四视图一键生成，漫剧真人素材SeedVR2高清放大4步加速版_2103174258447962113.json, 图片生成/图生图/一键转Q版V1｜人物角色萌系图生图直出转绘_2090154456955580418.json, 图片生成/图生图/一键转Q版工作流V1｜人物角色萌系图生图_2090426732053614594.json, 图片生成/图生图/角色漫剧加真人资产四视图一键生成Krea2工作流，图生图角色设计工具_2106892222200377346.json, 图片生成/图生图/角色漫剧加真人资产四视图一键生成Krea2工作流，图生图角色设计工具_2108745674354413570.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_149

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Krea2角色四视图一键出图｜漫剧真人资产4步加速SeedVR2放大_2103036736904450049.json、图片生成/图生图/Krea2角色漫剧真人资产四视图一键生成4步加速版 角色设定批量产出_2109007283790376962.json、图片生成/图生图/Krea2角色漫剧真人资产四视图一键生成4步加速版 角色设定批量产出_2109012115167203329.json、图片生成/图生图/Krea2角色漫剧真人资产四视图一键生成4步加速版 角色设定批量产出_2109065387508846593.json、图片生成/图生图/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100678526088335362.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/11 个有
- `EmptySD3LatentImage` —— 9/11 个有
- `Krea2EditGroundedEncode` —— 9/11 个有
- `Krea2EditModelPatch` —— 9/11 个有
- `SeedVR2LoadDiTModel` —— 6/11 个有
- `SeedVR2LoadVAEModel` —— 6/11 个有
- `SeedVR2VideoUpscaler` —— 6/11 个有
- `Any Switch (rgthree)` —— 4/11 个有
- `ImpactInt` —— 4/11 个有
- `KepStringLiteral` —— 3/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `Image Comparer (rgthree)` —— 2/11 个有
- `ImageScaleToTotalPixels` —— 2/11 个有
- `MuyeTextEditOutput` —— 2/11 个有
- `TextEncodeQwenImageEditPlus` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `easy imageConcat` —— 2/11 个有
- `EmptyImage` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
