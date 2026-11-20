---
name: unknown_workflow_upscale_sampler_clip_64
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.949
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, KSamplerSelect, LoadImage, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/放大不变化工作流_1959094113310289922.json, 平台全量/万能放大3K_1964920589750292481.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/放大不变化工作流_1959094113310289922.json、平台全量/万能放大3K_1964920589750292481.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Image Lucy Sharpen` —— 1/2 个有
- `ImageColorMatch+` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustom` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `UltimateSDUpscaleNoUpscale` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
