---
name: text_to_image_controlnet_inpaint_upscale_2
type: Text To Image
frequency: 3
level: strong
coverage: 0.863
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetInpaintingAliMamaApply, ControlNetLoader, EmptyLatentImage, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2512最新四合一_2008846137444278274.json, 图片生成/文生图/Qwen-Image2512文生图+图生图+局部重绘_2007108957206220802.json, 图片生成/文生图/【推荐】Qwen-Image2512文生图+图生图+局部重绘_2009842414927749121.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_upscale_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen image 2512最新四合一_2008846137444278274.json、图片生成/文生图/Qwen-Image2512文生图+图生图+局部重绘_2007108957206220802.json、图片生成/文生图/【推荐】Qwen-Image2512文生图+图生图+局部重绘_2009842414927749121.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `LayerMask: MaskGrow` —— 2/3 个有
- `Mask Fill Holes` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `easy getNode` —— 2/3 个有
- `easy setNode` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `MaskBlur+` —— 1/3 个有
- `MaskFillHoles` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1664 | 512 - 1664 | 3 | 58% |
| 高度 | 928 | 512 - 928 | 3 | 75% |
| 采样步数 | 6 | 4 - 6 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1664，观测区间 512 - 1664，3 个样本
- 高度 中位数 928，观测区间 512 - 928，3 个样本
- 采样步数 中位数 6，观测区间 4 - 6，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足
