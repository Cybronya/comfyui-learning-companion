---
name: image_to_image_controlnet_video_lora
type: Image To Image
frequency: 2
level: weak
coverage: 0.8825
common_nodes: [BatchCount+, CLIPTextEncode, ChangeImageBatchSize //Inspire, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, CreateShapeMask, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, ImageBatch, ImageCompositeBy_Zho, ImageListToImageBatch, ImageScaleToTotalPixels, ImageToMask, ImpactImageBatchToImageList, JoinImageWithAlpha, KSampler, LoadImage, LoraLoader, MaskToImage, MasksToMaskList, PreviewImage, SolidMask, VAEDecode, VAEEncode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Ghibli 吉卜力转场动画_1909785208340840449.json, 视频生成/图生视频/Ghibli 吉卜力转成动画 ｜一键生成视频系列_1907380226249396226.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_video_lora

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Ghibli 吉卜力转场动画_1909785208340840449.json、视频生成/图生视频/Ghibli 吉卜力转成动画 ｜一键生成视频系列_1907380226249396226.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BatchCount+`
- `CLIPTextEncode`
- `ChangeImageBatchSize //Inspire`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `CreateShapeMask`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
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
- `ConcatTextOfUtils` —— 1/2 个有
- `SDVN Joy Caption` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.8 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.75 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
