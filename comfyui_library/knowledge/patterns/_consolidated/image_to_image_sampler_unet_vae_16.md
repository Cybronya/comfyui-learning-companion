---
name: image_to_image_sampler_unet_vae_16
type: Image To Image
frequency: 9
level: moderate
coverage: 0.865111
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen+Edit+2511三图编辑_2074110282011598849.json, 图片生成/图生图/Qwen-Edit 二次元转超写实真人_2019670658141134849.json, 图片生成/图生图/Qwen-Edit-2509 场景换视角工作流_2046950886362062849.json, 图片生成/图生图/Qwen-Edit-2509 测试_2003005793597288449.json, 图片生成/图生图/Qwen-Edit-2509 白底图换场景工作流_2091502540566388738.json, 图片生成/图生图/Qwen-Edit-2509-多角度切换_2000522237449039873.json, 图片生成/图生图/Qwen-Edit-2509_白底图换场景工作流_2097869384277643266.json, 图片生成/图生图/Qwen-Edit-2509_白底图换场景工作流_2099408627546284034.json, 图片生成/图生图/Qwen-image edit 2511 最新一图生成人物的全角度_2003698374991855618.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen+Edit+2511三图编辑_2074110282011598849.json、图片生成/图生图/Qwen-Edit 二次元转超写实真人_2019670658141134849.json、图片生成/图生图/Qwen-Edit-2509 场景换视角工作流_2046950886362062849.json、图片生成/图生图/Qwen-Edit-2509 测试_2003005793597288449.json、图片生成/图生图/Qwen-Edit-2509 白底图换场景工作流_2091502540566388738.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `PreviewImage` —— 6/9 个有
- `easy imageSize` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `ImageBlend` —— 3/9 个有
- `Mask Fill Holes` —— 3/9 个有
- `MaskToImage` —— 3/9 个有
- `Any Switch (rgthree)` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `easy promptLine` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `DWPreprocessor` —— 1/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `LayerMask: LoadFlorence2Model` —— 1/9 个有
- `LayerUtility: Collage` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `easy imageBatchToImageList` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 20 | 9 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 9 | 60% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
