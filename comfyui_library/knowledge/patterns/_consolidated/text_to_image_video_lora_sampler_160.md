---
name: text_to_image_video_lora_sampler_160
type: Text To Image
frequency: 3
level: strong
coverage: 0.929667
common_nodes: [AutoCropFaces, CLIPLoader, CLIPTextEncode, ColorMatch, CreateVideo, EmptyLatentImage, FFmpeg_LoadVideoFromURL_JX, Float, GetImageSizeAndCount, GetVideoComponents, ImageBatch, ImageBatchRepeatInterleaving, ImageCASharpening+, ImageConcatMulti, ImageFromBatch+, ImageScale, ImageScaleToTotalPixels, JjkText, KSampler, LoadImage, LoadVideo, LoraLoaderModelOnly, MathExpression|pysssss, Pick From Batch (mtb), PreviewImage, RepeatImageBatch, RunningHub_DreamID-V_Loader, RunningHub_DreamID-V_Sampler, SaveVideo, UNETLoader, VAEDecode, VAELoader, VHS_SelectEveryNthImage, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/DreamID一键面部替换直出｜视频换脸图生图_2089695572570759169.json, 图片生成/图生图/DreamID视频换脸处理生成工作流工具包_2101382827316170754.json, 图片生成/图生图/视频换脸｜DreamID 一键面部替换直出_2089341677751328769.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_160

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/DreamID一键面部替换直出｜视频换脸图生图_2089695572570759169.json、图片生成/图生图/DreamID视频换脸处理生成工作流工具包_2101382827316170754.json、图片生成/图生图/视频换脸｜DreamID 一键面部替换直出_2089341677751328769.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `AutoCropFaces`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `CreateVideo`
- `EmptyLatentImage`
- `FFmpeg_LoadVideoFromURL_JX`
- `Float`
- `GetImageSizeAndCount`
- `GetVideoComponents`
- `ImageBatch`
- `ImageBatchRepeatInterleaving`
- `ImageCASharpening+`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `RepeatImageBatch`
- `RunningHub_DreamID-V_Loader`
- `RunningHub_DreamID-V_Sampler`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectEveryNthImage`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
