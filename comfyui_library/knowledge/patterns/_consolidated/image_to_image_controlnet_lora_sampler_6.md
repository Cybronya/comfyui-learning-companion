---
name: image_to_image_controlnet_lora_sampler_6
type: Image To Image
frequency: 3
level: strong
coverage: 0.814667
common_nodes: [AnyLineArtPreprocessor_aux, ApplyFBCacheOnModel, CLIPTextEncode, Canny, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, DeepTranslatorTextNode, DepthAnythingV2Preprocessor, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoader, LoraLoaderModelOnly, PreviewImage, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything, workflow>放大, workflow>获取latent]
problems: []
missing: []
members: [图片生成/图生图/FLUX （controlnet Union pro 2.0深度_线稿_姿势控制可选）洗图_1956969433690464258.json, 图片生成/图生图/一键转磨砂玻璃质感_1955263930451070977.json, 图片生成/文生图/FLUX 控制（controlnet Union pro 2.0）-洗图_1948377195357044738.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX （controlnet Union pro 2.0深度_线稿_姿势控制可选）洗图_1956969433690464258.json、图片生成/图生图/一键转磨砂玻璃质感_1955263930451070977.json、图片生成/文生图/FLUX 控制（controlnet Union pro 2.0）-洗图_1948377195357044738.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `AnyLineArtPreprocessor_aux`
- `ApplyFBCacheOnModel`
- `CLIPTextEncode`
- `Canny`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `DeepTranslatorTextNode`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`
- `workflow>放大`
- `workflow>获取latent`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.7 | 0.7 - 0.8 | 3 | 94% |
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.8，3 个样本，取值集中（一致性 94%）
- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
