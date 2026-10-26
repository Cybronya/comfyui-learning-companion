---
name: unknown_workflow_upscale_sampler_clip_58
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8275
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, easy cleanGpuUsed, easy int]
problems: []
missing: []
members: [图片生成/文生图/Z-Image-文生图-超高清放大_2101279706992697346.json, 图片生成/文生图/节点系列08-setNode+getNode节点精讲-已发布_2010960746124943362.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_58

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image-文生图-超高清放大_2101279706992697346.json、图片生成/文生图/节点系列08-setNode+getNode节点精讲-已发布_2010960746124943362.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageCASharpening+` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy mathInt` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 872 | - | 2 | 83% |
| 高度 | 1408 | - | 2 | 91% |
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 11 | - | 2 | 91% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 872，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1408，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
