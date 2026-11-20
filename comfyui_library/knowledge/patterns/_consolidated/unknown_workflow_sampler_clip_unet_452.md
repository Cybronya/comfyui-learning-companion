---
name: unknown_workflow_sampler_clip_unet_452
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.842
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: ["图片生成/图生图/老版三件套Flux,Redux,Clipvision双图融合加速可调权重工作流_1912460148080635906.json", 图片生成/文生图/Redux角色一致性_1901277660763275265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_452

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/老版三件套Flux,Redux,Clipvision双图融合加速可调权重工作流_1912460148080635906.json、图片生成/文生图/Redux角色一致性_1901277660763275265.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `StyleModelAdvancedApply` —— 1/2 个有
- `Switch any [Crystools]` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
