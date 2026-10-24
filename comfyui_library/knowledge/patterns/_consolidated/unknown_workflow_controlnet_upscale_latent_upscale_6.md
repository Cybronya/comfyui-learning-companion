---
name: unknown_workflow_controlnet_upscale_latent_upscale_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.77
common_nodes: [ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CR Text Input Switch (4 way), ControlNetLoader, DualCLIPLoader, EmptyImage, EmptyLatentImage, Fast Groups Muter (rgthree), FluxGuidance, GetNode, ImageScale, ImageScaleToTotalPixels, ImageUpscaleWithModel, Int, InversionDemoLazyIndexSwitch, JjkText, JoinStrings, KSamplerSelect, LatentUpscaleBy, LoadImage, LoraLoader, ModelSamplingFlux, PreviewImage, RandomNoise, SDXLEmptyLatentSizePicker+, SamplerCustomAdvanced, SaveImage, SetNode, SetUnionControlNetType, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy showAnything, workflow>gguf-sample, workflow>save]
problems: []
missing: []
members: [图片生成/文生图/FLUX文生图-丝袜真人美女_1903378795104215041.json, 图片生成/文生图/FLUX文生图-姿势切换丝袜真人美女_1926495843577176065.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_latent_upscale_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/FLUX文生图-丝袜真人美女_1903378795104215041.json、图片生成/文生图/FLUX文生图-姿势切换丝袜真人美女_1926495843577176065.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApplySingle_v2`
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Text Input Switch (4 way)`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `GetNode`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `Int`
- `InversionDemoLazyIndexSwitch`
- `JjkText`
- `JoinStrings`
- `KSamplerSelect`
- `LatentUpscaleBy`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SDXLEmptyLatentSizePicker+`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy showAnything`
- `workflow>gguf-sample`
- `workflow>save`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |
| ControlNet 权重 | 0.7 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1.5 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
