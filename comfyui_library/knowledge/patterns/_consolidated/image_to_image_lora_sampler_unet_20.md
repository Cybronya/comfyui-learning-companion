---
name: image_to_image_lora_sampler_unet_20
type: Image To Image
frequency: 20
level: strong
coverage: 0.88815
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键换衣 OOTD 3.0【 edit 2511 最新版 】_2010296531844337665.json, 图片生成/图生图/一键换装 女装童装 小红书电商带货_2087841507427573761.json, 图片生成/图生图/千问编辑2511-人物多角度出图_2039933028406923265.json, 图片生成/图生图/千问编辑2511-人物多角度出图_2059908761376083970.json, 图片生成/图生图/小红书8步加速换装FireRed-Image-edit1.1_2030823318718259202.json, 图片生成/图生图/小红书FireRed Image Edit 1.1 多图编辑加速版｜模特换装｜换场景｜换颜色_2049307280159547394.json, 图片生成/图生图/小红书FireRed-Image-edit 单图双图多图编辑 换装迁移_2031243779381923842.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 单图双图三图编辑_2029911022823280641.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑_2031635950748569602.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑（文字排版参考）_2029575105692573697.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑（文字排版参考）_2030166401742282754.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 文字排版_2029759015185551362.json, 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致性）_2029575084368728065.json, 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致性）_2029727437268979713.json, 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致）_2029741910889336833.json, 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑（换装）_2029575073815863298.json, 图片生成/图生图/小红书FireRed-Image-edit1.1图像编辑（妆容迁移）_2029575093277433858.json, 图片生成/图生图/小红书FireRed-Image-edit1.1妆容迁移_2029746671227248641.json, 图片生成/图生图/小红书FireRed批量换装_2046756130541539330.json, 图片生成/图生图/（好用）小红书FireRed-Image-edit1.1双图编辑（情趣换装）_2030162350132695041.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_20

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/一键换衣 OOTD 3.0【 edit 2511 最新版 】_2010296531844337665.json、图片生成/图生图/一键换装 女装童装 小红书电商带货_2087841507427573761.json、图片生成/图生图/千问编辑2511-人物多角度出图_2039933028406923265.json、图片生成/图生图/千问编辑2511-人物多角度出图_2059908761376083970.json、图片生成/图生图/小红书8步加速换装FireRed-Image-edit1.1_2030823318718259202.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 18/20 个有
- `CR Prompt Text` —— 17/20 个有
- `easy int` —— 17/20 个有
- `FluxKontextImageScale` —— 15/20 个有
- `Image Comparer (rgthree)` —— 15/20 个有
- `easy cleanGpuUsed` —— 15/20 个有
- `Any Switch (rgthree)` —— 13/20 个有
- `PreviewImage` —— 13/20 个有
- `Fast Groups Muter (rgthree)` —— 8/20 个有
- `ImageResizeKJv2` —— 3/20 个有
- `ImageConcatMulti` —— 2/20 个有
- `Fast Groups Bypasser (rgthree)` —— 1/20 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/20 个有
- `HAIGC_LoadImagesFromZip` —— 1/20 个有
- `RHHiddenNodes` —— 1/20 个有
- `RH_BatchImages` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 20 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，20 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
