---
name: image_to_image_lora_sampler_clip_66
type: Image To Image
frequency: 4
level: strong
coverage: 0.80125
common_nodes: [CLIPTextEncode, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/21.tonnie-kontext换脸（手动）_1997904264250949633.json, 图片生成/图生图/24.tonnie-kontext万物迁移_1997984525126918145.json, 图片生成/图生图/Kontext 一键溶图、换头、换背景_1966380464816762882.json, 图片生成/图生图/Kontext+lora新版产品溶图_1961704631699181570.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_66

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/21.tonnie-kontext换脸（手动）_1997904264250949633.json、图片生成/图生图/24.tonnie-kontext万物迁移_1997984525126918145.json、图片生成/图生图/Kontext 一键溶图、换头、换背景_1966380464816762882.json、图片生成/图生图/Kontext+lora新版产品溶图_1961704631699181570.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `ModelSamplingFlux` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `InspyrenetRembg` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `CropFace` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `LayerUtility: CropByMask V2` —— 1/4 个有
- `LayerUtility: ImageAutoCrop V2` —— 1/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/4 个有
- `easy imageDetailTransfer` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 10 - 20 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
