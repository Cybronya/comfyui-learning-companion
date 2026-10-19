---
name: unknown_workflow_video_lora_sampler_639
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.933667
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1951180458820313090.json, 视频生成/图生视频/1956285883156758529.json, 视频生成/图生视频/1957437861178044418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_639

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1951180458820313090.json、视频生成/图生视频/1956285883156758529.json、视频生成/图生视频/1957437861178044418.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 2/3 个有
- `AudioSeparation` —— 2/3 个有
- `CreateCFGScheduleFloatList` —— 2/3 个有
- `FloatConstant` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `WanVideoSetBlockSwap` —— 2/3 个有
- `WanVideoSetLoRAs` —— 2/3 个有
- `WanVideoTextEncode` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `WanVideoApplyNAG` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `WanVideoEnhanceAVideo` —— 1/3 个有
- `WanVideoExperimentalArgs` —— 1/3 个有
- `WanVideoTextEncodeSingle` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
