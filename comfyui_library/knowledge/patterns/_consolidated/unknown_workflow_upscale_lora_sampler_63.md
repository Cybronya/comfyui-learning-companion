---
name: unknown_workflow_upscale_lora_sampler_63
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.766667
common_nodes: [CLIPLoader, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["图片生成/图生图/flux2-klein9b超强一致性换装,高清直出_2020127287064141825.json", 图片生成/图生图/【御川】最新版！人像放大增加皮肤细节_2087472112440274946.json, 图片生成/图生图/风景场景+高清修复_2070018330341240834.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux2-klein9b超强一致性换装,高清直出_2020127287064141825.json、图片生成/图生图/【御川】最新版！人像放大增加皮肤细节_2087472112440274946.json、图片生成/图生图/风景场景+高清修复_2070018330341240834.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 2/3 个有
- `Get Image Size` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `easy int` —— 2/3 个有
- `图像缩放V2_孤海` —— 2/3 个有
- `数学运算_孤海` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `ColorCorrect` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `CropWithPadInfo_EditUtils` —— 1/3 个有
- `Flux2KleinOutputExtractor_EditUtils` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `LG_Color_Match_V2` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Number Multiple Of` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy boolean` —— 1/3 个有
- `easy ifElse` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有
- `easy imageScaleDownBy` —— 1/3 个有
- `easy imageScaleToNormPixels` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
