---
name: unknown_workflow_video_sampler_vae_12
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.898684
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk & LatentSync 对口型工作流 V1.0_2028880263652052993.json, 视频生成/图生视频/InfiniteTalk单人数字人对口型_1998953194820620290.json, 视频生成/图生视频/InfiniteTalk图片对口型工作流_2070420975967100929.json, 视频生成/图生视频/infinitetalk 单人音频驱动 对口型 数字人_2038129720084140034.json, 视频生成/图生视频/infinitetalk 对口型 数字人 单人音频驱动_2039686638024003585.json, 视频生成/图生视频/infinitetalk 音频驱动 对口型 数字人_2038259769424744450.json, 视频生成/图生视频/infinitetalk 音频驱动 对口型 数字人_2043221914818191361.json, 视频生成/图生视频/infinitetalk-workflow_2101559918137536513.json, 视频生成/图生视频/infinitetalk-数字人口播对口型V1_2054541988237717506.json, 视频生成/图生视频/infinitetalk单人-I2V-720p-竖屏_1958721721454981121.json, 视频生成/图生视频/infinitetalk单人-表达式科技AIGC_1993155666919571457.json, 视频生成/图生视频/infinitetalk单人_1957826962256658434.json, 视频生成/图生视频/infinitetalk单人_2044669894783934465.json, 视频生成/图生视频/infinitetalk改进版单人数字人对口型_1999412008917364738.json, 视频生成/图生视频/【CQ808】infinitetalk单人对口型_2054517632375771138.json, 视频生成/图生视频/单人数字人对口型说话工作流（infinitetalk）_2044453798432739329.json, 视频生成/图生视频/图片对口型音乐人_1995653735567261698.json, 视频生成/图生视频/图片对口型音乐人（去除背景音乐）_1983895730928713729.json, 视频生成/图生视频/数字人对口型，照片说话 （Infinitetalk+Wan2.1加速版）_1966856780053614593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_12

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk & LatentSync 对口型工作流 V1.0_2028880263652052993.json、视频生成/图生视频/InfiniteTalk单人数字人对口型_1998953194820620290.json、视频生成/图生视频/InfiniteTalk图片对口型工作流_2070420975967100929.json、视频生成/图生视频/infinitetalk 单人音频驱动 对口型 数字人_2038129720084140034.json、视频生成/图生视频/infinitetalk 对口型 数字人 单人音频驱动_2039686638024003585.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 19 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
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
- `AudioCrop` —— 18/19 个有
- `RH_GetAudioDuration` —— 17/19 个有
- `SimpleMath+` —— 17/19 个有
- `ToInt` —— 17/19 个有
- `easy showAnything` —— 17/19 个有
- `Int` —— 16/19 个有
- `WanVideoLoraSelect` —— 16/19 个有
- `WanVideoTorchCompileSettings` —— 16/19 个有
- `ImageResizeKJv2` —— 15/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/19 个有
- `PreviewImage` —— 5/19 个有
- `GetNode` —— 4/19 个有
- `SetNode` —— 4/19 个有
- `easy cleanGpuUsed` —— 4/19 个有
- `Anything Everywhere` —— 3/19 个有
- `INTConstant` —— 3/19 个有
- `SaveAudio` —— 3/19 个有
- `WanVideoLoraSelectMulti` —— 3/19 个有
- `PreviewAudio` —— 2/19 个有
- `CM_IntToFloat` —— 1/19 个有
- `CR Prompt Text` —— 1/19 个有
- `JWInteger` —— 1/19 个有
- `LatentSyncNode` —— 1/19 个有
- `PrimitiveFloat` —— 1/19 个有
- `Text` —— 1/19 个有
- `VHS_LoadVideo` —— 1/19 个有
- `VideoLengthAdjuster` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
