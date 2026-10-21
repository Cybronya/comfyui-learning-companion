---
name: unknown_workflow_video_sampler_vae_64
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.948875
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2065613874346418178.json, 视频生成/文生视频/1963933041288728578.json, 视频生成/文生视频/InfiniteTalk对口型_2072999601646641152.json, 视频生成/文生视频/infinitetalk图片数字人唱歌不限时长版_2004411444588408834.json, 音频生成/音频生成/InfiniteTalk数字人-唱歌自由_2046674996084346882.json, 音频生成/音频生成/超强视频对口型唱歌数字人_2100410279401181185.json, 音频生成/音频生成/超强视频对口型唱歌数字人_2100497922336055297.json, 音频生成/音频生成/超自然对口型 视频数字人_2000587001097224194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_64

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2065613874346418178.json、视频生成/文生视频/1963933041288728578.json、视频生成/文生视频/InfiniteTalk对口型_2072999601646641152.json、视频生成/文生视频/infinitetalk图片数字人唱歌不限时长版_2004411444588408834.json、音频生成/音频生成/InfiniteTalk数字人-唱歌自由_2046674996084346882.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 7/8 个有
- `AudioSeparation` —— 7/8 个有
- `INTConstant` —— 7/8 个有
- `MultiTalkModelLoader` —— 7/8 个有
- `Anything Everywhere` —— 5/8 个有
- `LoadImage` —— 5/8 个有
- `WanVideoLoraSelect` —— 5/8 个有
- `WanVideoTextEncodeCached` —— 5/8 个有
- `GetImageRangeFromBatch` —— 4/8 个有
- `WanVideoEncode` —— 4/8 个有
- `easy int` —— 4/8 个有
- `LoadWanVideoT5TextEncoder` —— 3/8 个有
- `VHS_LoadVideo` —— 3/8 个有
- `WanVideoTextEncode` —— 3/8 个有
- `AudioCropProcessUTK` —— 1/8 个有
- `MelBandRoFormerModelLoader` —— 1/8 个有
- `MelBandRoFormerSampler` —— 1/8 个有
- `PreviewAudio` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
