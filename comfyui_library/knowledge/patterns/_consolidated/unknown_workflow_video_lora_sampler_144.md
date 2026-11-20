---
name: unknown_workflow_video_lora_sampler_144
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.708385
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, Int, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AI女友对口型V2=图片说话唱歌+动作=InfiniTetalk=B站艾橘溪_1960951492805103618.json, 视频生成/图生视频/AI女友对口型V2=图片说话唱歌+动作_2065438787911639042.json, 视频生成/图生视频/AI女友对口型_1989024069318217729.json, 视频生成/图生视频/AI数字人对口型 角色 图片 说话唱歌 克隆动作 InfiniTetalk   内附音频生成_2006172526635917314.json, 视频生成/图生视频/Infinite Talk 人物对口型V2+图片说话唱歌+动作_2005908579766988801.json, 视频生成/图生视频/InfiniteTalk图生长视频超自然-AI漫剧口播对口型（唱歌_说话）_2015607180996644865.json, 视频生成/图生视频/InfiniteTalk数字人图生长视频-自动对口型（支持唱歌_说话）_1993207838587764737.json, 视频生成/图生视频/Infinitetalk_图片对口型_2046155816666927106.json, 视频生成/图生视频/Wanvideo_infinitetalk_图片对口型_单人工作流_1980220668019171330.json, 视频生成/图生视频/【AI代码侠土豆】I2V-InfiniteTalk数字人_1964947566926417921.json, 视频生成/图生视频/图片对口型音乐人_1995653735567261698.json, 视频生成/图生视频/图片对口型音乐人（去除背景音乐）_1983895730928713729.json, 视频生成/图生视频/数字人对口型，照片说话 （Infinitetalk+Wan2.1加速版）_1966856780053614593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_144

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/AI女友对口型V2=图片说话唱歌+动作=InfiniTetalk=B站艾橘溪_1960951492805103618.json、视频生成/图生视频/AI女友对口型V2=图片说话唱歌+动作_2065438787911639042.json、视频生成/图生视频/AI女友对口型_1989024069318217729.json、视频生成/图生视频/AI数字人对口型 角色 图片 说话唱歌 克隆动作 InfiniTetalk   内附音频生成_2006172526635917314.json、视频生成/图生视频/Infinite Talk 人物对口型V2+图片说话唱歌+动作_2005908579766988801.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 13 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `Int`
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
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 12/13 个有
- `SimpleMath+` —— 11/13 个有
- `GetNode` —— 10/13 个有
- `SetNode` —— 10/13 个有
- `PrimitiveString` —— 6/13 个有
- `GetImageSizeAndCount` —— 5/13 个有
- `LayerUtility: PurgeVRAM` —— 5/13 个有
- `Text Multiline` —— 5/13 个有
- `easy cleanGpuUsed` —— 5/13 个有
- `PreviewImage` —— 4/13 个有
- `RH_GetAudioDuration` —— 4/13 个有
- `Anything Everywhere` —— 3/13 个有
- `Float to Int` —— 3/13 个有
- `INTConstant` —— 3/13 个有
- `SaveAudio` —— 3/13 个有
- `ToInt` —— 3/13 个有
- `easy showAnything` —— 3/13 个有
- `ImageConcatMulti` —— 2/13 个有
- `SoundFlow_GetLength` —— 2/13 个有
- `CM_IntToFloat` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `easy int` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
