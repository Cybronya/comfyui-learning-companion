---
name: unknown_workflow_upscale_lora_sampler_5
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.778333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/【 Banan老照片修复】香蕉图像编辑-TTP高清放大_1965854119267340289.json, 图片生成/图生图/【Nano Banan单人写真定制】香蕉图像编辑-TTP高清放大_1968281148851933185.json, 图片生成/图生图/【Nano Banan手办定制】香蕉图像编辑-TTP高清放大_1968220824744374273.json, 图片生成/图生图/【老照片修复V2】全能图片pro-TTP高清放大_1993420879201763329.json, 图片生成/图生图/【表情包定制】 Banan-TTP高清放大_2040783870953529345.json, 图片生成/图生图/【表情包定制】全能图片V1+一键生成表情包+照片一键制作卡通动物表情包+生成+九宫格+表情包_2019319522431340546.json, 图片生成/图生图/【表情包定制】高清放大_2016317444448591873.json, 图片生成/图生图/全能图片V1 2 & Pro 万能图像编辑 完胜Qwen-Image TTP拆分+Seed_1994603666466349057.json, 图片生成/图生图/卡通头像  一键表情包_2067204909480632322.json, 图片生成/图生图/卡通头像一键生成表情包_2069954852985335810.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】Banan高清放大_2067054099513823233.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】Banan高清放大_2068202060545351682.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】_2069224450087804930.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】_2071766464339726338.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】_2072861657474359297.json, 图片生成/图生图/生成卡通头像一键表情包生成【表情包定制】_2076464180277899265.json, 图片生成/图生图/生成卡通头像一键表情包生成真人动漫都可用【表情包定制】_2067313367072727042.json, 图片生成/文生图/【自定义静态表情包定制】 Banan-TTP高清放大_2065150014434930689.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/【 Banan老照片修复】香蕉图像编辑-TTP高清放大_1965854119267340289.json、图片生成/图生图/【Nano Banan单人写真定制】香蕉图像编辑-TTP高清放大_1968281148851933185.json、图片生成/图生图/【Nano Banan手办定制】香蕉图像编辑-TTP高清放大_1968220824744374273.json、图片生成/图生图/【老照片修复V2】全能图片pro-TTP高清放大_1993420879201763329.json、图片生成/图生图/【表情包定制】 Banan-TTP高清放大_2040783870953529345.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 18 个 workflow 都包含：
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
- `Anything Everywhere3` —— 17/18 个有
- `ImageResize+` —— 17/18 个有
- `RH_Nano_Banana_Image2Image` —— 16/18 个有
- `CR Text` —— 15/18 个有
- `RHHiddenNodes` —— 15/18 个有
- `RH_Translator` —— 3/18 个有
- `RH_Nano_Banana2_Image2Image` —— 2/18 个有
- `AILab_MiniCPM_4_V_Advanced` —— 1/18 个有
- `CR Text Concatenate` —— 1/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有
- `ImpactSwitch` —— 1/18 个有
- `Int` —— 1/18 个有
- `TT_img_enc` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2 | 2 - 2 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | karras | - | 18 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.45 | 18 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 18/18 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 2，观测区间 2 - 2，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 karras，18 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.45，18 个样本，取值集中（一致性 89%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
- 高发问题（18/18 个样本）：发现KSampler但没有VAEDecode
