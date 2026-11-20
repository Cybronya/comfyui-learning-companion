---
name: image_to_image_lora_sampler_checkpoint_6
type: Image To Image
frequency: 5
level: moderate
coverage: 0.5464
common_nodes: [CFGNorm, CR Prompt Text, CheckpointLoaderSimple, INTConstant, Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-2511-AIO-单图-双图-三图_2004370340950278146.json, 图片生成/图生图/Qwen-AIO单_双_三图编辑_2010261352249561089.json, 图片生成/图生图/单图编辑_2007256291760152578.json, 图片生成/文生图/【尺素】Qwen-AIO图像编辑集合_2074882464908136449.json, 平台全量/Qwen-Rapid-AIO--单图编辑  添加文字 去除图案等_2079816997495459842.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-2511-AIO-单图-双图-三图_2004370340950278146.json、图片生成/图生图/Qwen-AIO单_双_三图编辑_2010261352249561089.json、图片生成/图生图/单图编辑_2007256291760152578.json、图片生成/文生图/【尺素】Qwen-AIO图像编辑集合_2074882464908136449.json、平台全量/Qwen-Rapid-AIO--单图编辑  添加文字 去除图案等_2079816997495459842.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `INTConstant`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/5 个有
- `PlaySound|pysssss` —— 4/5 个有
- `EmptyLatentImage` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `DWPreprocessor` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `GetImage` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 512 - 1920 | 3 | 54% |
| 高度 | 1280 | 512 - 1280 | 3 | 65% |
| 采样步数 | 4 | 4 - 6 | 5 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 512 - 1920，3 个样本
- 高度 中位数 1280，观测区间 512 - 1280，3 个样本
- 采样步数 中位数 4，观测区间 4 - 6，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
