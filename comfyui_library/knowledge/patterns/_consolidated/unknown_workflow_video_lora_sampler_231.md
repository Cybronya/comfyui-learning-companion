---
name: unknown_workflow_video_lora_sampler_231
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.934444
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1968700475308691457.json, 视频生成/图生视频/1983881923028287489.json, 视频生成/图生视频/1985498577474625538.json, 视频生成/图生视频/2033715529726300161.json, 视频生成/图生视频/2034066519231041538.json, 视频生成/图生视频/2077567710116012034.json, 视频生成/图生视频/图生视频-infinitetalk单人_2084526458785058817.json, 视频生成/图生视频/1901831714153324545.json, 视频生成/图生视频/1966325384155475970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_231

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1968700475308691457.json、视频生成/图生视频/1983881923028287489.json、视频生成/图生视频/1985498577474625538.json、视频生成/图生视频/2033715529726300161.json、视频生成/图生视频/2034066519231041538.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 8/9 个有
- `LoadAudio` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 8/9 个有
- `AudioCrop` —— 7/9 个有
- `RH_GetAudioDuration` —— 7/9 个有
- `ToInt` —— 7/9 个有
- `easy showAnything` —— 7/9 个有
- `CR Text` —— 2/9 个有
- `easy anythingIndexSwitch` —— 2/9 个有
- `Audio Duration (mtb)` —— 1/9 个有
- `FlashVSRNode` —— 1/9 个有
- `Float to Int` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `IndexTTS2_Emotion` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `Sleep` —— 1/9 个有
- `TrimAudioDuration` —— 1/9 个有
- `VHS_LoadAudioUpload` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
