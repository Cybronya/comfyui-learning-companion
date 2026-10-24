---
name: image_to_image_controlnet_upscale_lora_3
type: Image To Image
frequency: 9
level: strong
coverage: 0.803556
common_nodes: [AddLabel, Anything Everywhere3, CLIPTextEncode, ColorMatch, ControlNetApplyAdvanced, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), ImageConcatMulti, ImagePadForOutpaint, ImageUpscaleWithModel, KSampler, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleRestore, LoadImage, LoraLoader, PreviewImage, RHHiddenNodes, RH_Captioner, ResizeImageMixlab, SaveImage, SetLatentNoiseMask, ShowText|pysssss, SubtractMask, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageDetailTransfer, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物参考图换背景-100%还原动作服装_1939250816853393410.json, 图片生成/图生图/人物换背景-不改变人物着装_2057667736947482625.json, 图片生成/图生图/人物换背景-人物保持不变_2046462939066015745.json, 图片生成/图生图/人物换背景-生成式-100%不动服装_2056206238928646146.json, 图片生成/图生图/人物换背景-生成式-100%不动服装_2088507727193661442.json, 图片生成/图生图/人物换背景-生成式-100%不动服装自用_2013980585991081985.json, 图片生成/图生图/人物换背景【保证服装不变】_1988181368284823554.json, 图片生成/图生图/换背景_1951214425015562242.json, 图片生成/图生图/🦖人物换背景_1938173102591229953.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/人物参考图换背景-100%还原动作服装_1939250816853393410.json、图片生成/图生图/人物换背景-不改变人物着装_2057667736947482625.json、图片生成/图生图/人物换背景-人物保持不变_2046462939066015745.json、图片生成/图生图/人物换背景-生成式-100%不动服装_2056206238928646146.json、图片生成/图生图/人物换背景-生成式-100%不动服装_2088507727193661442.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 9 个 workflow 都包含：
- `AddLabel`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `ImagePadForOutpaint`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleRestore`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_Captioner`
- `ResizeImageMixlab`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `SubtractMask`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageDetailTransfer`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 8/9 个有
- `ImageAndMaskPreview` —— 8/9 个有
- `LayerMask: MaskPreview` —— 8/9 个有
- `NunchakuFluxDiTLoader` —— 8/9 个有
- `NunchakuFluxLoraLoader` —— 8/9 个有
- `TextInput_` —— 8/9 个有
- `easy imageScaleDownToSize` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | normal | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.5 | 9 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 9 | 100% |
| ControlNet 权重 | 0.3 | 0.3 - 0.3 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 normal，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.5，9 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.3，观测区间 0.3 - 0.3，9 个样本，取值集中（一致性 100%）
- 高发问题（18/9 个样本）：Steps较低可能导致细节不足
