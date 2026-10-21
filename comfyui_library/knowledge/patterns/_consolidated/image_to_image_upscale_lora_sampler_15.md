---
name: image_to_image_upscale_lora_sampler_15
type: Image To Image
frequency: 2
level: weak
coverage: 0.696
common_nodes: [CLIPLoader, CLIPTextEncode, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: [easy cleanGpuUsed, easy imageBatchToImageList, easy anythingIndexSwitch]
members: [图片生成/文生图/1950100432455647233.json, 图片生成/文生图/1950730887648448513.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1950100432455647233.json、图片生成/文生图/1950730887648448513.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
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
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SaveAnimatedWEBP` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 10.5 | - | 2 | 10% |
| 采样算法 | 3.5 | - | 1 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 0.1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 10.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 10%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、easy imageBatchToImageList、easy anythingIndexSwitch
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
