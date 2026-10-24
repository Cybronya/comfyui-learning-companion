---
name: unknown_workflow_upscale_sampler_clip_9
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.79625
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, Fast Groups Muter (rgthree), FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSamplerSelect, LayerUtility: BooleanOperator, LoadImage, MathExpression|pysssss, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy ifElse, easy imageSize, easy imageSizeBySide]
problems: []
missing: []
members: [图片生成/图生图/FLUX 图片放大_1951546972727660546.json, 图片生成/图生图/图像放大_FLUX  KREA+TTP(4步lora加速版)_1958709608397303810.json, 图片生成/图生图/图片放大_FLUX+TTP(加速版)_1964970443709009922.json, 图片生成/图生图/图片高清细节放大_1971399258912014338.json, 图片生成/图生图/姿势迁移+清晰放大_1980532329577889794.json, 图片生成/图生图/放大_FLUX+TTP(加速版)_1901535975481450497.json, 图片生成/图生图/放大_FLUX+TTP(常用版)_1901536141084868610.json, 图片生成/图生图/禾筑AIARCH建筑美化工作流_1963204850215530497.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX 图片放大_1951546972727660546.json、图片生成/图生图/图像放大_FLUX  KREA+TTP(4步lora加速版)_1958709608397303810.json、图片生成/图生图/图片放大_FLUX+TTP(加速版)_1964970443709009922.json、图片生成/图生图/图片高清细节放大_1971399258912014338.json、图片生成/图生图/姿势迁移+清晰放大_1980532329577889794.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSamplerSelect`
- `LayerUtility: BooleanOperator`
- `LoadImage`
- `MathExpression|pysssss`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageSize`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 6/8 个有
- `ImageResizeKJ` —— 6/8 个有
- `LoraLoader` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `Textbox` —— 3/8 个有
- `CR Image Input Switch` —— 2/8 个有
- `CR Text Concatenate` —— 2/8 个有
- `Float` —— 2/8 个有
- `ImageScaleBy` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `RH_Captioner` —— 2/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `easy int` —— 2/8 个有
- `CLIPVisionEncode` —— 1/8 个有
- `CLIPVisionLoader` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `FramePackLoraSelect` —— 1/8 个有
- `FramePackSingleFrameSampler` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `LoadFramePackModel` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `RH_Nano_Banana_Image2Image` —— 1/8 个有
- `TextBox1` —— 1/8 个有
- `easy imageConcat` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | -7.72 - 1 | 6 | 0% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 -7.72 - 1，6 个样本，取值分散，一致性仅 0%
