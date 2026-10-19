---
name: unknown_workflow_video_sampler_3
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9166
common_nodes: [AudioCrop, AudioSeparation, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MultiTalkWav2VecEmbeds, RHHiddenNodes, RH_GetAudioDuration, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoTextEncode]
problems: []
missing: []
members: [视频生成/图生视频/1983542488248033281.json, 视频生成/图生视频/1981283367738138625.json, 视频生成/图生视频/1996999462549655554.json, 视频生成/图生视频/1988524870826901505.json, 视频生成/图生视频/1992836871027838977.json, 视频生成/图生视频/1990968064927801345.json, 视频生成/图生视频/1991042926883053570.json, 视频生成/图生视频/2003004392984965122.json, 视频生成/图生视频/数字人对口型+动态一致_2015428221566717953.json, 音频生成/音频生成/MV音乐赛道专用，商用级_2046698333896445954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_3

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1983542488248033281.json、视频生成/图生视频/1981283367738138625.json、视频生成/图生视频/1996999462549655554.json、视频生成/图生视频/1988524870826901505.json、视频生成/图生视频/1992836871027838977.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkWav2VecEmbeds`
- `RHHiddenNodes`
- `RH_GetAudioDuration`
- `SimpleMath+`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler`
- `WanVideoTextEncode`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 9/10 个有
- `CLIPVisionLoader` —— 6/10 个有
- `CreateVideo` —— 6/10 个有
- `DownloadAndLoadWav2VecModel` —— 6/10 个有
- `LoadWanVideoT5TextEncoder` —— 6/10 个有
- `PreViewVideo` —— 6/10 个有
- `WanVideoBlockSwap` —— 6/10 个有
- `WanVideoVAELoader` —— 6/10 个有
- `JWFloat` —— 4/10 个有
- `ToFloat` —— 3/10 个有
- `PreviewAny` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `easy clearCacheAll` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
