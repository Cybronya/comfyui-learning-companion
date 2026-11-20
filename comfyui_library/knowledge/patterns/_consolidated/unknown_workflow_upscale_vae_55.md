---
name: unknown_workflow_upscale_vae_55
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.531
common_nodes: [Fast Groups Muter (rgthree), Image Comparer (rgthree), ImageBlend, ImageUpscaleWithModel, ImpactMakeAnyList, LoadImage, PreviewImage, PrimitiveInt, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UpscaleModelLoader, easy imageColorMatch]
problems: []
missing: []
members: [图片生成/图生图/模糊变清晰，细节增加，seedvr2_1995106312390422530.json, 图片生成/图生图/超强图片变清晰，超清，高清_1990451039277125633.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_55

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/模糊变清晰，细节增加，seedvr2_1995106312390422530.json、图片生成/图生图/超强图片变清晰，超清，高清_1990451039277125633.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `ImageBlend`
- `ImageUpscaleWithModel`
- `ImpactMakeAnyList`
- `LoadImage`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UpscaleModelLoader`
- `easy imageColorMatch`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
