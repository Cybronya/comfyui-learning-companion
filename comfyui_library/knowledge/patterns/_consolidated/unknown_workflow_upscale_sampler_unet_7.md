---
name: unknown_workflow_upscale_sampler_unet_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6105
common_nodes: [AIO_Preprocessor, Anything Everywhere3, CLIPLoader, ComfySwitchNode, EmptyLatentImage, FloatConstant, GetImageSize, GetImageSize+, Image Comparer (rgthree), ImageConcatMulti, ImageResize+, ImageScaleBy, JsonExtractString, KOOK_SaveJPGImage, KSamplerAdvanced, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewAny, PreviewImage, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, QwenImage21Cache, QwenMultiangleCameraNode, ResolutionSelector, RunningHub Deepcleaner, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, TextGenerate, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy positive, 忽略多组孤海]
problems: []
missing: [Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, RunningHub Deepcleaner, SimpleMath+, easy positive, 忽略多组孤海, GetImageSize+, ImageResize+, Seed (rgthree)]
members: [图片生成/图生图/2105998336317804545.json, 图片生成/文生图/Q2.1-全能工作流_2105998336317804545.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2105998336317804545.json、图片生成/文生图/Q2.1-全能工作流_2105998336317804545.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `FloatConstant`
- `GetImageSize`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `ImageResize+`
- `ImageScaleBy`
- `JsonExtractString`
- `KOOK_SaveJPGImage`
- `KSamplerAdvanced`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `QwenMultiangleCameraNode`
- `ResolutionSelector`
- `RunningHub Deepcleaner`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy positive`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 25 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、LayerUtility: ImageScaleByAspectRatio V2、RunningHub Deepcleaner、SimpleMath+、easy positive
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
