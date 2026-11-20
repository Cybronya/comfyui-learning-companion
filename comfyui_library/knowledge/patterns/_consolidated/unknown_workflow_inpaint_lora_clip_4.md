---
name: unknown_workflow_inpaint_lora_clip_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, CR Overlay Transparent Image, ConditioningZeroOut, ConstrainImage|pysssss, DetailerForEach, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMask, InpaintCrop, InpaintStitch, InvertMask (segment anything), LayerMask: PersonMaskUltra V2, LayerMask: SegformerB2ClothesUltra, LayerUtility: ColorImage, LayerUtility: PurgeVRAM V2, LoadImage, MaskToSEGS, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PatchModelAddDownscale, SaveImage, SubtractMask, VAELoader, easy imageScaleDownToSize]
problems: []
missing: []
members: [平台全量/图片换头图片其他部分不变只改变头工作流_1977958342826020866.json, 平台全量/换头工作流_1923282620015439874.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_clip_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/图片换头图片其他部分不变只改变头工作流_1977958342826020866.json、平台全量/换头工作流_1923282620015439874.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Overlay Transparent Image`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DetailerForEach`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMask`
- `InpaintCrop`
- `InpaintStitch`
- `InvertMask (segment anything)`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ColorImage`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskToSEGS`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `PatchModelAddDownscale`
- `SaveImage`
- `SubtractMask`
- `VAELoader`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
