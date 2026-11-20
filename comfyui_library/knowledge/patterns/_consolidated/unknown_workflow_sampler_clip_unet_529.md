---
name: unknown_workflow_sampler_clip_unet_529
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9615
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【一键换脸】FLUX_PulID2 多人ID组合_1954237975934726146.json, 平台全量/CG迷-FLUX PuLID换脸工作流_1927057336362291201.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_529

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【一键换脸】FLUX_PulID2 多人ID组合_1954237975934726146.json、平台全量/CG迷-FLUX PuLID换脸工作流_1927057336362291201.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyTeaCachePatch` —— 1/2 个有
- `FluxForwardOverrider` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `MaskComposite` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
