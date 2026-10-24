---
name: unknown_workflow_video_sampler_vae_49
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.779444
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk带动作数字人V2【动态增强版】_1996999462549655554.json, 视频生成/图生视频/InfiniteTalk数字人图生视频-自动对口型（支持唱歌_说话） 浮云12.11 次用_1998779897466249217.json, 视频生成/图生视频/InfiniteTalk数字人图生长视频-自动对口型（支持唱歌_说话）_1993207838587764737.json, 视频生成/图生视频/InfiniteTalk高动态_1985744717117890562.json, 视频生成/图生视频/【AI代码侠土豆】I2V-InfiniteTalk数字人_1964947566926417921.json, 视频生成/图生视频/商用娱乐地表最强数字人（测颜版）_1988227930037903361.json, 视频生成/图生视频/新版极速Infinite Talk图片数字人--自动计算_1988898686707044353.json, 视频生成/图生视频/自动计算帧数！Infinite Talk极速数字人。  基于T8star-Aix版本改造_1984094280551694338.json, 音频生成/音频生成/(歌曲数字人)全流程精准口型高强动作V4_1989287142675369986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_49

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk带动作数字人V2【动态增强版】_1996999462549655554.json、视频生成/图生视频/InfiniteTalk数字人图生视频-自动对口型（支持唱歌_说话） 浮云12.11 次用_1998779897466249217.json、视频生成/图生视频/InfiniteTalk数字人图生长视频-自动对口型（支持唱歌_说话）_1993207838587764737.json、视频生成/图生视频/InfiniteTalk高动态_1985744717117890562.json、视频生成/图生视频/【AI代码侠土豆】I2V-InfiniteTalk数字人_1964947566926417921.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 8/9 个有
- `AudioSeparation` —— 8/9 个有
- `MultiTalkModelLoader` —— 8/9 个有
- `MultiTalkWav2VecEmbeds` —— 8/9 个有
- `SimpleMath+` —— 8/9 个有
- `WanVideoLoraSelect` —— 8/9 个有
- `Int` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `WanVideoModelLoader` —— 7/9 个有
- `PreviewAny` —— 6/9 个有
- `RH_GetAudioDuration` —— 6/9 个有
- `CR Prompt Text` —— 5/9 个有
- `GetImageSizeAndCount` —— 5/9 个有
- `JWInteger` —— 5/9 个有
- `ToInt` —— 5/9 个有
- `Float to Int` —— 3/9 个有
- `JWFloat` —— 3/9 个有
- `RHHiddenNodes` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `SoundFlow_GetLength` —— 2/9 个有
- `Comfly_api_set` —— 1/9 个有
- `Comfly_suno_custom` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `SaveAudio` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `easy clearCacheAll` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
