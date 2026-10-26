---
name: text_to_image_lora_sampler_clip_201
type: Text To Image
frequency: 9
level: strong
coverage: 0.847556
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/360°任意视角+高斯喷溅生图_2041889802005516290.json, 图片生成/图生图/360°任意视角—自由编辑图生图_2011726957599268866.json, 图片生成/图生图/【推荐】360°任意视角—自由编辑图生图_2011865122460930049.json, 图片生成/图生图/【自用】任意视角_2054837567236911105.json, 图片生成/图生图/任意角度调节_2054468883075084289.json, 图片生成/图生图/图上图-调角度_2035945557197328385.json, 图片生成/图生图/多视角+高斯泼溅 二合一_2011816749838114817.json, 图片生成/图生图/高斯泼溅VS多视角_2010358064557334530.json, 图片生成/图生图/高斯泼溅多角度-rubby_2014656322096078850.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_201

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/360°任意视角+高斯喷溅生图_2041889802005516290.json、图片生成/图生图/360°任意视角—自由编辑图生图_2011726957599268866.json、图片生成/图生图/【推荐】360°任意视角—自由编辑图生图_2011865122460930049.json、图片生成/图生图/【自用】任意视角_2054837567236911105.json、图片生成/图生图/任意角度调节_2054468883075084289.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `MemoryCleaner` —— 8/9 个有
- `LayerUtility: ImageReel` —— 7/9 个有
- `LayerUtility: ImageReelComposit` —— 7/9 个有
- `CFGNorm` —— 5/9 个有
- `CR Prompt Text` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/9 个有
- `INTConstant` —— 5/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `ModelSamplingAuraFlow` —— 5/9 个有
- `VAEEncode` —— 5/9 个有
- `LoadSharpModel` —— 3/9 个有
- `SharpPredict` —— 3/9 个有
- `YCGaussianPreview` —— 3/9 个有
- `GetImageSize` —— 2/9 个有
- `Note _O` —— 2/9 个有
- `easy imageScaleDownToSize` —— 2/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1280 - 1280 | 9 | 100% |
| 高度 | 720 | 720 - 720 | 9 | 100% |
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler_ancestral | - | 9 | 100% |
| 调度器 | beta57 | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 1280 - 1280，9 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，9 个样本，一致性 100%
- 调度器 最常用 beta57，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（14/9 个样本）：Steps较低可能导致细节不足
