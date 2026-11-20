---
name: unknown_workflow_inpaint_lora_sampler_83
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.915
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, INPAINT_MaskedBlur, INPAINT_MaskedFill, ImagePadKJ, InpaintModelConditioning, KSampler (Efficient), LayerColor: ColorAdapter, LayerMask: MaskGrow, LayerUtility: ImageBlend V2, LayerUtility: PurgeVRAM V2, LoadAndResizeImage, NunchakuFluxDiTLoader, NunchakuTextEncoderLoaderV2, PrimitiveInt, SaveImage, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-nunchaku 扩图_1933431793569964034.json, 平台全量/flux.1- fill扩图v1_1962316097447989249.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_83

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux-nunchaku 扩图_1933431793569964034.json、平台全量/flux.1- fill扩图v1_1962316097447989249.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `INPAINT_MaskedBlur`
- `INPAINT_MaskedFill`
- `ImagePadKJ`
- `InpaintModelConditioning`
- `KSampler (Efficient)`
- `LayerColor: ColorAdapter`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageBlend V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAndResizeImage`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoaderV2`
- `PrimitiveInt`
- `SaveImage`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
