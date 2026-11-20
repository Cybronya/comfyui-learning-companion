---
name: unknown_workflow_upscale_sampler_clip_62
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8005
common_nodes: [CLIPTextEncode, ConcatText_Zho, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxSamplerParams+, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, LoadImage, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/一键毛孔级高清修复图片、人像风景宠物摄影等适用 flux-ttp_1927287507900125186.json, 平台全量/一键毛孔级高清修复图片、人像风景宠物摄影等适用 flux-ttp_1930639689907417090.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键毛孔级高清修复图片、人像风景宠物摄影等适用 flux-ttp_1927287507900125186.json、平台全量/一键毛孔级高清修复图片、人像风景宠物摄影等适用 flux-ttp_1930639689907417090.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConcatText_Zho`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxSamplerParams+`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
