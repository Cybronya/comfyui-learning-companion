---
name: unknown_workflow_video_lora_sampler_676
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.810667
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: [Audio Duration (mtb), SimpleMath+, String Literal, ttN int]
members: [视频生成/图生视频/图片对口型工作流_2092091005381206017.json, 视频生成/文生视频/1958479331356000258.json, 音频生成/音频生成/文字转语音_1983514355780263937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_676

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/图片对口型工作流_2092091005381206017.json、视频生成/文生视频/1958479331356000258.json、音频生成/音频生成/文字转语音_1983514355780263937.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 2/3 个有
- `AudioSeparation` —— 2/3 个有
- `String Literal` —— 2/3 个有
- `ttN int` —— 2/3 个有
- `Audio Cut (mtb)` —— 1/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Input Switch` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `Float` —— 1/3 个有
- `ImageResize` —— 1/3 个有
- `IndexTTS2Run` —— 1/3 个有
- `IndexTTSRun` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `Reroute (rgthree)` —— 1/3 个有
- `SaveAudio` —— 1/3 个有
- `SoundFlow_GetLength` —— 1/3 个有
- `SoundFlow_TrimAudio` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Audio Duration (mtb)、SimpleMath+、String Literal、ttN int
