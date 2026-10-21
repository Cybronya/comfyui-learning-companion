---
name: unknown_workflow_video_lora_sampler_895
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.963
common_nodes: [AudioSeparation, AudioToFPS, CLIPVisionLoader, CM_FloatToInt, CR Prompt Text, DownloadAndLoadWav2VecModel, ImageResizeKJv2, JWInteger, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoCombineEmbeds, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1985521110055796737.json, 视频生成/图生视频/1984092423439712257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_895

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1985521110055796737.json、视频生成/图生视频/1984092423439712257.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioSeparation`
- `AudioToFPS`
- `CLIPVisionLoader`
- `CM_FloatToInt`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoCombineEmbeds`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `DownloadAndLoadSAM2Model` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `DrawViTPose` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `Florence2toCoordinates` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `OnnxDetectionModelLoader` —— 1/2 个有
- `PoseAndFaceDetection` —— 1/2 个有
- `RepeatImageBatch` —— 1/2 个有
- `Sam2Segmentation` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
