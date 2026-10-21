---
name: unknown_workflow_upscale_lora_sampler_8
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.679857
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageListToImageBatch, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: [easy cleanGpuUsed, easy imageBatchToImageList, CR Text, CR Text Concatenate, SDXLEmptyLatentSizePicker+, easy seed, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, Text Multiline, easy int, easy imageSize]
members: [图片生成/文生图/1950100592413818881.json, 图片生成/文生图/1950394501548433410.json, 图片生成/文生图/1950457350153003010.json, 图片生成/文生图/1950888087578681345.json, 图片生成/文生图/1950913071642509313.json, 图片生成/文生图/1953395549405937666.json, 图片生成/文生图/1954735113898749953.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_8

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1950100592413818881.json、图片生成/文生图/1950394501548433410.json、图片生成/文生图/1950457350153003010.json、图片生成/文生图/1950888087578681345.json、图片生成/文生图/1950913071642509313.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
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
- `EmptyHunyuanLatentVideo` —— 5/7 个有
- `KSamplerAdvanced` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `RH_Prompter` —— 5/7 个有
- `RH_Translator` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `CR Text Concatenate` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `ImageScaleBy` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `MathExpression|pysssss` —— 3/7 个有
- `PrimitiveBoolean` —— 3/7 个有
- `Text Multiline` —— 3/7 个有
- `easy ifElse` —— 3/7 个有
- `easy imageSize` —— 3/7 个有
- `easy int` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `SDXLEmptyLatentSizePicker+` —— 2/7 个有
- `SaveAnimatedWEBP` —— 2/7 个有
- `easy seed` —— 2/7 个有
- `GetNode` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 7 | 0% |
| 采样算法 | heun | - | 7 | 71% |
| 调度器 | beta | - | 7 | 71% |
| 重绘幅度 | 0.1 | 0.06 - 1 | 6 | 0% |
| 宽度 | 1280x768 (1.67) | - | 2 | 50% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，7 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 heun，7 个样本，一致性 71%
- 调度器 最常用 beta，7 个样本，一致性 71%
- 重绘幅度 中位数 0.1，观测区间 0.06 - 1，6 个样本，取值分散，一致性仅 0%
- 宽度 最常用 1280x768 (1.67)，2 个样本，一致性 50%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 0.06，低于常用下限 0.1（）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、easy imageBatchToImageList、CR Text、CR Text Concatenate、SDXLEmptyLatentSizePicker+
