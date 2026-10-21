---
name: unknown_workflow_upscale_lora_sampler_19
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.845
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoraLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate, LayerMask: LoadFlorence2Model, easy imageBatchToImageList, LayerUtility: Florence2Image2Prompt, Preview from image [Crystools]]
members: [图片生成/文生图/1954519876507451393.json, 图片生成/文生图/1986047424126996481.json, 图片生成/文生图/AI动画文生图_2026095152678309890.json, 图片生成/文生图/千问+CG动漫角色_2005905611554521089.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1954519876507451393.json、图片生成/文生图/1986047424126996481.json、图片生成/文生图/AI动画文生图_2026095152678309890.json、图片生成/文生图/千问+CG动漫角色_2005905611554521089.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `EmptySD3LatentImage` —— 3/4 个有
- `KSampler` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LayerMask: LoadFlorence2Model` —— 2/4 个有
- `LayerUtility: Florence2Image2Prompt` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `Preview from image [Crystools]` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 16 - 20 | 3 | 90% |
| Prompt 约束强度(CFG) | 2.5 | 2 - 3.5 | 3 | 77% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 4 | 90% |
| LoRA 文本强度 | 0.9 | 0.8 - 1 | 4 | 89% |
| 宽度 | 1360 | - | 1 | 100% |
| 高度 | 768 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 16 - 20，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2 - 3.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，4 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 0.9，观测区间 0.8 - 1，4 个样本，取值集中（一致性 89%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、LayerMask: LoadFlorence2Model、easy imageBatchToImageList、LayerUtility: Florence2Image2Prompt、Preview from image [Crystools]
