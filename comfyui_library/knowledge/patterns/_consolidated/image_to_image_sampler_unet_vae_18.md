---
name: image_to_image_sampler_unet_vae_18
type: Image To Image
frequency: 11
level: moderate
coverage: 0.879
common_nodes: [Image Comparer (rgthree), ImageResize+, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/87time # 33  QW 图生图_1988940448918016002.json, 图片生成/图生图/87time # 37 krea图生图_1988936794341257218.json, 图片生成/图生图/F2K-家具软装-材质迁移-材质替换_2057342903248314370.json, 图片生成/图生图/F2K-材质迁移-材质替换-双图编辑_2057284294703407106.json, 图片生成/图生图/FLUX.2·klein双图编辑_2035297860731805697.json, 图片生成/图生图/FLUX.2·klein多图编辑_2035923140114653186.json, 图片生成/图生图/Flux2-klein-图像编辑（单图）_2032355193949528065.json, 图片生成/图生图/Flux2-klein-图像编辑（单图）_2037862676570836993.json, 图片生成/图生图/Flux2-klein-图像编辑（单图）_2037876044539109377.json, 图片生成/图生图/flux2-klein编辑+高清修复_2013069939640377345.json, 平台全量/内部测试专用001（GQ）_2015103809042784258.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_18

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/87time # 33  QW 图生图_1988940448918016002.json、图片生成/图生图/87time # 37 krea图生图_1988936794341257218.json、图片生成/图生图/F2K-家具软装-材质迁移-材质替换_2057342903248314370.json、图片生成/图生图/F2K-材质迁移-材质替换-双图编辑_2057284294703407106.json、图片生成/图生图/FLUX.2·klein双图编辑_2035297860731805697.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 10/11 个有
- `CLIPTextEncode` —— 10/11 个有
- `ConditioningZeroOut` —— 10/11 个有
- `PreviewImage` —— 9/11 个有
- `ReferenceLatent` —— 9/11 个有
- `EmptyFlux2LatentImage` —— 6/11 个有
- `LatentUpscaleBy` —— 5/11 个有
- `easy imageColorMatch` —— 5/11 个有
- `LoraLoaderModelOnly` —— 4/11 个有
- `Anything Everywhere` —— 2/11 个有
- `Fast Groups Muter (rgthree)` —— 2/11 个有
- `ImageColorMatchAdobe+` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `CLIPTextEncodeFlux` —— 1/11 个有
- `DualCLIPLoader` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `RH_Translator` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 16 | 11 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 82% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 0.25 - 1 | 11 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 16，11 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 82%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，11 个样本
- 高发问题（14/11 个样本）：Steps较低可能导致细节不足
