---
name: unknown_workflow_controlnet_lora_clip
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.813083
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptySD3LatentImage, Get Image Size, GetImageSize, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImpactMinMax, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, Qwen3_VQA, QwenImageDiffsynthControlnet, SaveImage, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch, Text Concatenate, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/(贞贞版)Z-image完美版自动提示词多条件Cn控制V1_1996548797037682690.json, 图片生成/图生图/(贞贞版)Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000525286678687745.json, 图片生成/图生图/Z-image-controlnet-自动提示词-双采样器-更好_1997872694026731522.json, 图片生成/图生图/Z-image-controlnet-自动提示词-双采样器效果更好_1997221726897520642.json, 图片生成/图生图/Z-image完美版自动提示词多条件Cn控制V1_1996605433223725058.json, 图片生成/图生图/Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000525304743460865.json, 图片生成/图生图/Z-image自动提示词+Union Controlnet 2.0控制+TTP放大_2001462714058895361.json, 图片生成/图生图/Z-image自动提示词多条件Union Controlnet 2.0控制+分块放大V1_2000560398984151041.json, 图片生成/图生图/Z-image自动提示词（洗图）Union Controlnet 2.0_2001482568493039618.json, 图片生成/图生图/Z-image自动提示词（洗图）Union+Controlnet+2.0_2001643386878717953.json, 图片生成/图生图/老高自动提示词（洗图背景）Union+Controlnet+2.0_2015688100151824386.json, 图片生成/图生图/（牛逼洗图）Z-image自动洗图-魔改T8，感谢T8开源分享_2018356196398338049.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_clip

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/(贞贞版)Z-image完美版自动提示词多条件Cn控制V1_1996548797037682690.json、图片生成/图生图/(贞贞版)Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000525286678687745.json、图片生成/图生图/Z-image-controlnet-自动提示词-双采样器-更好_1997872694026731522.json、图片生成/图生图/Z-image-controlnet-自动提示词-双采样器效果更好_1997221726897520642.json、图片生成/图生图/Z-image完美版自动提示词多条件Cn控制V1_1996605433223725058.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 12 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Get Image Size`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `Qwen3_VQA`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Canny` —— 10/12 个有
- `ImageConcatMulti` —— 10/12 个有
- `KSampler` —— 10/12 个有
- `ImageScaleToMaxDimension` —— 7/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/12 个有
- `easy int` —— 3/12 个有
- `Anything Everywhere` —— 2/12 个有
- `GetNode` —— 2/12 个有
- `KSamplerAdvanced` —— 2/12 个有
- `SetNode` —— 2/12 个有
- `easy imageConcat` —— 2/12 个有
- `ColorCorrect` —— 1/12 个有
- `ImageConcanate` —— 1/12 个有
- `Int` —— 1/12 个有
- `ShowText` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 10 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 12 | 0% |
| 采样算法 | euler | - | 12 | 67% |
| 调度器 | ddim_uniform | - | 12 | 67% |
| 重绘幅度 | 0.65 | 0.65 - 1 | 10 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，10 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，12 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，12 个样本，一致性 67%
- 调度器 最常用 ddim_uniform，12 个样本，一致性 67%
- 重绘幅度 中位数 0.65，观测区间 0.65 - 1，10 个样本，取值集中（一致性 81%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（8/12 个样本）：Steps较低可能导致细节不足
