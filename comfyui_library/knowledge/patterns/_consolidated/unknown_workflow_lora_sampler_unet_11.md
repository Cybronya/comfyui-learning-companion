---
name: unknown_workflow_lora_sampler_unet_11
type: Unknown Workflow
frequency: 31
level: strong
coverage: 0.839935
common_nodes: [CLIPLoader, ConditioningZeroOut, Flux2KleinEditTextEncode_EditUtils, GetImageSize, INTConstant, KSampler, LCSColorAnchor, LCSLoadData, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LoadImage, LoraLoaderModelOnly, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/4K零变形高清修复Klein+TTP+ 去除AI感_2081195988076810242.json, 图片生成/图生图/4K高清修复  Klein+TTP 去除AI塑料感_2075023047899303937.json, 图片生成/图生图/Flux-2-Klein-9B去AI感人像精修+高清放大+-去油腻修复皮肤质感+去除脏污+噪点+油腻_2093321576824528898.json, 图片生成/图生图/Flux-2-Klein-9B去AI感人像精修+高清放大+-去油腻修复皮肤质感+去除脏污+噪点+油腻_2097162390164041730.json, 图片生成/图生图/Flux-2-Klein-9B去AI感人像精修+高清放大+-去油腻修复皮肤质感+去除脏污+噪点+油腻_2097502199990538242.json, 图片生成/图生图/HD Restoration图片高清放大变清晰分块放大SeedVR2.5+++TTP_2098214253705650177.json, 图片生成/图生图/High-Definition Restorati4K零变形高清修复Klein+TTP++去除AI感_2094242010805919745.json, 图片生成/图生图/Klein+TTP 零变形高清修复 4K_2061263969981124609.json, 图片生成/图生图/Klein+TTP 零变形高清修复 4K_2061390459804667905.json, 图片生成/图生图/Klein+TTP 零变形高清修复 4K_2064903373018714114.json, 图片生成/图生图/Klein+TTP 高清修复 4K_2060227055467450370.json, 图片生成/图生图/Klein+TTP+零变形高清修复+4K (1)_2067496500036464641.json, 图片生成/图生图/Klein+TTP+零变形高清修复+4K_2061256324096286722.json, 图片生成/图生图/Klein+TTP_零变形高清修复_4K_2060902117925277698.json, 图片生成/图生图/Klein+TTP_零变形高清修复_4K_2061257595431768066.json, 图片生成/图生图/TPP人像精修_2079206858736365570.json, 图片生成/图生图/TPP人像精修_2081983712404787202.json, 图片生成/图生图/TPP高清放大-人像精修_2082288270473523201.json, 图片生成/图生图/TPP高清放大-人像精修_2082295189032497154.json, 图片生成/图生图/klein+TTP放大_2066751659522478081.json, 图片生成/图生图/修到4K脸却变了？这套零变形方案，毛孔都清晰人还不走样_2060418252785934337.json, 图片生成/图生图/图片超清放大（ZLTD）_2069606120322330625.json, 图片生成/图生图/图片高清！_去AI感去油！Klein+TTP！_2100194646679969793.json, 图片生成/图生图/图片高清！_去AI感去油！Klein+TTP！_2100855956463767553.json, 图片生成/图生图/图片高清！_去AI感去油！Klein+TTP！_2101126416896188418.json, 图片生成/图生图/放大去AI感_增加皮肤纹理_Klein+TTP+零变形高清修复+4K_2072593896399532034.json, 图片生成/图生图/放大去AI感_增加皮肤纹理_Klein+TTP+零变形高清修复+4K_2072950870114918402.json, 图片生成/图生图/放大去AI感_增加皮肤纹理_Klein+TTP+零变形高清修复4K_2073222622690758657.json, 图片生成/图生图/无变形高清修复 4K_2071616768271011842.json, 图片生成/图生图/超好用🔥零变形高清放大修复-4K-最新_2066457945453453314.json, 数字人/数字人/图片高清！ 去AI感去油！Klein+TTP！_2100028593916170242.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_11

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（图片生成/图生图/4K零变形高清修复Klein+TTP+ 去除AI感_2081195988076810242.json、图片生成/图生图/4K高清修复  Klein+TTP 去除AI塑料感_2075023047899303937.json、图片生成/图生图/Flux-2-Klein-9B去AI感人像精修+高清放大+-去油腻修复皮肤质感+去除脏污+噪点+油腻_2093321576824528898.json、图片生成/图生图/Flux-2-Klein-9B去AI感人像精修+高清放大+-去油腻修复皮肤质感+去除脏污+噪点+油腻_2097162390164041730.json、图片生成/图生图/Flux-2-Klein-9B去AI感人像精修+高清放大+-去油腻修复皮肤质感+去除脏污+噪点+油腻_2097502199990538242.json…）

- **类型**：Unknown Workflow
- **样本数**：31
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 31 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Flux2KleinEditTextEncode_EditUtils`
- `GetImageSize`
- `INTConstant`
- `KSampler`
- `LCSColorAnchor`
- `LCSLoadData`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 30/31 个有
- `Image Comparer (rgthree)` —— 30/31 个有
- `MemoryCleaner` —— 30/31 个有
- `PreviewImage` —— 30/31 个有
- `SaveImage` —— 30/31 个有
- `SetNode` —— 30/31 个有
- `MathExpression|pysssss` —— 25/31 个有
- `LCSSharpnessCalibrate` —— 11/31 个有
- `LCSSharpnessIntervene` —— 11/31 个有
- `GoohaiAnyExists` —— 2/31 个有
- `EmptyImage` —— 1/31 个有
- `JjkText` —— 1/31 个有
- `KOOK_ImageCompression` —— 1/31 个有
- `KOOK_SaveJPGImage` —— 1/31 个有
- `RHHiddenNodes` —— 1/31 个有
- `easy showAnything` —— 1/31 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 31 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 31 | 100% |
| 采样算法 | euler | - | 31 | 90% |
| 调度器 | simple | - | 31 | 84% |
| 重绘幅度 | 1 | 1 - 1 | 31 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/31 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，31 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，31 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，31 个样本，一致性 90%
- 调度器 最常用 simple，31 个样本，一致性 84%
- 重绘幅度 中位数 1，观测区间 1 - 1，31 个样本，取值集中（一致性 100%）
- 高发问题（31/31 个样本）：Steps较低可能导致细节不足
