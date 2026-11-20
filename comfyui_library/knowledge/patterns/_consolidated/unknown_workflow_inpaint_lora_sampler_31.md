---
name: unknown_workflow_inpaint_lora_sampler_31
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6912
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DeepTranslatorTextNode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetImageSize+, ImageConcanate, ImageToMask, InpaintModelConditioning, Joy_caption, Joy_caption_load, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, MaskToImage, ModelSamplingFlux, PreviewImage, ReduxAdvanced, SaveImage, SolidMask, StringFunction|pysssss, StyleModelLoader, Text Concatenate (JPS), UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/万物迁移至臻版（百分99.9%精准还原产品）_1896100682346921986.json, 平台全量/F.1 首饰项链万物迁移（小物件，保留原尺寸大小）_1913216109074444290.json, 平台全量/Nunchaku+redux+ace极速万物迁移_1910648600571932674.json, 平台全量/万物迁移_1908485890501713921.json, 平台全量/顶级精细万物迁移（一比一还原）_1916351969538281473.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/万物迁移至臻版（百分99.9%精准还原产品）_1896100682346921986.json、平台全量/F.1 首饰项链万物迁移（小物件，保留原尺寸大小）_1913216109074444290.json、平台全量/Nunchaku+redux+ace极速万物迁移_1910648600571932674.json、平台全量/万物迁移_1908485890501713921.json、平台全量/顶级精细万物迁移（一比一还原）_1916351969538281473.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `ImageConcanate`
- `ImageToMask`
- `InpaintModelConditioning`
- `Joy_caption`
- `Joy_caption_load`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `MaskToImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `SolidMask`
- `StringFunction|pysssss`
- `StyleModelLoader`
- `Text Concatenate (JPS)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `Image Crop Location` —— 4/5 个有
- `LayerUtility: GetImageSize` —— 4/5 个有
- `LayerUtility: ImageMaskScaleAs` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `GrowMaskWithBlur` —— 1/5 个有
- `InpaintCrop` —— 1/5 个有
- `InpaintStitch` —— 1/5 个有
- `LayerMask: MaskPreview` —— 1/5 个有
- `NunchakuFluxDiTLoader` —— 1/5 个有
- `NunchakuTextEncoderLoader` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有
- `easy imageInsetCrop` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 28 - 30 | 5 | 97% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 28 - 30，5 个样本，取值集中（一致性 97%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
