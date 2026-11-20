---
name: image_to_image_inpaint_lora_sampler_11
type: Image To Image
frequency: 3
level: strong
coverage: 0.936667
common_nodes: [CLIPLoader, CLIPTextEncode, DownloadAndLoadFlorence2Model, Florence2Run, GrowMaskWithBlur, Image Comparer (rgthree), ImageScaleToTotalPixels, InpaintModelConditioning, KSampler, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【CQ808】修手-人像局部修复(wan2.2流程）_2020703748913369089.json, 图片生成/图生图/修手-人像局部修复(wan2.2流程）_1955634273345683458.json, 平台全量/超强局部修复 哪里有问题点哪里_1956672500363091970.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【CQ808】修手-人像局部修复(wan2.2流程）_2020703748913369089.json、图片生成/图生图/修手-人像局部修复(wan2.2流程）_1955634273345683458.json、平台全量/超强局部修复 哪里有问题点哪里_1956672500363091970.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStarAndInit` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `Note _O` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 3 | 100% |
| LoRA 模型强度 | 0.4 | - | 1 | 100% |
| LoRA 文本强度 | 0.4 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
