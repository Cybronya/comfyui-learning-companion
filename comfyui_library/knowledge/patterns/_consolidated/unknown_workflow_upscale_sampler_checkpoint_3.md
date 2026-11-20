---
name: unknown_workflow_upscale_sampler_checkpoint_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.831
common_nodes: [BasicScheduler, CFGNorm, CLIPLoader, CheckpointLoaderSimple, DetailDaemonSamplerNode, Fast Groups Bypasser (rgthree), FluxKontextImageScale, ImageScaleToTotalPixelsX, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, PreviewBridge, SamplerCustom, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy positive, easy promptReplace, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/qwen-image-edit-2511-万物提取-产品白底图-服装液化-产品精修_1994729347460308993.json, 平台全量/服饰提取 变白底图 产品白底图 qwen-image-edit-2511 万物提取--服装液化-产品_2043142298350915585.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/qwen-image-edit-2511-万物提取-产品白底图-服装液化-产品精修_1994729347460308993.json、平台全量/服饰提取 变白底图 产品白底图 qwen-image-edit-2511 万物提取--服装液化-产品_2043142298350915585.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGNorm`
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `DetailDaemonSamplerNode`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextImageScale`
- `ImageScaleToTotalPixelsX`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewBridge`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`
- `easy promptReplace`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
