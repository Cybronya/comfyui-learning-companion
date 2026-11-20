---
name: text_to_image_sampler_clip_unet_47
type: Text To Image
frequency: 13
level: weak
coverage: 0.847077
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2_Turbo反推提示词生图_2071103038554726401.json, 图片生成/文生图/Krea2_Turbo生图（无审查版）_2071109949048053761.json, 图片生成/文生图/Krea2_写实人像_2083068524297277442.json, 图片生成/文生图/Krea2_写实人像（双采版）_2071137932169269249.json, 图片生成/文生图/Krea2_写实人像（双采版）_2077640931263737858.json, 图片生成/文生图/Krea2_写实人像（双采版）_2079377240273547266.json, 图片生成/文生图/Krea2_写实人像（双采版）_2087070012069736450.json, 图片生成/文生图/Krea2_写实人像（双采版）_2087380793143422978.json, 图片生成/文生图/Krea2人物四视图工作流，人物角色角色设计文生图工具_2107516751167713281.json, 图片生成/文生图/Krea2双图编辑完美替换｜文生图图生图堪比闭源_2090473972126273538.json, 图片生成/文生图/Krea2局部重绘移除｜精准无缝融合文生图图生图_2090464406776926210.json, 图片生成/文生图/双图编辑完美替换｜Krea2文生图图生图处理_2090192438358011906.json, 视频生成/文生视频/单图编辑完美一致性｜Krea2文生图图生视频生成_2090203681751912449.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_47

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Krea2_Turbo反推提示词生图_2071103038554726401.json、图片生成/文生图/Krea2_Turbo生图（无审查版）_2071109949048053761.json、图片生成/文生图/Krea2_写实人像_2083068524297277442.json、图片生成/文生图/Krea2_写实人像（双采版）_2071137932169269249.json、图片生成/文生图/Krea2_写实人像（双采版）_2077640931263737858.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 10/13 个有
- `ResolutionSelector` —— 10/13 个有
- `ConditioningZeroOut` —— 9/13 个有
- `孤海注释` —— 7/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `JjkText` —— 5/13 个有
- `solarL_SaveImagesToZip` —— 5/13 个有
- `EmptySD3LatentImage` —— 4/13 个有
- `ImageScaleToTotalPixels` —— 4/13 个有
- `Krea2EditGroundedEncode` —— 4/13 个有
- `Krea2EditModelPatch` —— 4/13 个有
- `LoadImage` —— 4/13 个有
- `Seed (rgthree)` —— 4/13 个有
- `VAEEncode` —— 4/13 个有
- `GetImageSize+` —— 2/13 个有
- `Label (rgthree)` —— 2/13 个有
- `DrawMaskOnImage` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `PreviewImage` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 13 | 31% |
| 高度 | 1024 | 80 - 1024 | 13 | 31% |
| 采样步数 | 4 | 4 - 12 | 13 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 13 | 27% |
| 采样算法 | euler | - | 13 | 62% |
| 调度器 | sgm_uniform | - | 13 | 46% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，13 个样本，取值分散，一致性仅 31%
- 高度 中位数 1024，观测区间 80 - 1024，13 个样本，取值分散，一致性仅 31%
- 采样步数 中位数 4，观测区间 4 - 12，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，13 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，13 个样本，一致性 62%
- 调度器 最常用 sgm_uniform，13 个样本，一致性 46%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（18/13 个样本）：Steps较低可能导致细节不足
