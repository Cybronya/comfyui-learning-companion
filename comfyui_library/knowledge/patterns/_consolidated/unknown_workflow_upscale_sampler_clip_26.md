---
name: unknown_workflow_upscale_sampler_clip_26
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.91625
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, FluxGuidance, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UpscaleModelLoader, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux超清放大_图像修复_1895074154842882049.json, 平台全量/TTP 一键高清修复放大，拒绝加班系列工具_1955678505768030210.json, 平台全量/flux ttp 高清放大 v1 版_1975119237314383874.json, 平台全量/flux脸部无变形人像放大_1917892743241072642.json, 平台全量/z image的TTP高清放大_1998777073697218561.json, 平台全量/【自然肌肤专修】人像精修+8K画质-傲雪AIGC_1979389388272603137.json, 平台全量/增加细节+X4倍放大+提示优化-傲雪AIGC_1958905491411906561.json, 平台全量/高清放大+增加细节-傲雪AIGC_1957662142747045890.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/Flux超清放大_图像修复_1895074154842882049.json、平台全量/TTP 一键高清修复放大，拒绝加班系列工具_1955678505768030210.json、平台全量/flux ttp 高清放大 v1 版_1975119237314383874.json、平台全量/flux脸部无变形人像放大_1917892743241072642.json、平台全量/z image的TTP高清放大_1998777073697218561.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `VAEDecodeTiled` —— 7/8 个有
- `easy imageBatchToImageList` —— 7/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `ImageListToImageBatch` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `CR Text Concatenate` —— 4/8 个有
- `KepStringLiteral` —— 4/8 个有
- `DeepTranslatorTextNode` —— 3/8 个有
- `LoraLoader` —— 3/8 个有
- `PlaySound|pysssss` —— 3/8 个有
- `ImageResizeKJ` —— 2/8 个有
- `ImageScaleBy` —— 2/8 个有
- `NunchakuFluxDiTLoader` —— 2/8 个有
- `ArgosTranslateTextNode` —— 1/8 个有
- `CLIPLoader` —— 1/8 个有
- `CR Simple Image Compare` —— 1/8 个有
- `Image Resize Factor (mtb)` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `NunchakuFluxLoraLoader` —— 1/8 个有
- `VAEDecode` —— 1/8 个有
- `easy imageListToImageBatch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
