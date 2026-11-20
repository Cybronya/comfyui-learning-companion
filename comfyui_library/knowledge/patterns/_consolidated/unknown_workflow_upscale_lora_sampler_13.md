---
name: unknown_workflow_upscale_lora_sampler_13
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.8224
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxResolutionNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, JjkText, KSamplerSelect, LoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextCombinerTwo, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/【独一无二】【图生图】【专属定制】_1901982736465158145.json, 图片生成/文生图/3D蛇年定制头像_1882053493610700801.json, 平台全量/【基础流】风格迁移-游戏-2D角色文生图_1866475154942357506.json, 平台全量/新年3D人物_1881629292378615810.json, 平台全量/时尚杂志封面替换-Flux Redux+Pulid_1866713681701851137.json, 平台全量/服装创意手稿图_1899656768463749121.json, 平台全量/游戏-卡通场景建筑出同款_1866313192992305153.json, 平台全量/游戏-古风场景建筑出同款_1867088136240332801.json, 平台全量/游戏二次元角色出同款_1866489263293362178.json, 平台全量/游戏卡通角色出同款_1866448664909795329.json, 平台全量/游戏卡通角色出同款_1866451113045028865.json, 平台全量/游戏机甲角色出同款_1866476457265360897.json, 平台全量/蛇来运转吉祥物_1880142084052082689.json, 平台全量/财神的日常生活_1881245160632721410.json, 平台全量/赛博朋克风格头像切换-Flux Redux+Pulid_1866728529600606209.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/【独一无二】【图生图】【专属定制】_1901982736465158145.json、图片生成/文生图/3D蛇年定制头像_1882053493610700801.json、平台全量/【基础流】风格迁移-游戏-2D角色文生图_1866475154942357506.json、平台全量/新年3D人物_1881629292378615810.json、平台全量/时尚杂志封面替换-Flux Redux+Pulid_1866713681701851137.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxResolutionNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `JjkText`
- `KSamplerSelect`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextCombinerTwo`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 14/15 个有
- `Label (rgthree)` —— 13/15 个有
- `Anything Everywhere` —— 10/15 个有
- `CLIPVisionEncode` —— 10/15 个有
- `CLIPVisionLoader` —— 10/15 个有
- `LoadImage` —— 10/15 个有
- `RH_Captioner` —— 10/15 个有
- `StyleModelApplyAdvanced` —— 10/15 个有
- `StyleModelLoader` —— 10/15 个有
- `ImageResizeKJ` —— 8/15 个有
- `RH_Prompter` —— 4/15 个有
- `ApplyPulidFlux` —— 3/15 个有
- `PulidFluxEvaClipLoader` —— 3/15 个有
- `PulidFluxInsightFaceLoader` —— 3/15 个有
- `PulidFluxModelLoader` —— 3/15 个有
- `AegisFlow/aflogo` —— 1/15 个有
- `CR Image Input Switch (4 way)` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.4 - 1 | 15 | 84% |
| LoRA 文本强度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 15 | 100% |
| 高度 | 1280 | 1280 - 1280 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.4 - 1，15 个样本，取值集中（一致性 84%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，15 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，15 个样本，取值集中（一致性 100%）
