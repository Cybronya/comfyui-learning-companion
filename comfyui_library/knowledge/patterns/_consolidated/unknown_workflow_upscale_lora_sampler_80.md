---
name: unknown_workflow_upscale_lora_sampler_80
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.844
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, EmptyHunyuanLatentVideo, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageListToImageBatch, ImageScaleBy, ImageUpscaleWithModel, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, PrimitiveBoolean, RH_Prompter, RH_Translator, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Multiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy ifElse, easy imageBatchToImageList, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1950913071642509313.json, 图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953.json, 图片生成/文生图/Wan2.2 电影级文生图 + 提示词润色+TTP高清放大_1953395549405937666.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_80

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1950913071642509313.json、图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953.json、图片生成/文生图/Wan2.2 电影级文生图 + 提示词润色+TTP高清放大_1953395549405937666.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `EmptyHunyuanLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveBoolean`
- `RH_Prompter`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Multiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 3 | 0% |
| 采样算法 | heun | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 0.1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 heun，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
