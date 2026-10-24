---
name: text_to_image_controlnet_upscale_lora_10
type: Text To Image
frequency: 2
level: weak
coverage: 0.81
common_nodes: [AddLabel, Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ColorMatch, ControlNetApplyAdvanced, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageConcatMulti, ImagePadForOutpaint, ImageUpscaleWithModel, JjkText, KSampler, LayerMask: MaskPreview, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleRestore, LoadImage, LoraLoader, LoraLoaderModelOnly, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PreviewImage, RHHiddenNodes, RH_Captioner, ResizeImageMixlab, SaveImage, SetLatentNoiseMask, ShowText|pysssss, SubtractMask, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageDetailTransfer, easy imageRemBg, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/100%不动服装生成式人物换背景局部重绘图片换背景_2087353262398853122.json, 图片生成/图生图/100%不动服装｜人物生成式换背景局部重绘_2092603971650281473.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/100%不动服装生成式人物换背景局部重绘图片换背景_2087353262398853122.json、图片生成/图生图/100%不动服装｜人物生成式换背景局部重绘_2092603971650281473.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
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
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.3 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（6/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
