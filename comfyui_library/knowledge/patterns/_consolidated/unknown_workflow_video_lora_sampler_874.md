---
name: unknown_workflow_video_lora_sampler_874
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.755
common_nodes: [AudioCrop, AudioEncoderEncode, AudioEncoderLoader, CR Prompt Text, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageSizeAndCount, InsertLatentToIndexed, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PreviewAny, SaveAudio, VHS_SplitImages, VHS_VideoCombine, WanVideoAddAudioEmbeds, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2008581712120385537.json, 视频生成/图生视频/1961069392614330370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_874

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2008581712120385537.json、视频生成/图生视频/1961069392614330370.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CR Prompt Text`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `InsertLatentToIndexed`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `PreviewAny`
- `SaveAudio`
- `VHS_SplitImages`
- `VHS_VideoCombine`
- `WanVideoAddAudioEmbeds`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `Int` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
