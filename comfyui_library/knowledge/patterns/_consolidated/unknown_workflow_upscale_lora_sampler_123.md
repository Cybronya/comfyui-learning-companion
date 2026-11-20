---
name: unknown_workflow_upscale_lora_sampler_123
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.815
common_nodes: [AILab_QwenVL, BasicScheduler, CFGNorm, CLIPLoader, CR Text, CheckpointLoaderSimple, DetailDaemonSamplerNode, ImageScaleToTotalPixelsX, JDCN_StringToList, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ProcessString, SamplerCustom, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse, easy int, easy promptReplace]
problems: []
missing: []
members: [图片生成/图生图/超写实 8K 高清摄影 Qwe edit-2511+firered edit-1.1 服装摄影 多角_2043143536920502274.json, 平台全量/qwen-image-edit-2511+firered-image-edit-1.1-服装摄影师-多角度多姿态一致性模特图像生成_2015300465973534721.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_123

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/超写实 8K 高清摄影 Qwe edit-2511+firered edit-1.1 服装摄影 多角_2043143536920502274.json、平台全量/qwen-image-edit-2511+firered-image-edit-1.1-服装摄影师-多角度多姿态一致性模特图像生成_2015300465973534721.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicScheduler`
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `CheckpointLoaderSimple`
- `DetailDaemonSamplerNode`
- `ImageScaleToTotalPixelsX`
- `JDCN_StringToList`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ProcessString`
- `SamplerCustom`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy int`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
