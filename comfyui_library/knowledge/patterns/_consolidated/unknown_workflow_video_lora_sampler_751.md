---
name: unknown_workflow_video_lora_sampler_751
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.944667
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图片对口型工作流_2092091005381206017.json, 视频生成/图生视频/数字人-口播_1901831714153324545.json, 视频生成/文生视频/小赛数字人_1958479331356000258.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_751

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/图片对口型工作流_2092091005381206017.json、视频生成/图生视频/数字人-口播_1901831714153324545.json、视频生成/文生视频/小赛数字人_1958479331356000258.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

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
- `SimpleMath+`
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
- `AudioSeparation` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Audio Duration (mtb)` —— 1/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `Float` —— 1/3 个有
- `Float to Int` —— 1/3 个有
- `ImageResize` —— 1/3 个有
- `RH_GetAudioDuration` —— 1/3 个有
- `SoundFlow_GetLength` —— 1/3 个有
- `SoundFlow_TrimAudio` —— 1/3 个有
- `String Literal` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `ttN int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
