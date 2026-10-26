---
name: unknown_workflow_video_lora_sampler_766
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.968667
common_nodes: [CreateCFGScheduleFloatList, DownloadAndLoadWav2VecModel, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/音乐数字人（单人唱歌） wan2.2 multiTalk_1957437861178044418.json, 视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json, 视频生成/文生视频/Wan2.2+Multitalk 文生视频_1952158294372765697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_766

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/音乐数字人（单人唱歌） wan2.2 multiTalk_1957437861178044418.json、视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json、视频生成/文生视频/Wan2.2+Multitalk 文生视频_1952158294372765697.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float to Int` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `Int` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `RH_GetAudioDuration` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `WanVideoClipVisionEncode` —— 1/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
