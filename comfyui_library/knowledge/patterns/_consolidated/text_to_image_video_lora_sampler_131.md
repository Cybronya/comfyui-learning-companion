---
name: text_to_image_video_lora_sampler_131
type: Text To Image
frequency: 5
level: strong
coverage: 0.8334
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, GetImageRangeFromBatch, GetNode, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/视频对口型InfiniteTalk数字人｜经典本角色一致性超稳_2100774100947001345.json, 图片生成/图生图/超自然数字人对口型方案，情感口播图生图制作_2110875851725295617.json, 数字人/数字人/InfiniTetalk超自然数字人对口型｜情感口播 人物类特效数字人_2104076796160466946.json, 数字人/数字人/InfiniteTalk单人对口型数字人 音频驱动口型同步_2099225085285593089.json, 视频生成/图生视频/InfiniTetalk音频驱动数字人｜电商带货图生视频_2096311256083951618.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_131

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/视频对口型InfiniteTalk数字人｜经典本角色一致性超稳_2100774100947001345.json、图片生成/图生图/超自然数字人对口型方案，情感口播图生图制作_2110875851725295617.json、数字人/数字人/InfiniTetalk超自然数字人对口型｜情感口播 人物类特效数字人_2104076796160466946.json、数字人/数字人/InfiniteTalk单人对口型数字人 音频驱动口型同步_2099225085285593089.json、视频生成/图生视频/InfiniTetalk音频驱动数字人｜电商带货图生视频_2096311256083951618.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LoadWanVideoT5TextEncoder` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `PlaySound|pysssss` —— 4/5 个有
- `WanVideoTextEncode` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `Anything Everywhere` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `WanVideoEncode` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `easy int` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `ColorCorrectOfUtils` —— 1/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/5 个有
- `FlashVSRNode` —— 1/5 个有
- `GIMMVFI_interpolate` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `ImageCASharpening+` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `PrimitiveString` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `VHS_VideoInfoLoaded` —— 1/5 个有
- `WanVideoTextEncodeCached` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
