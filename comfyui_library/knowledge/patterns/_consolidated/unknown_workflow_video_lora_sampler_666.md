---
name: unknown_workflow_video_lora_sampler_666
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.928
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/超清数字人对口型音乐_2098282192836317186.json, 视频生成/图生视频/Wan Video InfiniteTalk  双人对话_1988149592183234562.json, 视频生成/图生视频/infinitetalk多段mv生成_1968146725170982914.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_666

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/超清数字人对口型音乐_2098282192836317186.json、视频生成/图生视频/Wan Video InfiniteTalk  双人对话_1988149592183234562.json、视频生成/图生视频/infinitetalk多段mv生成_1968146725170982914.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
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
- `LoadAudio` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `RH_GetAudioDuration` —— 2/3 个有
- `SoundFlow_TrimAudio` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR Float To Integer` —— 1/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `Display Int (rgthree)` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `ImpactFloat` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
