---
name: unknown_workflow_upscale_sampler_clip_84
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8165
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ConditioningAverage, Constant Number, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TTP_CoordinateSplitter, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAELoader, easy imageBatchToImageList, easy imageInsetCrop]
problems: []
missing: []
members: [平台全量/多模型可选-高清修复_1918559604182290434.json, 平台全量/高清人像放大_1899750238616170498.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/多模型可选-高清修复_1918559604182290434.json、平台全量/高清人像放大_1899750238616170498.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningAverage`
- `Constant Number`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_CoordinateSplitter`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTP_condsetarea_merge`
- `TTP_condtobatch`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImageSharpen` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `Miaoshouai_Tagger` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `VAEEncodeTiled` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
