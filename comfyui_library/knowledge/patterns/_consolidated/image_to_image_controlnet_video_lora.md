---
name: image_to_image_controlnet_video_lora
type: Image To Image
frequency: 3
level: strong
coverage: 0.855
common_nodes: [BatchCount+, CLIPTextEncode, ChangeImageBatchSize //Inspire, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, CreateShapeMask, ImageBatch, ImageCompositeBy_Zho, ImageListToImageBatch, ImageScaleToTotalPixels, ImageToMask, ImpactImageBatchToImageList, JoinImageWithAlpha, KSampler, LoadImage, LoraLoader, MaskToImage, MasksToMaskList, PreviewImage, SolidMask, VAEDecode, VAEEncode, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/图片转宫崎骏画风 吉卜力魔法 _ Ghibli Magic_1864556340139196417.json, 视频生成/图生视频/Ghibli 吉卜力转场动画_1909785208340840449.json, 视频生成/图生视频/Ghibli 吉卜力转成动画 ｜一键生成视频系列_1907380226249396226.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_video_lora

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/图片转宫崎骏画风 吉卜力魔法 _ Ghibli Magic_1864556340139196417.json、视频生成/图生视频/Ghibli 吉卜力转场动画_1909785208340840449.json、视频生成/图生视频/Ghibli 吉卜力转成动画 ｜一键生成视频系列_1907380226249396226.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `BatchCount+`
- `CLIPTextEncode`
- `ChangeImageBatchSize //Inspire`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `CreateShapeMask`
- `ImageBatch`
- `ImageCompositeBy_Zho`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageToMask`
- `ImpactImageBatchToImageList`
- `JoinImageWithAlpha`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `MaskToImage`
- `MasksToMaskList`
- `PreviewImage`
- `SolidMask`
- `VAEDecode`
- `VAEEncode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DepthAnything_V2` —— 2/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/3 个有
- `ConcatTextOfUtils` —— 1/3 个有
- `DepthAnythingPreprocessor` —— 1/3 个有
- `SDVN Joy Caption` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | 0.8 - 1 | 3 | 90% |
| 采样步数 | 20 | 4 - 20 | 3 | 49% |
| Prompt 约束强度(CFG) | 1.8 | 1.8 - 1.8 | 3 | 100% |
| 采样算法 | dpmpp_sde | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 0.75 | 0.75 - 0.75 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- 采样步数 中位数 20，观测区间 4 - 20，3 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1.8，观测区间 1.8 - 1.8，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 0.75，观测区间 0.75 - 0.75，3 个样本，取值集中（一致性 100%）
