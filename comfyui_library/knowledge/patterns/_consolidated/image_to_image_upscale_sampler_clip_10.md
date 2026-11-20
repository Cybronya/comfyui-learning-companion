---
name: image_to_image_upscale_sampler_clip_10
type: Image To Image
frequency: 12
level: strong
coverage: 0.857583
common_nodes: [CLIPLoader, CLIPTextEncode, ImageListToImageBatch, ImageUpscaleWithModel, KSampler, LoadImage, ModelSamplingSD3, PreviewImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/wan高清写实放大api_1957979462142935041.json, 图片生成/图生图/【CQ808】高清放大-WAN2.2_联合_TTP_超级-键4K放大_2115962186911801345.json, 图片生成/图生图/【CQ808】高清放大-WAN2.2_联合_TTP_超级-键4K放大_2115973086964183041.json, 图片生成/图生图/万相2.2高清放大TTP放大_1946954453464952834.json, 图片生成/文生图/Wan2.2 TTP高阶放大（全网ID ：楚门的AI世界）_1950100432455647233.json, 平台全量/Upscaler高清放大修复画面细节 增加清晰度_1965943372391321602.json, 平台全量/Wan2.2 - 14B - 加速版 - TTP 图片放大_1950200138313678850.json, 平台全量/Wan2.2-14B加速版TTP图片放大ttp加速插画图片放大图片高清图片细节放大_1998608845691846658.json, 平台全量/【CQ808】高清放大-WAN2.2 联合 TTP 超级-键4K放大_2033473002561609729.json, 平台全量/【CQ808】高清放大-WAN2.2 联合 TTP 超级-键4K放大_2047202358995718145.json, 平台全量/图片增强4K_1951210818199334913.json, 平台全量/图片高清-V2版本_2051154656180617217.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/wan高清写实放大api_1957979462142935041.json、图片生成/图生图/【CQ808】高清放大-WAN2.2_联合_TTP_超级-键4K放大_2115962186911801345.json、图片生成/图生图/【CQ808】高清放大-WAN2.2_联合_TTP_超级-键4K放大_2115973086964183041.json、图片生成/图生图/万相2.2高清放大TTP放大_1946954453464952834.json、图片生成/文生图/Wan2.2 TTP高阶放大（全网ID ：楚门的AI世界）_1950100432455647233.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
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
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/12 个有
- `easy cleanGpuUsed` —— 11/12 个有
- `ImageScaleToTotalPixels` —— 10/12 个有
- `Label (rgthree)` —— 5/12 个有
- `Image Comparer (rgthree)` —— 4/12 个有
- `Anything Everywhere3` —— 2/12 个有
- `ConstrainImage|pysssss` —— 2/12 个有
- `GetImageSize` —— 1/12 个有
- `LayerUtility: BooleanOperatorV2` —— 1/12 个有
- `LayerUtility: If ` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `easy imageScaleDownToSize` —— 1/12 个有
- `easy int` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 10 | 12 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | heun | - | 12 | 92% |
| 调度器 | beta | - | 12 | 92% |
| 重绘幅度 | 0.1 | 0.08 - 0.2 | 12 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 10，12 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，12 个样本，一致性 92%
- 调度器 最常用 beta，12 个样本，一致性 92%
- 重绘幅度 中位数 0.1，观测区间 0.08 - 0.2，12 个样本
- 风险：重绘幅度 观测到 0.08，低于常用下限 0.1（）
