---
name: unknown_workflow_video_lora_sampler_247
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.94325
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/超清数字人对口型音乐_2098282192836317186.json, 视频生成/图生视频/1957828185982599170.json, 视频生成/图生视频/1998698671518666753.json, 视频生成/图生视频/1978645327920173058.json, 视频生成/图生视频/1978307219957637121.json, 视频生成/图生视频/1982650082937978882.json, 视频生成/图生视频/1982712177004027905.json, 视频生成/图生视频/2019287708035719169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_247

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/超清数字人对口型音乐_2098282192836317186.json、视频生成/图生视频/1957828185982599170.json、视频生成/图生视频/1998698671518666753.json、视频生成/图生视频/1978645327920173058.json、视频生成/图生视频/1978307219957637121.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `AudioCrop` —— 6/8 个有
- `Int` —— 6/8 个有
- `LoadAudio` —— 6/8 个有
- `ToInt` —— 6/8 个有
- `Audio Duration (mtb)` —— 3/8 个有
- `RH_GetAudioDuration` —— 3/8 个有
- `PreviewImage` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `AudioCombine` —— 1/8 个有
- `CR Float To Integer` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `ImpactFloat` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `PreviewAudio` —— 1/8 个有
- `Qwen3TTSModelLoader` —— 1/8 个有
- `Qwen3TTSVoiceDesign` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
