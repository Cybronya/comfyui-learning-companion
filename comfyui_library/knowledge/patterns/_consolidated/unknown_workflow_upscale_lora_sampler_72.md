---
name: unknown_workflow_upscale_lora_sampler_72
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.897667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LoraLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen加速+超清工作流_1954519876507451393.json, 图片生成/文生图/千问+CG动漫角色_2005905611554521089.json, 图片生成/文生图/千问-文生图Q版+高清放大_1986047424126996481.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_72

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen加速+超清工作流_1954519876507451393.json、图片生成/文生图/千问+CG动漫角色_2005905611554521089.json、图片生成/文生图/千问-文生图Q版+高清放大_1986047424126996481.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
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
- `CR Text Concatenate` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LayerMask: LoadFlorence2Model` —— 2/3 个有
- `LayerUtility: Florence2Image2Prompt` —— 2/3 个有
- `TextInput_` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Preview from image [Crystools]` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 16 - 20 | 3 | 90% |
| Prompt 约束强度(CFG) | 2.5 | 2 - 3.5 | 3 | 77% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 3 | 89% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 3 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 16 - 20，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2 - 3.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，3 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
