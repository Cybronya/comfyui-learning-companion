---
name: text_to_image_video_lora_sampler_130
type: Text To Image
frequency: 5
level: strong
coverage: 0.5554
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImagesFromBatchIndexed, INTConstant, Image Comparer (rgthree), Int, JoinStrings, KSampler, KSamplerAdvanced, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, PlaySound|pysssss, PreviewImage, Qwen3_VQA, QwenMultiangleCameraNode, RIFE VFI, ReferenceLatent, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlus, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, easy cleanGpuUsed, easy imageSize, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/可视化编辑视角+首尾帧视频大合集_2031599755595354114.json, 图片生成/图生图/可视化角度编辑转换+首尾帧视+动漫转真人合集_2017058733100113922.json, 视频生成/图生视频/Qwen image 一键动漫转真人+可视化编辑视角+首尾帧视频大合集_2010182153828569090.json, 视频生成/图生视频/动漫转真人+可视化编辑视角+首尾帧视频大合集_2009838590578139138.json, 视频生成/图生视频/动漫转真人_可视化编辑视角_首尾帧视频_2011030081191288834.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_130

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/可视化编辑视角+首尾帧视频大合集_2031599755595354114.json、图片生成/图生图/可视化角度编辑转换+首尾帧视+动漫转真人合集_2017058733100113922.json、视频生成/图生视频/Qwen image 一键动漫转真人+可视化编辑视角+首尾帧视频大合集_2010182153828569090.json、视频生成/图生视频/动漫转真人+可视化编辑视角+首尾帧视频大合集_2009838590578139138.json、视频生成/图生视频/动漫转真人_可视化编辑视角_首尾帧视频_2011030081191288834.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImagesFromBatchIndexed`
- `INTConstant`
- `Image Comparer (rgthree)`
- `Int`
- `JoinStrings`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PreviewImage`
- `Qwen3_VQA`
- `QwenMultiangleCameraNode`
- `RIFE VFI`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 5 | 65% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 5 | 80% |
| 重绘幅度 | normal | - | 5 | 80% |
| 宽度 | 1280 | 1280 - 1280 | 5 | 100% |
| 高度 | 720 | 720 - 720 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 80%
- 重绘幅度 最常用 normal，5 个样本，一致性 80%
- 宽度 中位数 1280，观测区间 1280 - 1280，5 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
