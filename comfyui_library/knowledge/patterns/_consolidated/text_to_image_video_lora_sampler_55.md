---
name: text_to_image_video_lora_sampler_55
type: Text To Image
frequency: 14
level: strong
coverage: 0.878357
common_nodes: [AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Infinitetalk单人数字人｜无限时长自循环口播_2089424078561177602.json, 视频生成/图生视频/InfiniTetalk情感口播数字人｜超自然对口型口播必备_2111111924355264514.json, 视频生成/图生视频/InfiniTetalk数字人对口型｜情感口播超自然口型同步_2108430225666301953.json, 视频生成/图生视频/InfiniTetalk数字人对话｜wan2.1声音处理真人感_2095972968512966658.json, 视频生成/图生视频/InfiniTetalk超自然对口型，情感口播数字人制作_2110858558400188418.json, 视频生成/图生视频/InfiniTetalk超自然对口型，情感口播数字人制作_2111254679618416641.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播人物特效_2094193709834395649.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播视频生成_2098854674370752513.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播视频生成_2099597317438525442.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播视频生成_2100680027225550850.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播视频生成_2104705468173213698.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播视频生成_2104711738179538945.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型，情感口播数字人制作_2110525729363550210.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型，情感口播数字人制作_2111275845468901377.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_55

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（数字人/数字人/Infinitetalk单人数字人｜无限时长自循环口播_2089424078561177602.json、视频生成/图生视频/InfiniTetalk情感口播数字人｜超自然对口型口播必备_2111111924355264514.json、视频生成/图生视频/InfiniTetalk数字人对口型｜情感口播超自然口型同步_2108430225666301953.json、视频生成/图生视频/InfiniTetalk数字人对话｜wan2.1声音处理真人感_2095972968512966658.json、视频生成/图生视频/InfiniTetalk超自然对口型，情感口播数字人制作_2110858558400188418.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
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

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 13/14 个有
- `GetImageRangeFromBatch` —— 13/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/14 个有
- `MathExpression|pysssss` —— 13/14 个有
- `孤海注释` —— 13/14 个有
- `GetNode` —— 12/14 个有
- `PlaySound|pysssss` —— 12/14 个有
- `SetNode` —— 12/14 个有
- `SaveImage` —— 9/14 个有
- `AudioCombine` —— 1/14 个有
- `EmptyImage` —— 1/14 个有
- `ImageResizeKJv2` —— 1/14 个有
- `ImageScaleToTotalPixels` —— 1/14 个有
- `Int` —— 1/14 个有
- `PreviewAudio` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `Qwen3TTSCustomVoice` —— 1/14 个有
- `RH_GetAudioDuration` —— 1/14 个有
- `SaveAudioAdvanced` —— 1/14 个有
- `SeedVCRun` —— 1/14 个有
- `SeedVR2` —— 1/14 个有
- `SeedVR2BlockSwap` —— 1/14 个有
- `SeedVR2ExtraArgs` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有
- `TDQwen3TTSModelLoader` —— 1/14 个有
- `ToInt` —— 1/14 个有
- `WanVideoTorchCompileSettings` —— 1/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
