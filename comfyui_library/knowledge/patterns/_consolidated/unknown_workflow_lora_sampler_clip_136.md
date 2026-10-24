---
name: unknown_workflow_lora_sampler_clip_136
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7455
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoader, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/不分块仅修复车身结构_2072852231782748161.json, 图片生成/图生图/分块仅修复车身结构_2061261942400049153.json, 图片生成/图生图/平台用—汽车图片8K放大+lora修复车身加速版_2059489770337816578.json, 图片生成/图生图/汽车图片8K放大+lora修复车身加速版_2056945533108973570.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_136

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/不分块仅修复车身结构_2072852231782748161.json、图片生成/图生图/分块仅修复车身结构_2061261942400049153.json、图片生成/图生图/平台用—汽车图片8K放大+lora修复车身加速版_2059489770337816578.json、图片生成/图生图/汽车图片8K放大+lora修复车身加速版_2056945533108973570.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageListToImageBatch` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `TTP_Image_Assy` —— 3/4 个有
- `TTP_Image_Tile_Batch` —— 3/4 个有
- `TTP_Tile_image_size` —— 3/4 个有
- `easy imageBatchToImageList` —— 3/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `InpaintCropImproved` —— 2/4 个有
- `InpaintStitchImproved` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `SAM3_Detect` —— 2/4 个有
- `Text` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `VAEDecode` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `LayerMask: MaskPreview` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
