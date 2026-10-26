---
name: unknown_workflow_lora_sampler_clip_193
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.727333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoader, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/不分块仅修复车身结构_2072852231782748161.json, 图片生成/图生图/分块仅修复车身结构_2061261942400049153.json, 图片生成/图生图/平台用—汽车图片8K放大+lora修复车身加速版_2059489770337816578.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_193

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/不分块仅修复车身结构_2072852231782748161.json、图片生成/图生图/分块仅修复车身结构_2061261942400049153.json、图片生成/图生图/平台用—汽车图片8K放大+lora修复车身加速版_2059489770337816578.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
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
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/3 个有
- `ImageListToImageBatch` —— 2/3 个有
- `InpaintCropImproved` —— 2/3 个有
- `InpaintStitchImproved` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `SAM3_Detect` —— 2/3 个有
- `TTP_Image_Assy` —— 2/3 个有
- `TTP_Image_Tile_Batch` —— 2/3 个有
- `TTP_Tile_image_size` —— 2/3 个有
- `Text` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `easy imageBatchToImageList` —— 2/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有

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
