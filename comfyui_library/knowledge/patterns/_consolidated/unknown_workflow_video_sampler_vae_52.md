---
name: unknown_workflow_video_sampler_vae_52
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.954556
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1961732854524874753.json, 视频生成/文生视频/1957952304787898369.json, 视频生成/文生视频/1963933041288728578.json, 视频生成/文生视频/InfiniteTalk对口型_2072999601646641152.json, 视频生成/文生视频/infinitetalk图片数字人唱歌不限时长版_2004411444588408834.json, 音频生成/音频生成/InfiniteTalk数字人-唱歌自由_2046674996084346882.json, 音频生成/音频生成/超强视频对口型唱歌数字人_2100410279401181185.json, 音频生成/音频生成/超强视频对口型唱歌数字人_2100497922336055297.json, 音频生成/音频生成/超自然对口型 视频数字人_2000587001097224194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_52

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1961732854524874753.json、视频生成/文生视频/1957952304787898369.json、视频生成/文生视频/1963933041288728578.json、视频生成/文生视频/InfiniteTalk对口型_2072999601646641152.json、视频生成/文生视频/infinitetalk图片数字人唱歌不限时长版_2004411444588408834.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 8/9 个有
- `AudioSeparation` —— 8/9 个有
- `INTConstant` —— 8/9 个有
- `WanVideoLoraSelect` —— 7/9 个有
- `LoadImage` —— 6/9 个有
- `Anything Everywhere` —— 5/9 个有
- `WanVideoTextEncodeCached` —— 5/9 个有
- `GetImageRangeFromBatch` —— 4/9 个有
- `LoadWanVideoT5TextEncoder` —— 4/9 个有
- `WanVideoEncode` —— 4/9 个有
- `WanVideoTextEncode` —— 4/9 个有
- `easy int` —— 4/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `Int` —— 1/9 个有
- `PainterAudioLength` —— 1/9 个有
- `RIFEInterpolation` —— 1/9 个有
- `ShowAnything|Mie` —— 1/9 个有
- `ToFloat` —— 1/9 个有
- `ToInt` —— 1/9 个有
- `easy mathInt` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
