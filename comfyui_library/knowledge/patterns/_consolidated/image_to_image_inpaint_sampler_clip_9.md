---
name: image_to_image_inpaint_sampler_clip_9
type: Image To Image
frequency: 3
level: moderate
coverage: 0.663333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flex2和fill对比工作流_1916135838919626754.json, 图片生成/图生图/对比工作流_1934871181893771265.json, 平台全量/FluxFill局部重绘、扩图与消除_1974132351385120769.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flex2和fill对比工作流_1916135838919626754.json、图片生成/图生图/对比工作流_1934871181893771265.json、平台全量/FluxFill局部重绘、扩图与消除_1974132351385120769.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `DeepTranslatorTextNode` —— 2/3 个有
- `Flex2Conditioner` —— 2/3 个有
- `ImageScaleToMegapixels` —— 2/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | deis | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 0.2 - 1 | 3 | 49% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，3 个样本，取值分散，一致性仅 49%
