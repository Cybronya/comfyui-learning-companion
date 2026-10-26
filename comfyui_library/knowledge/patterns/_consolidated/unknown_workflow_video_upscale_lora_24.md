---
name: unknown_workflow_video_upscale_lora_24
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.864
common_nodes: [Any Switch (rgthree), BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, DetailDaemonSamplerNode, DisableNoise, Fast Groups Muter (rgthree), ImageListToImageBatch, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, SaveImage, SplitSigmas, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WanVideoNAG]
problems: []
missing: []
members: [图片生成/图生图/[🛫书墨]wan2.2图像低降噪全屏洗图+TTP放大_1952380443255607298.json, 图片生成/文生图/[🛫书墨]wan2.2文生图+ttp2倍_1952329723617718274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/[🛫书墨]wan2.2图像低降噪全屏洗图+TTP放大_1952380443255607298.json、图片生成/文生图/[🛫书墨]wan2.2文生图+ttp2倍_1952329723617718274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DetailDaemonSamplerNode`
- `DisableNoise`
- `Fast Groups Muter (rgthree)`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SplitSigmas`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerMask: LoadFlorence2Model` —— 1/2 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
