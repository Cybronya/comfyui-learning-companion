---
name: unknown_workflow_inpaint_lora_sampler_20
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.4572
common_nodes: [CFGNorm, CLIPLoader, CreateShapeMask, EmptySD3LatentImage, GetNode, GrowMaskWithBlur, ImageBlend, ImageConcanate, ImagePadForOutpaint, ImageResizeKJv2, ImageScaleToTotalPixels, InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingAuraFlow, PreviewImage, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, SaveImage, SetNode, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MICKMUMPITZ_千问分镜编辑流_1985558463273226241.json, 图片生成/图生图/Qwen2511背景一致性_2060375478309052417.json, 图片生成/图生图/qwen edit生成和修复360全景图_1985932651158806529.json, 图片生成/图生图/一图直出360全景图_1994978537155309569.json, 图片生成/文生图/251101_MICKMUMPITZ_SCENE-BUILDER_1-0_1986688032843706370.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/MICKMUMPITZ_千问分镜编辑流_1985558463273226241.json、图片生成/图生图/Qwen2511背景一致性_2060375478309052417.json、图片生成/图生图/qwen edit生成和修复360全景图_1985932651158806529.json、图片生成/图生图/一图直出360全景图_1994978537155309569.json、图片生成/文生图/251101_MICKMUMPITZ_SCENE-BUILDER_1-0_1986688032843706370.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CreateShapeMask`
- `EmptySD3LatentImage`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageBlend`
- `ImageConcanate`
- `ImagePadForOutpaint`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 4/5 个有
- `OlmDragCrop` —— 4/5 个有
- `DWPreprocessor` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `LoaderGGUF` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `GGUFLoaderKJ` —— 2/5 个有
- `JoinStringMulti` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `PanoramaViewerNode` —— 1/5 个有
- `SaveImageToLocal` —— 1/5 个有
- `Setter` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
