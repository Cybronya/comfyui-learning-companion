---
name: unknown_workflow_lora_sampler_clip_87
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.753
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/无损高清放大工作流｜一键超清_1914134415251861506.json, 图片生成/图生图/无损高清放大工作流｜一键超清_1942154651460595713.json, 平台全量/F.1-HD-title-2025.5.21_1967505204423823361.json, 平台全量/Flux_tile场景高清放大_1922687693023580161.json, 平台全量/flux高清放大-在线生图4K（TTP）_1963867118193430530.json, 平台全量/山口组-放大_1944975410481520641.json, 平台全量/无损高清TTP放大工作流｜一键超清_人像放大_1925166311016755202.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_87

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/无损高清放大工作流｜一键超清_1914134415251861506.json、图片生成/图生图/无损高清放大工作流｜一键超清_1942154651460595713.json、平台全量/F.1-HD-title-2025.5.21_1967505204423823361.json、平台全量/Flux_tile场景高清放大_1922687693023580161.json、平台全量/flux高清放大-在线生图4K（TTP）_1963867118193430530.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 6/7 个有
- `easy imageBatchToImageList` —— 6/7 个有
- `GetNode` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `ImageResizeKJ` —— 4/7 个有
- `ImageUpscaleWithModel` —— 4/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `UpscaleModelLoader` —— 4/7 个有
- `ColorMatch` —— 3/7 个有
- `Florence2ModelLoader` —— 3/7 个有
- `Florence2Run` —— 3/7 个有
- `workflow>放大预处理` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `FloatConstant` —— 1/7 个有
- `ImageScaleBy` —— 1/7 个有
- `ImageSharpen` —— 1/7 个有
- `ImpactImageBatchToImageList` —— 1/7 个有
- `JoyCaptionAlpha2Online` —— 1/7 个有
- `LayerUtility: JoyCaption2ExtraOptions` —— 1/7 个有
- `LoraLoader|pysssss` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `Reroute (rgthree)` —— 1/7 个有
- `Text Concatenate (JPS)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
