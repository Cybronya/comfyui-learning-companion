---
name: text_to_image_video_lora_sampler_151
type: Text To Image
frequency: 5
level: weak
coverage: 0.5144
common_nodes: [AnyBooleanSwitch, AudioConcat, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfySwitchNode, EmptyLatentImage, FloatInput, GetImageSize, GetNode, INTConstant, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, ImageScaleToTotalPixels, Int, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, Primitive integer [Crystools], PrimitiveBoolean, RH_RhartImageG2ImageToImage, SAM3_VideoTrack, SCAIL2ColoredMaskV2, SeedVR2, SetNode, SimpleMath+, TextEncodeQwenImageEditPlus, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus TorchCompileSettings, WanAnimatePlus VAELoader, WanVideoLoraSelectMulti, WanVideoTeaCache, easy cleanGpuUsed, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/SCAIL2 v3一键换装跳舞 胸部抖动细节可自由调节_2095064894033977346.json, 平台全量/SCAIL2 v3一键换装跳舞 胸部抖动细节可自由调节_2097460910775422978.json, 平台全量/SCAIL2 v3一键换装跳舞 胸部抖动细节可自由调节_2099272913731014658.json, 平台全量/SCAIL2 v3一键换装跳舞 胸部抖动细节可自由调节_2101084616722575361.json, 平台全量/动作迁移_一键换装跳舞视频_SCAIL2_v3_胸部抖动可控_2075965524944703489.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_151

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/SCAIL2 v3一键换装跳舞 胸部抖动细节可自由调节_2095064894033977346.json、平台全量/SCAIL2 v3一键换装跳舞 胸部抖动细节可自由调节_2097460910775422978.json、平台全量/SCAIL2 v3一键换装跳舞 胸部抖动细节可自由调节_2099272913731014658.json、平台全量/SCAIL2 v3一键换装跳舞 胸部抖动细节可自由调节_2101084616722575361.json、平台全量/动作迁移_一键换装跳舞视频_SCAIL2_v3_胸部抖动可控_2075965524944703489.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 5 个 workflow 都包含：
- `AnyBooleanSwitch`
- `AudioConcat`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `FloatInput`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `Int`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `PrimitiveBoolean`
- `RH_RhartImageG2ImageToImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `SeedVR2`
- `SetNode`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlus`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus TorchCompileSettings`
- `WanAnimatePlus VAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoTeaCache`
- `easy cleanGpuUsed`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `solarL_SaveImagesToZip` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 720 | 5 | 0% |
| 高度 | 80 | 80 - 1280 | 5 | 0% |
| 采样步数 | 4 | 4 - 8 | 5 | 67% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 5 | 63% |
| 采样算法 | er_sde | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 720，5 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1280，5 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，5 个样本
- 采样算法 最常用 er_sde，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（14/5 个样本）：Steps较低可能导致细节不足
