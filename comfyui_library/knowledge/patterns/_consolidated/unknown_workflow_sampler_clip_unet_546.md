---
name: unknown_workflow_sampler_clip_unet_546
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, Florence2ModelLoader, Florence2Run, ImageResize+, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/FLUX快速图生图反推指定人脸写真_1894257013080371201.json, 平台全量/【星汇工作流】电商爆款复制器_1909910870724673538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_546

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/FLUX快速图生图反推指定人脸写真_1894257013080371201.json、平台全量/【星汇工作流】电商爆款复制器_1909910870724673538.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `ImageResize+`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidFlux` —— 1/2 个有
- `ArgosTranslateTextNode` —— 1/2 个有
- `CR Latent Batch Size` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PulidFluxEvaClipLoader` —— 1/2 个有
- `PulidFluxInsightFaceLoader` —— 1/2 个有
- `PulidFluxModelLoader` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
