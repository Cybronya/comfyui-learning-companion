---
name: text_to_image_video_lora_sampler_101
type: Text To Image
frequency: 7
level: strong
coverage: 0.863857
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, GetImageRangeFromBatch, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/InfiniTetalk超自然数字人对口型｜情感口播 人物类特效数字人_2104076796160466946.json, 数字人/数字人/InfiniteTalk单人对口型数字人 音频驱动口型同步_2099225085285593089.json, 视频生成/图生视频/InfiniTetalk情感口播对口型，数字人图生视频制作_2110880440189014018.json, 视频生成/图生视频/InfiniTetalk情感口播数字人｜超自然对口型口播必备_2111111924355264514.json, 视频生成/图生视频/InfiniTetalk数字人对口型｜情感口播超自然口型同步_2108430225666301953.json, 视频生成/图生视频/InfiniTetalk数字人对话｜wan2.1声音处理真人感_2095972968512966658.json, 视频生成/图生视频/InfiniTetalk音频驱动数字人｜电商带货图生视频_2096311256083951618.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_101

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/InfiniTetalk超自然数字人对口型｜情感口播 人物类特效数字人_2104076796160466946.json、数字人/数字人/InfiniteTalk单人对口型数字人 音频驱动口型同步_2099225085285593089.json、视频生成/图生视频/InfiniTetalk情感口播对口型，数字人图生视频制作_2110880440189014018.json、视频生成/图生视频/InfiniTetalk情感口播数字人｜超自然对口型口播必备_2111111924355264514.json、视频生成/图生视频/InfiniTetalk数字人对口型｜情感口播超自然口型同步_2108430225666301953.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
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
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `PlaySound|pysssss` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `PreviewAudio` —— 3/7 个有
- `Anything Everywhere` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `WanVideoTorchCompileSettings` —— 2/7 个有
- `easy int` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `AudioCombine` —— 1/7 个有
- `ColorCorrectOfUtils` —— 1/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/7 个有
- `FlashVSRNode` —— 1/7 个有
- `GIMMVFI_interpolate` —— 1/7 个有
- `ImageCASharpening+` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `Qwen3TTSCustomVoice` —— 1/7 个有
- `SaveAudioAdvanced` —— 1/7 个有
- `SeedVCRun` —— 1/7 个有
- `SeedVR2` —— 1/7 个有
- `SeedVR2BlockSwap` —— 1/7 个有
- `SeedVR2ExtraArgs` —— 1/7 个有
- `TDQwen3TTSModelLoader` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有
- `WanVideoEncode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
