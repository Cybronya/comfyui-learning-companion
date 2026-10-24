---
name: unknown_workflow_upscale_lora_sampler_97
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.944
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/小脸崩坏修复、细节修复，flux万能修复工作流_1927318504762925057.json, 图片生成/图生图/建筑线稿转实景_1835251994864021505.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_97

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/小脸崩坏修复、细节修复，flux万能修复工作流_1927318504762925057.json、图片生成/图生图/建筑线稿转实景_1835251994864021505.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `Joy_caption_two`
- `Joy_caption_two_load`
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
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ArgosTranslateTextNode` —— 1/2 个有
- `CLIPSetLastLayer` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ControlNetApplySD3` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `FloatSlider` —— 1/2 个有
- `IPAdapter` —— 1/2 个有
- `IPAdapterUnifiedLoader` —— 1/2 个有
- `JjkShowText` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LayerUtility: GetImageSize` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| 采样步数 | randomize | - | 1 | 100% |
| Prompt 约束强度(CFG) | 25 | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | euler_ancestral | - | 1 | 100% |
| 重绘幅度 | karras | - | 1 | 100% |
| ControlNet 权重 | 0.6 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
