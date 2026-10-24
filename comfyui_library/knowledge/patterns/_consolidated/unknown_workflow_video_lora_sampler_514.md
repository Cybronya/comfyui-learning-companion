---
name: unknown_workflow_video_lora_sampler_514
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.721
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CR Prompt Text, ColorMatch, DWPreprocessor, GetImageRangeFromBatch, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PreviewAny, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddS2VEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy anythingIndexSwitch]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 S2V+FramePack姿态控制数字人_2073345449498603522.json, 视频生成/图生视频/（KJ版）Wan2.2 S2V+FramePack全身姿态控制数字人V2_1962399732356222977.json, 视频生成/图生视频/（KJ版）Wan2.2 S2V全身姿势控制数字人V1_1962399741415919617.json, 视频生成/图生视频/（KJ版）Wan2.2 S2V头部姿势控制数字人V2_1962391778080985089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_514

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 S2V+FramePack姿态控制数字人_2073345449498603522.json、视频生成/图生视频/（KJ版）Wan2.2 S2V+FramePack全身姿态控制数字人V2_1962399732356222977.json、视频生成/图生视频/（KJ版）Wan2.2 S2V全身姿势控制数字人V1_1962399741415919617.json、视频生成/图生视频/（KJ版）Wan2.2 S2V头部姿势控制数字人V2_1962391778080985089.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CR Prompt Text`
- `ColorMatch`
- `DWPreprocessor`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `PreviewAny`
- `VHS_LoadVideo`
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
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 3/4 个有
- `GetImageSizeAndCount` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `WanVideoContextOptions` —— 3/4 个有
- `ACE_AudioCrop` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
