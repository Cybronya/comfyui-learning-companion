---
name: unknown_workflow_upscale_lora_sampler_37
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.899167
common_nodes: [CLIPLoader, CLIPTextEncode, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Wan2.2  高质量文生图  TTP高清放大_1950577515129655297.json, 图片生成/文生图/Wan2.2文生图+TTP放大_1951143607715737601.json, 图片生成/文生图/Wan2.2质量文生图+TTP高阶放大_1950457350153003010.json, 图片生成/文生图/Wan2.2质量文生图+TTP高阶放大（全网ID ：楚门的AI世界）_1950100592413818881.json, 图片生成/文生图/wan2.2文生图 高清放大_1950888087578681345.json, 图片生成/文生图/wan2.2文生图_效果惊艳_美感升级_1950394501548433410.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Wan2.2  高质量文生图  TTP高清放大_1950577515129655297.json、图片生成/文生图/Wan2.2文生图+TTP放大_1951143607715737601.json、图片生成/文生图/Wan2.2质量文生图+TTP高阶放大_1950457350153003010.json、图片生成/文生图/Wan2.2质量文生图+TTP高阶放大（全网ID ：楚门的AI世界）_1950100592413818881.json、图片生成/文生图/wan2.2文生图 高清放大_1950888087578681345.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `EmptyHunyuanLatentVideo` —— 4/6 个有
- `KSamplerAdvanced` —— 4/6 个有
- `SaveAnimatedWEBP` —— 3/6 个有
- `Anything Everywhere3` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `RH_Prompter` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `SDXLEmptyLatentSizePicker+` —— 2/6 个有
- `easy seed` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `easy getNode` —— 1/6 个有
- `easy setNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 6 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | heun | - | 6 | 83% |
| 调度器 | beta | - | 6 | 83% |
| 重绘幅度 | 0.1 | 0.06 - 1 | 6 | 0% |
| 宽度 | 768x1280 (0.6) | - | 2 | 50% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，6 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 83%
- 重绘幅度 中位数 0.1，观测区间 0.06 - 1，6 个样本，取值分散，一致性仅 0%
- 宽度 最常用 768x1280 (0.6)，2 个样本，一致性 50%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 0.06，低于常用下限 0.1（）
