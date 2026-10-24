---
name: unknown_workflow_controlnet_lora_sampler
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.517231
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ColorCorrect, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SetUnionControlNetType, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image2512+精准洗图+高清放大_2006556623728283649.json, 图片生成/图生图/Qwen-image2512-写实类洗图+高清放大_2006578345303089153.json, 图片生成/图生图/Qwen-image2512图生图+高清放大_2061008797669347329.json, 图片生成/图生图/Qwen-image2512真实感洗图+高清放大_sfw_2015408846612729858.json, 图片生成/图生图/Qwen-image2512真实感洗图+高清放大_本地解码_2010221306658164738.json, 图片生成/图生图/Qwen-image2512真实感洗图【深度_线稿控制】+seekvr2高清放大_2009918850896236546.json, 图片生成/图生图/一键任意风格迁移 _ 超邪修搭配_2046893085010960386.json, 图片生成/图生图/一键风格转绘_2002769931915653122.json, 图片生成/图生图/抄图像的风格：文生图_上传图 然后抄风格 洗图工作流_2032852655239864322.json, 图片生成/文生图/I2L一键风格转绘 _ 超邪修搭配，一张图直接转绘_1999746214172164098.json, 图片生成/文生图/Qwen-image2512真实感洗图+seekvr2高清放大_2006689719085699073.json, 图片生成/文生图/Qwen-image2512真实感洗图+高清放大_2006436408986181634.json, 图片生成/文生图/Qwen-image2512艺术感洗图+高清放大_2006396528398700545.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen-image2512+精准洗图+高清放大_2006556623728283649.json、图片生成/图生图/Qwen-image2512-写实类洗图+高清放大_2006578345303089153.json、图片生成/图生图/Qwen-image2512图生图+高清放大_2061008797669347329.json、图片生成/图生图/Qwen-image2512真实感洗图+高清放大_sfw_2015408846612729858.json、图片生成/图生图/Qwen-image2512真实感洗图+高清放大_本地解码_2010221306658164738.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 13 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ColorCorrect`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 11/13 个有
- `LayerUtility: ImageReel` —— 11/13 个有
- `LayerUtility: ImageReelComposit` —— 11/13 个有
- `Qwen3_VQA` —— 11/13 个有
- `SeedVR2LoadDiTModel` —— 11/13 个有
- `SeedVR2LoadVAEModel` —— 11/13 个有
- `SeedVR2VideoUpscaler` —— 11/13 个有
- `TextInput_` —— 11/13 个有
- `easy showAnything` —— 11/13 个有
- `Image Comparer (rgthree)` —— 10/13 个有
- `Fast Groups Bypasser (rgthree)` —— 9/13 个有
- `INTConstant` —— 9/13 个有
- `MemoryCleaner` —— 7/13 个有
- `ImageBatchMulti` —— 4/13 个有
- `ImageConcatMulti` —— 4/13 个有
- `ImageScaleBy` —— 4/13 个有
- `ImageScaleToMegapixels` —— 4/13 个有
- `Int` —— 4/13 个有
- `RunningHub_ImageQwenI2L_Loader(Style)` —— 4/13 个有
- `RunningHub_ImageQwenI2L_LoraGenerator` —— 4/13 个有
- `easy cleanGpuUsed` —— 4/13 个有
- `MultiLinePromptIndex` —— 2/13 个有
- `DuckHideNode` —— 1/13 个有
- `EmptyFlux2LatentImage` —— 1/13 个有
- `Fast Groups Muter (rgthree)` —— 1/13 个有
- `GetNode` —— 1/13 个有
- `SetNode` —— 1/13 个有
- `ToggleAnyNode` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 13 | 100% |
| 采样步数 | 8 | 4 - 8 | 13 | 85% |
| Prompt 约束强度(CFG) | 1.01 | 1 - 1.01 | 13 | 100% |
| 采样算法 | res_2s | - | 13 | 69% |
| 调度器 | beta57 | - | 13 | 69% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 8，13 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1.01，观测区间 1 - 1.01，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，13 个样本，一致性 69%
- 调度器 最常用 beta57，13 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
