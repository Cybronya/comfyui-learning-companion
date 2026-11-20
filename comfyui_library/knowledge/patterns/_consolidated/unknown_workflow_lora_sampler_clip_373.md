---
name: unknown_workflow_lora_sampler_clip_373
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.846
common_nodes: [AddMaskForICLora, BasicGuider, BasicScheduler, CLIPTextEncode, CR Simple Image Compare, CR Text, CheckpointLoaderSimple, DownloadAndLoadFlorence2Model, Florence2Run, FluxGuidance, ImageCrop+, ImageResizeKJ, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingFlux, PreviewImage, RandomNoise, Replace Text _O, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, ShowText|pysssss, VAEDecode, VAEEncode, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/photo2illustration (flux in-context lora)_1891306129174175745.json, 平台全量/照片转插图photo2illustration (flux in-context lora)_1858909864688005122.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_373

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/photo2illustration (flux in-context lora)_1891306129174175745.json、平台全量/照片转插图photo2illustration (flux in-context lora)_1858909864688005122.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMaskForICLora`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `CR Text`
- `CheckpointLoaderSimple`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `FluxGuidance`
- `ImageCrop+`
- `ImageResizeKJ`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `Replace Text _O`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
