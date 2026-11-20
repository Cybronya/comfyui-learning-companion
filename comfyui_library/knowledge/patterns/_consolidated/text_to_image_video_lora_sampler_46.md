---
name: text_to_image_video_lora_sampler_46
type: Text To Image
frequency: 15
level: strong
coverage: 0.861467
common_nodes: [AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, GetNode, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/InfiniTetalk超自然数字人对口型，情感口播视频自然逼真_2114505956007698433.json, 图片生成/图生图/视频对口型InfiniteTalk数字人｜经典本角色一致性超稳_2100774100947001345.json, 图片生成/图生图/超自然数字人对口型方案，情感口播图生图制作_2110875851725295617.json, 数字人/数字人/InfiniTetalk 对口型情感口播｜数字人说话自然流畅_2112417565694844929.json, 数字人/数字人/InfiniTetalk 超自然数字人对口型｜情感口播更传神_2112409370490400770.json, 数字人/数字人/InfiniTetalk数字人对口型｜情感口播视频自然同步口型_2113584045643878401.json, 数字人/数字人/InfiniTetalk超自然对口型，情感口播数字人制作_2111933509655941122.json, 数字人/数字人/InfiniTetalk超自然数字人对口型 情感口播人物特效工具_2113065058187169793.json, 数字人/数字人/InfiniTetalk超自然数字人对口型，情感口播图生视频自然神态_2112703278562766850.json, 数字人/数字人/InfiniTetalk超自然数字人对口型｜情感口播 人物类特效数字人_2104076796160466946.json, 数字人/数字人/InfiniTetalk超自然数字人对口型｜情感口播口型同步生成_2113546408635748354.json, 数字人/数字人/InfiniteTalk单人对口型数字人 音频驱动口型同步_2099225085285593089.json, 视频生成/图生视频/InfiniTetalk情感口播对口型，数字人图生视频制作_2110880440189014018.json, 视频生成/图生视频/InfiniTetalk配口型｜Wan2.1图像数字人KJ节点版_2094339522954874882.json, 视频生成/图生视频/InfiniTetalk音频驱动数字人｜电商带货图生视频_2096311256083951618.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/InfiniTetalk超自然数字人对口型，情感口播视频自然逼真_2114505956007698433.json、图片生成/图生图/视频对口型InfiniteTalk数字人｜经典本角色一致性超稳_2100774100947001345.json、图片生成/图生图/超自然数字人对口型方案，情感口播图生图制作_2110875851725295617.json、数字人/数字人/InfiniTetalk 对口型情感口播｜数字人说话自然流畅_2112417565694844929.json、数字人/数字人/InfiniTetalk 超自然数字人对口型｜情感口播更传神_2112409370490400770.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 15 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
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
- `Audio Duration (mtb)` —— 14/15 个有
- `GetImageRangeFromBatch` —— 14/15 个有
- `LoadWanVideoT5TextEncoder` —— 14/15 个有
- `PlaySound|pysssss` —— 14/15 个有
- `WanVideoTextEncode` —— 14/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/15 个有
- `LoadImage` —— 13/15 个有
- `MathExpression|pysssss` —— 13/15 个有
- `SaveImage` —— 7/15 个有
- `WanVideoTorchCompileSettings` —— 3/15 个有
- `Anything Everywhere` —— 2/15 个有
- `ImageResizeKJv2` —— 2/15 个有
- `PreviewAny` —— 2/15 个有
- `PreviewAudio` —— 2/15 个有
- `VHS_LoadVideo` —— 2/15 个有
- `WanVideoEncode` —— 2/15 个有
- `easy int` —— 2/15 个有
- `easy showAnything` —— 2/15 个有
- `ColorCorrectOfUtils` —— 1/15 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/15 个有
- `FlashVSRNode` —— 1/15 个有
- `GIMMVFI_interpolate` —— 1/15 个有
- `GetImageSizeAndCount` —— 1/15 个有
- `INTConstant` —— 1/15 个有
- `ImageCASharpening+` —— 1/15 个有
- `ImageFromBatch+` —— 1/15 个有
- `LayerUtility: PurgeVRAM` —— 1/15 个有
- `PixaromaResolution` —— 1/15 个有
- `PrimitiveInt` —— 1/15 个有
- `PrimitiveString` —— 1/15 个有
- `SimpleMath+` —— 1/15 个有
- `VHS_VideoInfoLoaded` —— 1/15 个有
- `WanVideoTextEncodeCached` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
