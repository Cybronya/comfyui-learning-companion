---
name: unknown_workflow_video_lora_sampler_372
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.680667
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, ColorMatch, DWPreprocessor, GetImageRangeFromBatch, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PreviewAny, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddS2VEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2073345449498603522.json, 视频生成/图生视频/1962399732356222977.json, 视频生成/图生视频/1962399741415919617.json, 视频生成/图生视频/1962391778080985089.json, 视频生成/文生视频/1962055822404685826.json, 视频生成/文生视频/KJ-Wan2.2-S2v_2072999620546174976.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_372

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2073345449498603522.json、视频生成/图生视频/1962399732356222977.json、视频生成/图生视频/1962399741415919617.json、视频生成/图生视频/1962391778080985089.json、视频生成/文生视频/1962055822404685826.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `ColorMatch`
- `DWPreprocessor`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
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

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 5/6 个有
- `GetNode` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `JWInteger` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `easy anythingIndexSwitch` —— 4/6 个有
- `AudioCrop` —— 3/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `WanVideoContextOptions` —— 3/6 个有
- `INTConstant` —— 2/6 个有
- `MergeAudioMW` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `VHS_LoadAudio` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `ACE_AudioCrop` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
