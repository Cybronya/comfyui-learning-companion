---
name: unknown_workflow_lora_sampler_clip_67
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.717333
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, Lora Loader Stack (rgthree), PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: [Note Plus (mtb), easy cleanGpuUsed, easy clearCacheAll, Lora Loader Stack (rgthree), CR Text Concatenate]
members: [图片生成/文生图/1906942276495450113.json, 图片生成/文生图/1925114613338152962.json, 图片生成/文生图/Flux最强换脸_1894257044323500034.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_67

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1906942276495450113.json、图片生成/文生图/1925114613338152962.json、图片生成/文生图/Flux最强换脸_1894257044323500034.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `DualCLIPLoaderGGUF` —— 1/3 个有
- `Florence2ModelLoader` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Note Plus (mtb)、easy cleanGpuUsed、easy clearCacheAll、Lora Loader Stack (rgthree)、CR Text Concatenate
