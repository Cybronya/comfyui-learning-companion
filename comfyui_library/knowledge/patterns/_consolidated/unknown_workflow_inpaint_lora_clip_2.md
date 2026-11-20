---
name: unknown_workflow_inpaint_lora_clip_2
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.819
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), ImpactInt, InpaintModelConditioning, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/QT101-万物移除（FLUX）万物擦除。轻松一键搞定_1933356799368015873.json, 平台全量/【无偏移】Flux.1 Fill OneReward 万物移除工作流_1998758440153534466.json, 平台全量/【精准修改】Flux.1 Fill OneReward 局部重绘_1998926717592985601.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_clip_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/QT101-万物移除（FLUX）万物擦除。轻松一键搞定_1933356799368015873.json、平台全量/【无偏移】Flux.1 Fill OneReward 万物移除工作流_1998758440153534466.json、平台全量/【精准修改】Flux.1 Fill OneReward 局部重绘_1998926717592985601.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `InpaintModelConditioning`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `KSamplerAdvanced` —— 2/3 个有
- `LayerMask: MaskGrow` —— 2/3 个有
- `LayerMask: MaskPreview` —— 2/3 个有
- `ToBinaryMask` —— 2/3 个有
- `孤海图像缩放按像素` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `InpaintCrop` —— 1/3 个有
- `InpaintStitch` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 3 | 42% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | simple | - | 3 | 33% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，3 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 simple，3 个样本，一致性 33%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
