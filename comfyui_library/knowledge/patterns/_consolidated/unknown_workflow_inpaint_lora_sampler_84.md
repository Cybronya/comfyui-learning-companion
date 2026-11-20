---
name: unknown_workflow_inpaint_lora_sampler_84
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.913
common_nodes: [CLIPTextEncodeFlux, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, FluxSampler, InpaintModelConditioning, LayerUtility: CropByMask V2, LayerUtility: ICMask, LayerUtility: ICMaskCropBack, LayerUtility: RestoreCropBox, LoadImage, MaskPreview+, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoaderV2, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-nunchaku-万物迁移_1933431858459750402.json, 平台全量/flux物品迁移_1949696483886026754.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux-nunchaku-万物迁移_1933431858459750402.json、平台全量/flux物品迁移_1949696483886026754.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `FluxSampler`
- `InpaintModelConditioning`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ICMask`
- `LayerUtility: ICMaskCropBack`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskPreview+`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoaderV2`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
