---
name: unknown_workflow_video_sampler_4
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8807
common_nodes: [AudioSeparation, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MultiTalkWav2VecEmbeds, RHHiddenNodes, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoTextEncode]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk带动作数字人V2【动态增强版】_1981283367738138625.json, 视频生成/图生视频/Vox Infinity 任意IP唱歌【动态稳定版】_1988524870826901505.json, 视频生成/图生视频/WanVideo-唱歌数字人-02_1992836871027838977.json, 视频生成/图生视频/WanVideo-唱歌数字人_1990968064927801345.json, 视频生成/图生视频/【动态控制版】数字人_1991042926883053570.json, 视频生成/图生视频/【大炮】InfiniteTalk音乐数字人_1990657012549771265.json, 视频生成/图生视频/数字人对口型    动态一致_2003004392984965122.json, 视频生成/图生视频/数字人对口型+动态一致_2015428221566717953.json, 视频生成/图生视频/自带运镜！演唱会数字人V1.0【口型完美+自动运镜】_1984278301894131714.json, 音频生成/音频生成/MV音乐赛道专用，商用级_2046698333896445954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_4

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk带动作数字人V2【动态增强版】_1981283367738138625.json、视频生成/图生视频/Vox Infinity 任意IP唱歌【动态稳定版】_1988524870826901505.json、视频生成/图生视频/WanVideo-唱歌数字人-02_1992836871027838977.json、视频生成/图生视频/WanVideo-唱歌数字人_1990968064927801345.json、视频生成/图生视频/【动态控制版】数字人_1991042926883053570.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioSeparation`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkWav2VecEmbeds`
- `RHHiddenNodes`
- `SimpleMath+`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler`
- `WanVideoTextEncode`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 9/10 个有
- `RH_GetAudioDuration` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `CLIPVisionLoader` —— 5/10 个有
- `CreateVideo` —— 5/10 个有
- `DownloadAndLoadWav2VecModel` —— 5/10 个有
- `LoadWanVideoT5TextEncoder` —— 5/10 个有
- `PreViewVideo` —— 5/10 个有
- `WanVideoBlockSwap` —— 5/10 个有
- `WanVideoVAELoader` —— 5/10 个有
- `ToFloat` —— 3/10 个有
- `JWFloat` —— 2/10 个有
- `GetAudioDurationFromAudio` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `SetNode` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
