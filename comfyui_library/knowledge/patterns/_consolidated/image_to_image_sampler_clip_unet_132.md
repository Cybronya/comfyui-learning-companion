---
name: image_to_image_sampler_clip_unet_132
type: Image To Image
frequency: 3
level: strong
coverage: 0.833333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), ImageConcanate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RH_ComfyFluxKontext, RH_Translator, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext +Gemini 2.5图像编辑-更新多图编辑_1967765917520322562.json, 图片生成/图生图/Flux Kontext +Gemini 2.5图像编辑_1945727122943987713.json, 图片生成/文生图/Flux Kontext单双图模式（4o进阶版）_1940231458583695361.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_132

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux Kontext +Gemini 2.5图像编辑-更新多图编辑_1967765917520322562.json、图片生成/图生图/Flux Kontext +Gemini 2.5图像编辑_1945727122943987713.json、图片生成/文生图/Flux Kontext单双图模式（4o进阶版）_1940231458583695361.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RH_ComfyFluxKontext`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 2/3 个有
- `RH_Nano_Banana_Image2Image` —— 2/3 个有
- `Note _O` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `easy textSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
