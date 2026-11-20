---
name: unknown_workflow_sampler_clip_checkpoint_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.929
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DualCLIPLoader, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LucidFlux_SM_Cond, LucidFlux_SM_Encode, LucidFlux_SM_KSampler, LucidFlux_SM_Model, SaveImage, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/LucidFlux图像修复V2_1976309147899699201.json, 图片生成/图生图/高清修复LucidFlux图像修复V2_1981313653012070402.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/LucidFlux图像修复V2_1976309147899699201.json、图片生成/图生图/高清修复LucidFlux图像修复V2_1981313653012070402.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LucidFlux_SM_Cond`
- `LucidFlux_SM_Encode`
- `LucidFlux_SM_KSampler`
- `LucidFlux_SM_Model`
- `SaveImage`
- `VAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
