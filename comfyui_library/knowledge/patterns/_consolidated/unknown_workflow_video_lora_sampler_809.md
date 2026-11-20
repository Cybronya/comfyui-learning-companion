---
name: unknown_workflow_video_lora_sampler_809
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9245
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, Int, JjkText, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RH_GetAudioDuration, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/个人测试_2032111547727745025.json, 视频生成/图生视频/InfiniteTalk单人对口型_1978307219957637121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_809

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/个人测试_2032111547727745025.json、视频生成/图生视频/InfiniteTalk单人对口型_1978307219957637121.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `RH_GetAudioDuration`
- `SimpleMath+`
- `ToInt`
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
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `1hew_TextListToString` —— 1/2 个有
- `AudioSeparation` —— 1/2 个有
- `IndexTTS2Run` —— 1/2 个有
- `LongCatVoiceCloneTTS` —— 1/2 个有
- `NormalizeAudioLoudness` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `Qwen3ASRLoader` —— 1/2 个有
- `Qwen3ASRTranscribe` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `RunningHub SoulX-FlashHead Loader` —— 1/2 个有
- `RunningHub SoulX-FlashHead Sampler` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
