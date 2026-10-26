---
name: unknown_workflow_video_sampler_vae_126
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.921
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/极速版-数字人_个人IP_2110421173111705601.json, 数字人/数字人/极速版-数字人_个人IP_2114179464493101058.json, 视频生成/图生视频/InfiniteTalk-单人视频转数字人_1991134809961398273.json, 音频生成/音频生成/InfiniteTalk-多人数字人_1991115212053131266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_126

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/极速版-数字人_个人IP_2110421173111705601.json、数字人/数字人/极速版-数字人_个人IP_2114179464493101058.json、视频生成/图生视频/InfiniteTalk-单人视频转数字人_1991134809961398273.json、音频生成/音频生成/InfiniteTalk-多人数字人_1991115212053131266.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `WanVideoEncode` —— 3/4 个有
- `AudioDuration_wan` —— 2/4 个有
- `AudioSeparation` —— 2/4 个有
- `H3ModeSwitch` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `IndexTTS2Run` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PrimitiveString` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `WanVideoLoraSelectMulti` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
