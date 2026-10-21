---
name: unknown_workflow_video_sampler_vae_180
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.971
common_nodes: [BasicMath, CLIPVisionLoader, DownloadAndLoadWav2VecModel, FloatConstant, INTConstant, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, StringConcatenate, ToFloat, ToInt, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2033528799509352449.json, 视频生成/图生视频/2033775049777352706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_180

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2033528799509352449.json、视频生成/图生视频/2033775049777352706.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicMath`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `FloatConstant`
- `INTConstant`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `StringConcatenate`
- `ToFloat`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
