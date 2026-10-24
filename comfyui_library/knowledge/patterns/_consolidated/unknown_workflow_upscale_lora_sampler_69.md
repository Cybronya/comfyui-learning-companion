---
name: unknown_workflow_upscale_lora_sampler_69
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.848
common_nodes: [CLIPLoader, CLIPTextEncode, ClownsharKSampler_Beta, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, JWStringConcat, LoadImage, LoraLoader, SaveImage, Seed (rgthree), ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, WD14Tagger|pysssss, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/文生图/Anima Preview3分块放大_2042211302168338434.json, 图片生成/文生图/Anima-Base分块放大_2055118475793838082.json, 图片生成/文生图/WAI-ANIMA分块放大_2046194195202838530.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_69

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Anima Preview3分块放大_2042211302168338434.json、图片生成/文生图/Anima-Base分块放大_2055118475793838082.json、图片生成/文生图/WAI-ANIMA分块放大_2046194195202838530.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `JWStringConcat`
- `LoadImage`
- `LoraLoader`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `KepStringLiteral` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.85 | 0.85 - 0.85 | 3 | 100% |
| LoRA 文本强度 | 0.85 | 0.85 - 0.85 | 3 | 100% |
| 采样步数 | beta57 | - | 3 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 25 | 3 | 89% |
| 采样算法 | -1 | -1 - -1 | 3 | 100% |
| 调度器 | 0.3 | 0.3 - 0.3 | 3 | 100% |
| 重绘幅度 | 2 | 2 - 2 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.85，观测区间 0.85 - 0.85，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.85，观测区间 0.85 - 0.85，3 个样本，取值集中（一致性 100%）
- 采样步数 最常用 beta57，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- 采样算法 中位数 -1，观测区间 -1 - -1，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 2，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
