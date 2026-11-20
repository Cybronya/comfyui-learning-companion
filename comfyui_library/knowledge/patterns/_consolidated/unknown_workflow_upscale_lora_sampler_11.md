---
name: unknown_workflow_upscale_lora_sampler_11
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.7508
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Concatenate, ComfySwitchNode, ConditioningRebalanceKrea2, ConditioningZeroOut, DepthAnythingV2Preprocessor, EmptyLatentImage, GetImageSize, GetNode, Image Comparer (rgthree), ImageConcatMulti, ImageResize+, ImageScaleBy, Int, KSamplerAdvanced, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveBoolean, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextGenerate, UNETLoader, VAEDecode, VAELoader, WD14Tagger|pysssss, easy cleanGpuUsed, easy imageSize, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Krea2_强化细节Depth_ControlNet前后控制双采样洗图_2076496008426639362.json, 图片生成/图生图/Krea2_强化细节Depth_ControlNet前后控制双采样洗图_2076504050669019137.json, 图片生成/图生图/Krea2_强化细节Depth_ControlNet前后控制双采样洗图_2080941364216422401.json, 图片生成/图生图/Krea2强化细节 Depth ControlNet前后控制双采样洗图_2081537496051183618.json, 图片生成/图生图/Krea2强化细节 Depth ControlNet前后控制双采样洗图_2087079253094518785.json, 图片生成/图生图/Krea2强化细节 Depth ControlNet前后控制双采样洗图_2087089820379213826.json, 图片生成/图生图/Krea2强化细节_Depth_ControlNet前后控制双采样洗图_2087390769110937602.json, 图片生成/图生图/Krea2强化细节_Depth_ControlNet前后控制双采样洗图_2092436988996710401.json, 图片生成/图生图/Krea2强化细节_Depth_ControlNet前后控制双采样洗图_2092614218330759169.json, 图片生成/图生图/强化细节Krea2 Depth ControlNet前后控制双采样洗图_2075910250133278721.json, 图片生成/图生图/强化细节Krea2 Depth ControlNet前后控制双采样洗图_2076505395677450242.json, 图片生成/图生图/强化细节Krea2_Depth_ControlNet前后控制双采样洗图_2095775196874633218.json, 图片生成/图生图/强化细节Krea2_Depth_ControlNet前后控制双采样洗图_2096068961183027201.json, 图片生成/图生图/美图生成 强化细节Krea2+Depth+ControlNet前后控制双采样洗图_2077206466569789441.json, 数字人/数字人/动作迁移 洗图Specifying Model Poses and Motion Transfer_2096776977326891009.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Krea2_强化细节Depth_ControlNet前后控制双采样洗图_2076496008426639362.json、图片生成/图生图/Krea2_强化细节Depth_ControlNet前后控制双采样洗图_2076504050669019137.json、图片生成/图生图/Krea2_强化细节Depth_ControlNet前后控制双采样洗图_2080941364216422401.json、图片生成/图生图/Krea2强化细节 Depth ControlNet前后控制双采样洗图_2081537496051183618.json、图片生成/图生图/Krea2强化细节 Depth ControlNet前后控制双采样洗图_2087079253094518785.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ComfySwitchNode`
- `ConditioningRebalanceKrea2`
- `ConditioningZeroOut`
- `DepthAnythingV2Preprocessor`
- `EmptyLatentImage`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `ImageResize+`
- `ImageScaleBy`
- `Int`
- `KSamplerAdvanced`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/15 个有
- `孤海注释` —— 3/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 15 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 15 | 100% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | euler | - | 15 | 100% |
| 重绘幅度 | sgm_uniform | - | 15 | 100% |
| 宽度 | 512 | 512 - 512 | 15 | 100% |
| 高度 | 512 | 512 - 512 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，15 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，15 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，15 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，15 个样本，一致性 100%
- 宽度 中位数 512，观测区间 512 - 512，15 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，15 个样本，取值集中（一致性 100%）
