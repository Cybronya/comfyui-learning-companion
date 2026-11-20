---
name: unknown_workflow_sampler_clip_unet_552
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8305
common_nodes: [Anything Everywhere3, ApplyPulidFlux, ApplyTeaCachePatch, ApplyTeaCachePatchAdvanced, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxForwardOverrider, FluxGuidance, ImageConcanate, KSamplerSelect, LmcqDeepGen, LmcqDeepLoader, LoadImage, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/人像写真PRO2.0_1892451990482685954.json, 平台全量/人像写真_1892192593197883393.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_552

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/人像写真PRO2.0_1892451990482685954.json、平台全量/人像写真_1892192593197883393.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `ApplyPulidFlux`
- `ApplyTeaCachePatch`
- `ApplyTeaCachePatchAdvanced`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxForwardOverrider`
- `FluxGuidance`
- `ImageConcanate`
- `KSamplerSelect`
- `LmcqDeepGen`
- `LmcqDeepLoader`
- `LoadImage`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
