---
name: unknown_workflow_upscale_lora_sampler_3
type: Unknown Workflow
frequency: 26
level: strong
coverage: 0.774231
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/【 Banan老照片修复】香蕉图像编辑-TTP高清放大_1965854119267340289.json, 图片生成/图生图/【Nano Banan单人写真定制】香蕉图像编辑-TTP高清放大_1968281148851933185.json, 图片生成/图生图/【Nano Banan手办定制】香蕉图像编辑-TTP高清放大_1968220824744374273.json, 图片生成/图生图/【老照片修复V2】全能图片pro-TTP高清放大_1993420879201763329.json, 图片生成/图生图/【表情包定制】 Banan-TTP高清放大_2040783870953529345.json, 图片生成/图生图/【表情包定制】全能图片V1+一键生成表情包+照片一键制作卡通动物表情包+生成+九宫格+表情包_2019319522431340546.json, 图片生成/图生图/【表情包定制】高清放大_2016317444448591873.json, 图片生成/图生图/全能图片V1 2 & Pro 万能图像编辑 完胜Qwen-Image TTP拆分+Seed_1994603666466349057.json, 图片生成/图生图/卡通头像  一键表情包_2067204909480632322.json, 图片生成/图生图/卡通头像一键生成表情包_2069954852985335810.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】Banan高清放大_2067054099513823233.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】Banan高清放大_2068202060545351682.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】_2069224450087804930.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】_2071766464339726338.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】_2072861657474359297.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】_2076464180277899265.json, 图片生成/图生图/生成卡通头像一键表情包生成真人动漫都可用【表情包定制】_2067313367072727042.json, 图片生成/文生图/【自定义静态表情包定制】 Banan-TTP高清放大_2065150014434930689.json, 平台全量/【表情包+动画形象设计定制】快来定制专属你的超可爱表情包和动画形象设计_2033721391152898049.json, 平台全量/【表情包+动画形象设计定制】快来定制专属你的超可爱表情包和动画形象设计_2043928061841776641.json, 平台全量/【表情包定制】 Banan-TTP高清放大_1969566089501941761.json, 平台全量/【表情包定制】 Banan-TTP高清放大_1969570949546844162.json, 平台全量/【表情包定制】Nano Banan-TTP高清放大_1968878645043449858.json, 平台全量/【表情包定制】全能图片V1 一键生成表情包 照片一键制作卡通动物表情包 生成 九宫格 表情包_1986677981793972225.json, 平台全量/【表情包定制】真人动漫都可以生成_2065152576076738562.json, 平台全量/全能图片V1 一键生成表情包 2d转3d + TTP拆分+SeedVR2  高清放大 【表情包定制】_1993854172219064322.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/图生图/【 Banan老照片修复】香蕉图像编辑-TTP高清放大_1965854119267340289.json、图片生成/图生图/【Nano Banan单人写真定制】香蕉图像编辑-TTP高清放大_1968281148851933185.json、图片生成/图生图/【Nano Banan手办定制】香蕉图像编辑-TTP高清放大_1968220824744374273.json、图片生成/图生图/【老照片修复V2】全能图片pro-TTP高清放大_1993420879201763329.json、图片生成/图生图/【表情包定制】 Banan-TTP高清放大_2040783870953529345.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 25/26 个有
- `ImageResize+` —— 25/26 个有
- `RH_Nano_Banana_Image2Image` —— 24/26 个有
- `CR Text` —— 23/26 个有
- `RHHiddenNodes` —— 23/26 个有
- `RH_Translator` —— 3/26 个有
- `RH_Nano_Banana2_Image2Image` —— 2/26 个有
- `AILab_MiniCPM_4_V_Advanced` —— 1/26 个有
- `CR Text Concatenate` —— 1/26 个有
- `Fast Groups Bypasser (rgthree)` —— 1/26 个有
- `ImpactSwitch` —— 1/26 个有
- `Int` —— 1/26 个有
- `TT_img_enc` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2 | 2 - 2 | 26 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 26 | 100% |
| 采样算法 | euler | - | 26 | 100% |
| 调度器 | karras | - | 26 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.45 | 26 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 26/26 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 2，观测区间 2 - 2，26 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，26 个样本，一致性 100%
- 调度器 最常用 karras，26 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.45，26 个样本，取值集中（一致性 91%）
- 高发问题（26/26 个样本）：Steps较低可能导致细节不足
- 高发问题（26/26 个样本）：发现KSampler但没有VAEDecode
