---
name: image_to_image_inpaint_lora_sampler_9
type: Image To Image
frequency: 3
level: strong
coverage: 0.913333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DeepTranslatorTextNode, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, InpaintCrop, InpaintStitch, KSampler, LayerUtility: CropByMask V3, LoadImage, LoraLoaderModelOnly, MaskPreview+, PreviewImage, RBGImageStitchPlus, ReferenceLatent, RepeatLatentBatch, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy imageRemBg, easy imageScaleDownToSize]
problems: []
missing: []
members: [图片生成/图生图/Kontext万物迁移_1948656943796760577.json, 图片生成/图生图/Kontext万物迁移终极版_1947905426147946497.json, 图片生成/图生图/Kontext万物迁移｜完美版_1950499032189816834.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Kontext万物迁移_1948656943796760577.json、图片生成/图生图/Kontext万物迁移终极版_1947905426147946497.json、图片生成/图生图/Kontext万物迁移｜完美版_1950499032189816834.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `InpaintCrop`
- `InpaintStitch`
- `KSampler`
- `LayerUtility: CropByMask V3`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PreviewImage`
- `RBGImageStitchPlus`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageRemBg`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 2/3 个有
- `GODMT_AnyCast` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `Image Blank` —— 1/3 个有
- `IsMaskEmpty` —— 1/3 个有
- `LayerUtility: ImageBlend` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
