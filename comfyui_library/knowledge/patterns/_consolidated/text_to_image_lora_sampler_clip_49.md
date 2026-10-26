---
name: text_to_image_lora_sampler_clip_49
type: Text To Image
frequency: 17
level: strong
coverage: 0.837588
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/角色资产4格图免提示词 Qwen-Image2.1放大处理工具_2113405844221157377.json, 图片生成/图生图/4K图像高清放大｜seedvr 2图生图一键提升画质_2092156503158517761.json, 图片生成/图生图/4K图像高清放大｜seedvr_2图生图一键提升画质_2092605288389111810.json, 图片生成/图生图/AI换装双图试穿工作流｜Qwen-Image_2.1智能提示词｜服装上身效果图秒出_2112076955049873410.json, 图片生成/图生图/FLUX 3 Image Klein图像编辑，图片换背景图生图_2111961472422203393.json, 图片生成/图生图/FLUX 3 Image Klein图像编辑｜换背景抠图一站式处理_2111754100328189953.json, 图片生成/图生图/FLUX 3 Image Klein官方版 图像编辑换背景处理工具_2113355640738508801.json, 图片生成/图生图/Flux3-klein常规图像编辑PUP增强版｜图生图精修更稳_2111740631423995905.json, 图片生成/图生图/MiniMax H3人像参考图专用生成器 人像图生图处理工具_2113024918748225538.json, 图片生成/图生图/Minimax H3人像参考图专用生成器｜写真质感一图即出_2112823108011909121.json, 图片生成/图生图/Moss Prompt文生图图生图 双模式图像生成处理工具_2114135139465908225.json, 图片生成/图生图/Qwen Image 2.1 V2编辑版，图生图处理优化升级方案_2103241696493531137.json, 图片生成/图生图/Qwen Image 2.1全能图片编辑加官方提示词强化，图生图处理质量提升_2103266944416833538.json, 图片生成/图生图/Qwen Image 2.1全能图片编辑官方提示词强化处理工具_2102552758141411330.json, 图片生成/图生图/Qwen-Image2.1全能图片编辑｜官方提示词强化改图更听话_2112932549029879810.json, 图片生成/文生图/MOSS SFT角色设计文生图 NB级图像生成处理工具_2114090024579981314.json, 图片生成/文生图/MOSS-Prompt RH版角色定妆照生成，文生图人设立绘质感精致_2114475089633828865.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_49

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/反推提示词/角色资产4格图免提示词 Qwen-Image2.1放大处理工具_2113405844221157377.json、图片生成/图生图/4K图像高清放大｜seedvr 2图生图一键提升画质_2092156503158517761.json、图片生成/图生图/4K图像高清放大｜seedvr_2图生图一键提升画质_2092605288389111810.json、图片生成/图生图/AI换装双图试穿工作流｜Qwen-Image_2.1智能提示词｜服装上身效果图秒出_2112076955049873410.json、图片生成/图生图/FLUX 3 Image Klein图像编辑，图片换背景图生图_2111961472422203393.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 16/17 个有
- `孤海注释` —— 16/17 个有
- `PrimitiveStringMultiline` —— 15/17 个有
- `ComfySwitchNode` —— 12/17 个有
- `ResolutionSelector` —— 11/17 个有
- `SeedVR2LoadDiTModel` —— 11/17 个有
- `SeedVR2LoadVAEModel` —— 11/17 个有
- `SeedVR2VideoUpscaler` —— 11/17 个有
- `Image Comparer (rgthree)` —— 10/17 个有
- `ImageScaleToTotalPixels` —— 10/17 个有
- `TextGenerate` —— 10/17 个有
- `BatchImagesNode` —— 9/17 个有
- `PreviewAny` —— 8/17 个有
- `QwenImage21Cache` —— 8/17 个有
- `TextEncodeQwenImage21` —— 8/17 个有
- `EmptyFlux2LatentImage` —— 7/17 个有
- `PreviewImage` —— 7/17 个有
- `PrimitiveBoolean` —— 7/17 个有
- `Fast Groups Bypasser (rgthree)` —— 5/17 个有
- `ReferenceMultiLatent` —— 4/17 个有
- `RegexExtract` —— 4/17 个有
- `INTConstant` —— 3/17 个有
- `ShowAnything|Mie` —— 3/17 个有
- `SkipLayerGuidanceDiTSimple` —— 3/17 个有
- `StringFormat` —— 3/17 个有
- `ConditioningZeroOut` —— 2/17 个有
- `RH_LLMAPI_Pro_Node` —— 2/17 个有
- `easy saveText` —— 2/17 个有
- `FastGroupsBypassSwitch` —— 1/17 个有
- `PrimitiveInt` —— 1/17 个有
- `SaveImageAdvanced` —— 1/17 个有
- `StringConcatenate` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（18/17 个样本）：Steps较低可能导致细节不足
