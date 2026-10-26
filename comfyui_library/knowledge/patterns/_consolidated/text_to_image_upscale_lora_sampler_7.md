---
name: text_to_image_upscale_lora_sampler_7
type: Text To Image
frequency: 15
level: weak
coverage: 0.886533
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, ImageScaleToTotalPixels, JjkText, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculator, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, QZ_ResolutionPreset, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMathDual+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy loraStack, easy loraStackApply, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/图片反推提示词Krea2超写实高清大图｜人物特效反推一键出图_2114260985493151746.json, 图片生成/反推提示词/图片反推提示词加Krea2超写实生成，高清大图还原度拉满_2114492777340952578.json, 图片生成/图生图/4K高清婚纱自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2113320436816769026.json, 图片生成/图生图/Krea2 超写实 4K 文生图｜超写实去AI感画面更真实_2096870089223131138.json, 图片生成/图生图/Krea2超写实4K图生图｜美少女写实出图质感在线_2108060491858931713.json, 图片生成/图生图/Krea2超写实4K文生图｜去AI感真实感人像场景生成_2096677854607142913.json, 图片生成/文生图/4K超写实去ai感｜Krea2文生图高清一键生成_2094764662138163201.json, 图片生成/文生图/4K超写实文生图｜Krea2人像写真角色设计超清直出_2089043670136868866.json, 图片生成/文生图/4K超写实文生图｜Krea2写实大片生成_2092583582224175105.json, 图片生成/文生图/Krea 2超写实4K文生图处理生成工作流_2101031767800115202.json, 图片生成/文生图/Krea2 4K超清写实文生图｜美少女直出高质量_2089433996257222657.json, 图片生成/文生图/Krea2 超写实4K文生图｜去AI感真实到犯规 直出大片_2097582803880865794.json, 图片生成/文生图/Krea2 超写实4K文生图｜美少女写实大片直出_2112441686365396994.json, 图片生成/文生图/Krea2写实美少女文生图，4K超高清流量出图_2110888355004239873.json, 图片生成/文生图/Krea2文生图_超写实4K商业级工作流_2082042807304409089.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/反推提示词/图片反推提示词Krea2超写实高清大图｜人物特效反推一键出图_2114260985493151746.json、图片生成/反推提示词/图片反推提示词加Krea2超写实生成，高清大图还原度拉满_2114492777340952578.json、图片生成/图生图/4K高清婚纱自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2113320436816769026.json、图片生成/图生图/Krea2 超写实 4K 文生图｜超写实去AI感画面更真实_2096870089223131138.json、图片生成/图生图/Krea2超写实4K图生图｜美少女写实出图质感在线_2108060491858931713.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculator`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `QZ_ResolutionPreset`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMathDual+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy loraStack`
- `easy loraStackApply`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 14/15 个有
- `LoraLoaderModelOnly` —— 14/15 个有
- `solarL_SaveImagesToZip` —— 14/15 个有
- `孤海注释` —— 14/15 个有
- `Fast Groups Bypasser (rgthree)` —— 9/15 个有
- `LoadImage` —— 3/15 个有
- `ShowText|pysssss` —— 2/15 个有
- `easy saveText` —— 2/15 个有
- `llama_cpp_instruct_adv` —— 2/15 个有
- `llama_cpp_model_loader` —— 2/15 个有
- `llama_cpp_parameters` —— 2/15 个有
- `GetImageSize+` —— 1/15 个有
- `ImageCASharpening+` —— 1/15 个有
- `ImageResize+` —— 1/15 个有
- `ImageScaleBy` —— 1/15 个有
- `RH_RhartImageG2ImageToImage` —— 1/15 个有
- `TTP_Image_Assy` —— 1/15 个有
- `TTP_Image_Tile_Batch` —— 1/15 个有
- `TTP_Tile_image_size` —— 1/15 个有
- `TextGenerateLTX2Prompt` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1152 | 15 | 0% |
| 高度 | 80 | 80 - 1536 | 15 | 0% |
| 采样步数 | 4 | 2 - 4 | 15 | 87% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 15 | 80% |
| 采样算法 | er_sde | - | 15 | 93% |
| 调度器 | beta | - | 15 | 93% |
| 重绘幅度 | 1 | 0.1 - 1 | 15 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1152，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，15 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 2 - 4，15 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，15 个样本
- 采样算法 最常用 er_sde，15 个样本，一致性 93%
- 调度器 最常用 beta，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，15 个样本
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
