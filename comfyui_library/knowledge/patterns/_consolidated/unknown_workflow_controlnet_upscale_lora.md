---
name: unknown_workflow_controlnet_upscale_lora
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.51925
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ColorCorrect, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, Image Comparer (rgthree), ImageScaleToTotalPixels, JoinStrings, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetUnionControlNetType, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/I2L一键风格转绘 _ 超邪修搭配，一张图直接转绘_1999746214172164098.json, 图片生成/文生图/Qwen-image2512真实感洗图+seekvr2高清放大_2006689719085699073.json, 图片生成/文生图/Qwen-image2512真实感洗图+高清放大_2006436408986181634.json, 图片生成/文生图/Qwen-image2512艺术感洗图+高清放大_2006396528398700545.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/I2L一键风格转绘 _ 超邪修搭配，一张图直接转绘_1999746214172164098.json、图片生成/文生图/Qwen-image2512真实感洗图+seekvr2高清放大_2006689719085699073.json、图片生成/文生图/Qwen-image2512真实感洗图+高清放大_2006436408986181634.json、图片生成/文生图/Qwen-image2512艺术感洗图+高清放大_2006396528398700545.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ColorCorrect`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `MemoryCleaner` —— 3/4 个有
- `ImageBatchMulti` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `ImageScaleToMegapixels` —— 1/4 个有
- `Int` —— 1/4 个有
- `RunningHub_ImageQwenI2L_Loader(Style)` —— 1/4 个有
- `RunningHub_ImageQwenI2L_LoraGenerator` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1.01 | 1 - 1.01 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 75% |
| 调度器 | beta57 | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.01，观测区间 1 - 1.01，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 75%
- 调度器 最常用 beta57，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
