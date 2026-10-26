---
name: text_to_image_video_lora_sampler_153
type: Text To Image
frequency: 4
level: strong
coverage: 0.42675
common_nodes: [Any2ListNode, Audio Duration (mtb), AudioCrop, AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DiffusionModelLoaderKJ, EmptyLatentImage, GetNode, ImageBatch, ImageFromBatch, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchLoader, PreviewAny, PreviewAudio, PreviewImage, PrimitiveFloat, SetNode, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy indexAnything, easy int, easy promptLine, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/InfiniteTalk数字人单人图像驱动32秒版本，数字人生成工作流_2103248055586873346.json, 数字人/数字人/InfiniteTalk数字人图像驱动 32秒单人视频生成工具_2114059597593010177.json, 数字人/数字人/鼎子InfiniteTalk数字人单人图像驱动｜32秒版本_2114011264488927234.json, 视频生成/图生视频/YZ金鱼单人InfiniteTalk官方版｜图生视频对口型驱动_2110726337492250626.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_153

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/InfiniteTalk数字人单人图像驱动32秒版本，数字人生成工作流_2103248055586873346.json、数字人/数字人/InfiniteTalk数字人图像驱动 32秒单人视频生成工具_2114059597593010177.json、数字人/数字人/鼎子InfiniteTalk数字人单人图像驱动｜32秒版本_2114011264488927234.json、视频生成/图生视频/YZ金鱼单人InfiniteTalk官方版｜图生视频对口型驱动_2110726337492250626.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：43%

## 共有节点

全部 4 个 workflow 都包含：
- `Any2ListNode`
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DiffusionModelLoaderKJ`
- `EmptyLatentImage`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `PreviewAny`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveFloat`
- `SetNode`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy indexAnything`
- `easy int`
- `easy promptLine`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 34/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（34/4 个样本）：Steps较低可能导致细节不足
