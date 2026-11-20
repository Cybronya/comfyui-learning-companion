---
name: unknown_workflow_video_sampler_vae_25
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.938308
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/数字人-InfiniteTalk-多人对口型工作流_1979435858610786305.json, 数字人/数字人/数字人-InfiniteTalk-视频对口型工作流_1971511965849960450.json, 数字人/数字人/数字人——视频对口型（可带货、MV、短剧）_2046949981302558722.json, 数字人/数字人/数字人直播带货-Infinite Talk2_2008575532488724481.json, 数字人/数字人/数字人直播带货-Infinite Talk_1998597454121590786.json, 数字人/数字人/数字人直播带货-Infinite Talk_2053309414647578626.json, 数字人/数字人/数字人，单人对口型工作流_2050824332179456001.json, 数字人/数字人/最强数字人-多人对口型工作流_1989261379653783553.json, 数字人/数字人/超逼真多人对话数字人-KJ-MultiTalk_1940916699317354497.json, 视频生成/图生视频/InfiniteTalk-wan-双人-index tts_1958085210749415426.json, 视频生成/图生视频/InfiniteTalk图片多人对口型工作流_2070503715320193025.json, 音频生成/音频生成/数字人-InfiniteTalk-视频对口型工作流_2051512102539538434.json, 音频生成/音频生成/视频单人对口型_2029818322556035074.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_25

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（数字人/数字人/数字人-InfiniteTalk-多人对口型工作流_1979435858610786305.json、数字人/数字人/数字人-InfiniteTalk-视频对口型工作流_1971511965849960450.json、数字人/数字人/数字人——视频对口型（可带货、MV、短剧）_2046949981302558722.json、数字人/数字人/数字人直播带货-Infinite Talk2_2008575532488724481.json、数字人/数字人/数字人直播带货-Infinite Talk_1998597454121590786.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 12/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/13 个有
- `WanVideoLoraSelectMulti` —— 11/13 个有
- `LoadImage` —— 10/13 个有
- `PreviewImage` —— 7/13 个有
- `MathExpression|pysssss` —— 5/13 个有
- `SeparateMasks` —— 5/13 个有
- `ImageConcanate` —— 4/13 个有
- `VHS_LoadVideo` —— 4/13 个有
- `WanVideoEncode` —— 4/13 个有
- `easy showAnything` —— 4/13 个有
- `Audio Duration (mtb)` —— 3/13 个有
- `LayerMask: MaskPreview` —— 3/13 个有
- `ImageResizeKJv2` —— 2/13 个有
- `MaskPreview` —— 2/13 个有
- `WanVideoLoraSelect` —— 2/13 个有
- `IndexTTSNode` —— 1/13 个有
- `Primitive integer [Crystools]` —— 1/13 个有
- `StringToInt` —— 1/13 个有
- `Text Multiline` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
