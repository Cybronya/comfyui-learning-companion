---
name: unknown_workflow_video_sampler_vae_77
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.904286
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图片对口型_2044939873613783041.json, 视频生成/图生视频/多人对口型 图生视频 数字人 InfiniteTalk 音频驱动 动作模仿_2044647085147951105.json, 视频生成/图生视频/多人对口型 图生视频 数字人 InfiniteTalk 音频驱动 动作模仿_2073622937676115969.json, 视频生成/图生视频/多角色数字人 InfiniteTalk 多人对口型 说话对话唱歌_2029363209500626945.json, 视频生成/图生视频/数字人-InfiniteTalk-多人对口型工作流_2051497728395489282.json, 视频生成/文生视频/图生视频 数字人 InfiniteTalk 多人对口型 动作模仿_2044640516272295938.json, 视频生成/文生视频/数字人口播_2106320471296925698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_77

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/图片对口型_2044939873613783041.json、视频生成/图生视频/多人对口型 图生视频 数字人 InfiniteTalk 音频驱动 动作模仿_2044647085147951105.json、视频生成/图生视频/多人对口型 图生视频 数字人 InfiniteTalk 音频驱动 动作模仿_2073622937676115969.json、视频生成/图生视频/多角色数字人 InfiniteTalk 多人对口型 说话对话唱歌_2029363209500626945.json、视频生成/图生视频/数字人-InfiniteTalk-多人对口型工作流_2051497728395489282.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `WanVideoLoraSelectMulti` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `LayerMask: MaskPreview` —— 5/7 个有
- `SeparateMasks` —— 5/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `easy int` —— 2/7 个有
- `Audio Duration (mtb)` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `IndexTTS2Run` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `WanVideoLoraSelect` —— 1/7 个有
- `WanVideoSetBlockSwap` —— 1/7 个有
- `WanVideoSetLoRAs` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
