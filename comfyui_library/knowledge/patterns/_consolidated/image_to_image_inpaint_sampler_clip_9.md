---
name: image_to_image_inpaint_sampler_clip_9
type: Image To Image
frequency: 2
level: weak
coverage: 0.646
common_nodes: [AIO_Preprocessor, CLIPTextEncode, ConditioningZeroOut, DeepTranslatorTextNode, DifferentialDiffusion, DualCLIPLoader, Flex2Conditioner, FluxGuidance, GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageScaleToMegapixels, InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flex2和fill对比工作流_1916135838919626754.json, 图片生成/图生图/对比工作流_1934871181893771265.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flex2和fill对比工作流_1916135838919626754.json、图片生成/图生图/对比工作流_1934871181893771265.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `Flex2Conditioner`
- `FluxGuidance`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageScaleToMegapixels`
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

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | deis | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
