---
name: unknown_workflow_controlnet_video_lora_33
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.413
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, GetNode, ImageResizeKJv2, Int, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, PreviewAny, PreviewImage, SaveAudio, SetNode, Text, VHS_LoadAudioUpload, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAddS2VEmbeds, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy seed]
problems: []
missing: []
members: [数字人/数字人/图片生成口播视频 可参考动作_2027996577247272961.json, 视频生成/图生视频/🈚️Wan2.2 S2V+u3c运镜+pose 唱歌数字人_动作迁移_对口型_2005645026296295426.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_33

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/图片生成口播视频 可参考动作_2027996577247272961.json、视频生成/图生视频/🈚️Wan2.2 S2V+u3c运镜+pose 唱歌数字人_动作迁移_对口型_2005645026296295426.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：41%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `PreviewAny`
- `PreviewImage`
- `SaveAudio`
- `SetNode`
- `Text`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAddS2VEmbeds`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
