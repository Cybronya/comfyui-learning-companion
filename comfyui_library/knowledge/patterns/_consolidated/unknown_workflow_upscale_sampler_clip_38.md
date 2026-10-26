---
name: unknown_workflow_upscale_sampler_clip_38
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.830667
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DownloadAndLoadFlorence2Model, Florence2Run, ImageUpscaleWithModel, KSamplerSelect, LoadImage, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/HiDream&TTP_1925414382111760386.json, 图片生成/图生图/Wan2.2分块超清放大_1950844011227578369.json, 图片生成/图生图/🐮老许Gary：WAN2.2分块超清放大_2017249178774151170.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/HiDream&TTP_1925414382111760386.json、图片生成/图生图/Wan2.2分块超清放大_1950844011227578369.json、图片生成/图生图/🐮老许Gary：WAN2.2分块超清放大_2017249178774151170.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
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

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `Florence2ModelLoader` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageSmartSharpen+` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `QuadrupleCLIPLoader` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.85 | - | 2 | 100% |
| LoRA 文本强度 | 0.85 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
