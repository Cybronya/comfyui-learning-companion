---
name: unknown_workflow_upscale_lora_sampler_50
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8368
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ClipInterrogator, ConditioningAverage, Constant Number, DualCLIPLoader, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_CoordinateSplitter, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, UNETLoader, UpscaleModelLoader, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageInsetCrop]
problems: []
missing: []
members: [图片生成/图生图/supir高清放大-在线生图_1909073050640523266.json, 图片生成/图生图/大场景风光-8K_1994718178498449409.json, 图片生成/图生图/小尺寸人像极致放大去模糊_1908813830091382785.json, 图片生成/文生图/大场景风光-8K_1904167132723056641.json, 平台全量/TTP模糊人像高清修复放大专用工作流_1912706184464297986.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_50

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/supir高清放大-在线生图_1909073050640523266.json、图片生成/图生图/大场景风光-8K_1994718178498449409.json、图片生成/图生图/小尺寸人像极致放大去模糊_1908813830091382785.json、图片生成/文生图/大场景风光-8K_1904167132723056641.json、平台全量/TTP模糊人像高清修复放大专用工作流_1912706184464297986.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ClipInterrogator`
- `ConditioningAverage`
- `Constant Number`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_CoordinateSplitter`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTP_condsetarea_merge`
- `TTP_condtobatch`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Anything Everywhere` —— 3/5 个有
- `ImageCompositeFromMaskBatch+` —— 3/5 个有
- `ImageScale` —— 3/5 个有
- `LayerMask: MaskGrow` —— 3/5 个有
- `LayerMask: SegmentAnythingUltra` —— 3/5 个有
- `ReActorRestoreFace` —— 3/5 个有
- `VAEDecodeTiled` —— 3/5 个有
- `workflow>4xnomos` —— 3/5 个有
- `ChinesePrompt_Mix` —— 2/5 个有
- `DetailDaemonSamplerNode` —— 2/5 个有
- `VAEDecode` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `EmptyLatentImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1152 | - | 1 | 100% |
| 高度 | 768 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
