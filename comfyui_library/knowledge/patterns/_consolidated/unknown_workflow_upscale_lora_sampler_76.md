---
name: unknown_workflow_upscale_lora_sampler_76
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.976
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader_Any, CLIPTextEncode, ImageScaleBy, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImageJPG_GH, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: []
missing: []
members: [图片生成/文生图/MOSS模型文生图加真实人物质感_2113812843035455490.json, 视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088069964401041409.json, 视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088143314515226625.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_76

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/MOSS模型文生图加真实人物质感_2113812843035455490.json、视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088069964401041409.json、视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088143314515226625.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImageJPG_GH`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader_Any`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader_Any`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `CLIPLoader` —— 1/3 个有
- `EmptyFlux2LatentImage` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `SkipLayerGuidanceDiTSimple` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `VAELoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | sgm_uniform | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
