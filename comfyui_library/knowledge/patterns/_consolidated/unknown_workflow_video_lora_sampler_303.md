---
name: unknown_workflow_video_lora_sampler_303
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.925857
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2028880263652052993.json, 视频生成/图生视频/1998953194820620290.json, 视频生成/图生视频/2070503715320193025.json, 视频生成/图生视频/1998964761461186561.json, 视频生成/图生视频/2044647085147951105.json, 视频生成/图生视频/2073622937676115969.json, 视频生成/图生视频/2029363209500626945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_303

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2028880263652052993.json、视频生成/图生视频/1998953194820620290.json、视频生成/图生视频/2070503715320193025.json、视频生成/图生视频/1998964761461186561.json、视频生成/图生视频/2044647085147951105.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 6/7 个有
- `LayerMask: MaskPreview` —— 5/7 个有
- `SeparateMasks` —— 5/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `LatentSyncNode` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `RH_GetAudioDuration` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `ToInt` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `VideoLengthAdjuster` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
