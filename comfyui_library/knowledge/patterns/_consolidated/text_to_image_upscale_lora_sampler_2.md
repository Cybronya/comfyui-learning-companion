---
name: text_to_image_upscale_lora_sampler_2
type: Text To Image
frequency: 20
level: weak
coverage: 0.8722
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2+zimage+flux2-klein三采极致洗图工作流_2074299116301152258.json, 图片生成/图生图/mj风格美学-图生图反推仿图-zimage双采样4k高清_2079745419407613954.json, 图片生成/图生图/zimage双采样-图生图反推仿图-MJ风格美学-4k高清_2080247747168530434.json, 图片生成/图生图/万能无损4K高清放大_人像皮肤细节增强真实感优化工作流_2085624260873244674.json, 图片生成/图生图/万能无损4K高清放大_人像皮肤细节增强真实感优化工作流_2085638324873687042.json, 图片生成/图生图/三采样高质量生图（可洗图）Krea2 + Z-Image Turbo + Flux2-Klein_2073570611582033922.json, 图片生成/图生图/产品精修增加细节高清处理_AI一键画质增强优化工作流_2085622556278738945.json, 图片生成/图生图/产品精修增加细节高清处理_AI一键画质增强优化工作流_2085632911126122498.json, 图片生成/图生图/图像反推 图生图 krea2+Klein+zimage  适合于 高清修复 图片反推_2072716298559246338.json, 图片生成/图生图/图像模仿洗图-高质量三采样-krea2+Klein+zimage_2072881381113417730.json, 图片生成/图生图/图像模仿洗图-高质量三采样-krea2+Klein+zimage_2075139075983630338.json, 图片生成/图生图/极致美学 人物模特 皮肤质感细化 图像模仿洗图-高质量三采样-krea2+Klein+zimage_2079034737200549890.json, 图片生成/图生图/洗图 图像反推  多功能优化 Krea2 - Zimage - Klein + 高清放大_2075393317843587073.json, 图片生成/文生图/Krea2 + Flux2-Klein文生图_2096577029973041153.json, 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2071552520446636033.json, 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2071597722657968129.json, 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2088834570824273922.json, 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模王炸合体_2071802083606618114.json, 图片生成/文生图/三模合体王炸｜Krea2+Z-Image Turbo+Flux2-Klein 文生图_2089298165005639682.json, 图片生成/文生图/极致美学高清生成｜Z-Image MJ风格版文生图制作_2096334353323347969.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/Krea2+zimage+flux2-klein三采极致洗图工作流_2074299116301152258.json、图片生成/图生图/mj风格美学-图生图反推仿图-zimage双采样4k高清_2079745419407613954.json、图片生成/图生图/zimage双采样-图生图反推仿图-MJ风格美学-4k高清_2080247747168530434.json、图片生成/图生图/万能无损4K高清放大_人像皮肤细节增强真实感优化工作流_2085624260873244674.json、图片生成/图生图/万能无损4K高清放大_人像皮肤细节增强真实感优化工作流_2085638324873687042.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 17/20 个有
- `easy cleanGpuUsed` —— 17/20 个有
- `easy imageSize` —— 17/20 个有
- `CR Text` —— 15/20 个有
- `PreviewImage` —— 15/20 个有
- `CLIPLoaderGGUF` —— 12/20 个有
- `Fast Groups Bypasser (rgthree)` —— 12/20 个有
- `LoadImage` —— 12/20 个有
- `TTResolutionSelector` —— 12/20 个有
- `RH_LLMAPI_Pro_Node` —— 8/20 个有
- `easy showAnything` —— 8/20 个有
- `JjkText` —— 7/20 个有
- `Label (rgthree)` —— 6/20 个有
- `solarL_SaveImagesToZip` —— 6/20 个有
- `GetImageSize+` —— 3/20 个有
- `ImageCASharpening+` —— 3/20 个有
- `Int` —— 3/20 个有
- `PhotoShakeNode` —— 3/20 个有
- `RunningHub Deepcleaner` —— 3/20 个有
- `孤海注释` —— 3/20 个有
- `PrimitiveFloat` —— 2/20 个有
- `easy anythingIndexSwitch` —— 2/20 个有
- `AIO_Preprocessor` —— 1/20 个有
- `ConditioningKrea2Rebalance` —— 1/20 个有
- `Krea2ControlApply` —— 1/20 个有
- `Krea2ControlImageEncode` —— 1/20 个有
- `Krea2ControlLoRALoader` —— 1/20 个有
- `NIX_SwitchAnything` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 10 | 20 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 20 | 22% |
| 采样算法 | euler | - | 20 | 70% |
| 调度器 | simple | - | 20 | 70% |
| 重绘幅度 | 1 | 0.25 - 1 | 20 | 65% |
| 宽度 | 1024 | 80 - 1080 | 20 | 42% |
| 高度 | 1024 | 80 - 1920 | 20 | 36% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 10，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，20 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 euler，20 个样本，一致性 70%
- 调度器 最常用 simple，20 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，20 个样本
- 宽度 中位数 1024，观测区间 80 - 1080，20 个样本，取值分散，一致性仅 42%
- 高度 中位数 1024，观测区间 80 - 1920，20 个样本，取值分散，一致性仅 36%
- 高发问题（31/20 个样本）：Steps较低可能导致细节不足
