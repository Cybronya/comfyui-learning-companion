---
name: text_to_image_controlnet_upscale_lora_7
type: Text To Image
frequency: 3
level: strong
coverage: 0.811333
common_nodes: [AddLabel, Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ColorMatch, ControlNetApplyAdvanced, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageConcatMulti, ImagePadForOutpaint, ImageUpscaleWithModel, JjkText, KSampler, LayerMask: MaskPreview, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleRestore, LoadImage, LoraLoader, LoraLoaderModelOnly, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PreviewImage, RHHiddenNodes, RH_Captioner, ResizeImageMixlab, SaveImage, SetLatentNoiseMask, ShowText|pysssss, SubtractMask, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageDetailTransfer, easy imageRemBg, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/100%不动服装生成式人物换背景局部重绘图片换背景_2087353262398853122.json, 图片生成/图生图/100%不动服装｜人物生成式换背景局部重绘_2092603971650281473.json, 平台全量/100%不动服装｜人物生成式换背景局部重绘_2092173475774550018.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/100%不动服装生成式人物换背景局部重绘图片换背景_2087353262398853122.json、图片生成/图生图/100%不动服装｜人物生成式换背景局部重绘_2092603971650281473.json、平台全量/100%不动服装｜人物生成式换背景局部重绘_2092173475774550018.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageConcatMulti`
- `ImagePadForOutpaint`
- `ImageUpscaleWithModel`
- `JjkText`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleRestore`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_Captioner`
- `ResizeImageMixlab`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `SubtractMask`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageDetailTransfer`
- `easy imageRemBg`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.3 | 0.3 - 0.3 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足
