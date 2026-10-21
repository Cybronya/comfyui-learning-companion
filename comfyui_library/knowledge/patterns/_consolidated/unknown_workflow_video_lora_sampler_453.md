---
name: unknown_workflow_video_lora_sampler_453
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9216
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [Audio Duration (mtb), SimpleMath+, String Literal, ttN int]
members: [视频生成/图生视频/图片对口型工作流_2092091005381206017.json, 视频生成/图生视频/2005465061298761730.json, 视频生成/图生视频/2015414691312443393.json, 视频生成/文生视频/1957952304787898369.json, 视频生成/文生视频/1958479331356000258.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_453

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/图片对口型工作流_2092091005381206017.json、视频生成/图生视频/2005465061298761730.json、视频生成/图生视频/2015414691312443393.json、视频生成/文生视频/1957952304787898369.json、视频生成/文生视频/1958479331356000258.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
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
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 4/5 个有
- `AudioCrop` —— 3/5 个有
- `INTConstant` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `Audio Duration (mtb)` —— 1/5 个有
- `CM_FloatToInt` —— 1/5 个有
- `Float` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageResize` —— 1/5 个有
- `SoundFlow_GetLength` —— 1/5 个有
- `SoundFlow_TrimAudio` —— 1/5 个有
- `String Literal` —— 1/5 个有
- `Text` —— 1/5 个有
- `ttN int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Audio Duration (mtb)、SimpleMath+、String Literal、ttN int
