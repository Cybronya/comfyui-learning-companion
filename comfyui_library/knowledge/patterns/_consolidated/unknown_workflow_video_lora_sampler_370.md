---
name: unknown_workflow_video_lora_sampler_370
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.794875
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [数字人/数字人/Infinitetalk_2099404964316663810.json, 数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_1961018358189723649.json, 数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_1972208046057385986.json, 数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_2011358802314010626.json, 数字人/数字人/Infinitetalk数字人_2006979668984991746.json, 数字人/数字人/zy_2014586051662192641.json, 数字人/数字人/视频对口型 1_2080489097541537793.json, 视频生成/图生视频/Infinitetalk数字人_1989166244014198786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_370

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Infinitetalk_2099404964316663810.json、数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_1961018358189723649.json、数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_1972208046057385986.json、数字人/数字人/Infinitetalk_视频对口型-完美复刻动作，保持原视频动作一致_2011358802314010626.json、数字人/数字人/Infinitetalk数字人_2006979668984991746.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `SaveAudio` —— 5/8 个有
- `SimpleMath+` —— 5/8 个有
- `ToInt` —— 5/8 个有
- `WanVideoTorchCompileSettings` —— 5/8 个有
- `Display Int (rgthree)` —— 3/8 个有
- `Int` —— 3/8 个有
- `SoundFlow_GetLength` —— 3/8 个有
- `INTConstant` —— 2/8 个有
- `ImageBatchMulti` —— 2/8 个有
- `ImageUpscaleWithModel` —— 2/8 个有
- `ImpactInt` —— 2/8 个有
- `LoadImage` —— 2/8 个有
- `LoadWanVideoT5TextEncoder` —— 2/8 个有
- `PreviewAny` —— 2/8 个有
- `ReverseImageBatch` —— 2/8 个有
- `Upscale Model Loader` —— 2/8 个有
- `WanVideoTextEncode` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `AudioCombine` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/8 个有
- `FlashVSRNode` —— 1/8 个有
- `GIMMVFI_interpolate` —— 1/8 个有
- `GetAudioDurationFromAudio` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `easy mathInt` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
