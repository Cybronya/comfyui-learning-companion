---
name: unknown_workflow_video_lora_sampler_389
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.721833
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, DWPreprocessor, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddS2VEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/04-06-02-WAN2.2-数字人-S2V-姿势控制数字人-kijai_1990969037591093249.json, 数字人/数字人/s2v姿势控制数字人视频生成_1963631931462225922.json, 视频生成/图生视频/Wan2.2 S2V+FramePack姿态控制数字人_2073345449498603522.json, 视频生成/图生视频/（KJ版）Wan2.2 S2V+FramePack全身姿态控制数字人V2_1962399732356222977.json, 视频生成/图生视频/（KJ版）Wan2.2 S2V全身姿势控制数字人V1_1962399741415919617.json, 视频生成/图生视频/（KJ版）Wan2.2 S2V头部姿势控制数字人V2_1962391778080985089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_389

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/04-06-02-WAN2.2-数字人-S2V-姿势控制数字人-kijai_1990969037591093249.json、数字人/数字人/s2v姿势控制数字人视频生成_1963631931462225922.json、视频生成/图生视频/Wan2.2 S2V+FramePack姿态控制数字人_2073345449498603522.json、视频生成/图生视频/（KJ版）Wan2.2 S2V+FramePack全身姿态控制数字人V2_1962399732356222977.json、视频生成/图生视频/（KJ版）Wan2.2 S2V全身姿势控制数字人V1_1962399741415919617.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddS2VEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 5/6 个有
- `ColorMatch` —— 5/6 个有
- `GetImageRangeFromBatch` —— 5/6 个有
- `PreviewAny` —— 5/6 个有
- `WanVideoLoraSelectMulti` —— 5/6 个有
- `easy anythingIndexSwitch` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `JWInteger` —— 4/6 个有
- `WanVideoContextOptions` —— 4/6 个有
- `WanVideoTextEncodeCached` —— 4/6 个有
- `GetImageSizeAndCount` —— 3/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `LoadWanVideoT5TextEncoder` —— 2/6 个有
- `WanVideoTextEncode` —— 2/6 个有
- `ACE_AudioCrop` —— 1/6 个有
- `Anything Everywhere` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `JWString` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `WanVideoLoraSelect` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
