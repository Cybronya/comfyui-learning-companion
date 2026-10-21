---
name: unknown_workflow_video_lora_sampler_348
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.611167
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, SetNode, VHS_VideoCombine, WanVideoAddS2VEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1973620998547353601.json, 视频生成/图生视频/1964737438142840834.json, 视频生成/图生视频/1964737369696030722.json, 视频生成/图生视频/1965441374021632001.json, 视频生成/图生视频/1966080494343458817.json, 视频生成/文生视频/1973620998547353601.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_348

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1973620998547353601.json、视频生成/图生视频/1964737438142840834.json、视频生成/图生视频/1964737369696030722.json、视频生成/图生视频/1965441374021632001.json、视频生成/图生视频/1966080494343458817.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoAddS2VEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 5/6 个有
- `DWPreprocessor` —— 5/6 个有
- `GetImageRangeFromBatch` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `PreviewAny` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `RH_Translator` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `RH_Nano_Banana_Image2Image` —— 4/6 个有
- `Label (rgthree)` —— 3/6 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/6 个有
- `GIMMVFI_interpolate` —— 1/6 个有
- `InsertLatentToIndexed` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `RunningHub USO Loader` —— 1/6 个有
- `RunningHub USO Sampler` —— 1/6 个有
- `VHS_SelectEveryNthImage` —— 1/6 个有
- `VHS_SplitImages` —— 1/6 个有
- `WanVideoContextOptions` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
