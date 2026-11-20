---
name: unknown_workflow_video_sampler_12
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8958
common_nodes: [AudioCrop, AudioSeparation, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MultiTalkWav2VecEmbeds, RHHiddenNodes, RH_GetAudioDuration, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoTextEncode]
problems: []
missing: []
members: [数字人/数字人/infinitetalk单人版数字人【gen全能视频Si】_2000816671558430722.json, 数字人/数字人/数字人-廖_1994303892110376962.json, 视频生成/图生视频/InfiniteTalk 数字人-对口型_1983542488248033281.json, 视频生成/图生视频/InfiniteTalk带动作数字人V2【动态增强版】_1981283367738138625.json, 视频生成/图生视频/InfiniteTalk带动作数字人V2【动态增强版】_1996999462549655554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_12

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/infinitetalk单人版数字人【gen全能视频Si】_2000816671558430722.json、数字人/数字人/数字人-廖_1994303892110376962.json、视频生成/图生视频/InfiniteTalk 数字人-对口型_1983542488248033281.json、视频生成/图生视频/InfiniteTalk带动作数字人V2【动态增强版】_1981283367738138625.json、视频生成/图生视频/InfiniteTalk带动作数字人V2【动态增强版】_1996999462549655554.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `CLIPVisionLoader` —— 4/5 个有
- `DownloadAndLoadWav2VecModel` —— 4/5 个有
- `LoadAudio` —— 4/5 个有
- `LoadWanVideoT5TextEncoder` —— 4/5 个有
- `WanVideoVAELoader` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `JWFloat` —— 3/5 个有
- `PreViewVideo` —— 3/5 个有
- `WanVideoBlockSwap` —— 2/5 个有
- `Load Image From Url (mtb)` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `ToFloat` —— 1/5 个有
- `VHS_LoadAudio` —— 1/5 个有
- `Wan22PromptSelector` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
