---
name: unknown_workflow_upscale_lora_sampler_119
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.579
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Upscale Image, FluxGuidance, GetNode, Image Comparer (rgthree), ImageResizeKJ, KSamplerSelect, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/商业人像放大器 _ 极速模式 _ 肤质加强_1919580364656803842.json, 平台全量/人像放大器 ；细节加强 ； 肤质加强；_2062116226339524610.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_119

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/商业人像放大器 _ 极速模式 _ 肤质加强_1919580364656803842.json、平台全量/人像放大器 ；细节加强 ； 肤质加强；_2062116226339524610.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Upscale Image`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `KSamplerSelect`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
