---
name: unknown_workflow_video_lora_sampler_163
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.717727
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, ImageResizeKJv2, Int, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AI动物说_2043873863750127617.json, 视频生成/图生视频/AI动物说话=B站艾橘溪_1963961319592480770.json, 视频生成/图生视频/AI女友对口型V2=图片说话唱歌+动作=InfiniTetalk=B站艾橘溪_1960951492805103618.json, 视频生成/图生视频/AI女友对口型V2=图片说话唱歌+动作_2065438787911639042.json, 视频生成/图生视频/AI女友对口型_1989024069318217729.json, 视频生成/图生视频/AI数字人对口型 角色 图片 说话唱歌 克隆动作 InfiniTetalk   内附音频生成_2006172526635917314.json, 视频生成/图生视频/Infinite Talk 人物对口型V2+图片说话唱歌+动作_2005908579766988801.json, 视频生成/图生视频/Infinitetalk_图片对口型_2046155816666927106.json, 视频生成/图生视频/Wanvideo_infinitetalk_图片对口型_单人工作流_1980220668019171330.json, 视频生成/图生视频/最新3.0AI动物说话（懒人版）_2065443186113339394.json, 视频生成/文生视频/AI动物说话=B站艾橘溪_1970041990975025153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_163

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/AI动物说_2043873863750127617.json、视频生成/图生视频/AI动物说话=B站艾橘溪_1963961319592480770.json、视频生成/图生视频/AI女友对口型V2=图片说话唱歌+动作=InfiniTetalk=B站艾橘溪_1960951492805103618.json、视频生成/图生视频/AI女友对口型V2=图片说话唱歌+动作_2065438787911639042.json、视频生成/图生视频/AI女友对口型_1989024069318217729.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 11 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
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
- `GetImageSizeAndCount` —— 9/11 个有
- `LayerUtility: PurgeVRAM` —— 9/11 个有
- `Text Multiline` —— 9/11 个有
- `AudioCrop` —— 6/11 个有
- `PrimitiveString` —— 6/11 个有
- `SimpleMath+` —— 5/11 个有
- `easy cleanGpuUsed` —— 5/11 个有
- `If ANY execute A else B` —— 4/11 个有
- `Int2Any_AS` —— 4/11 个有
- `PrimitiveInt` —— 4/11 个有
- `SaveAudio` —— 4/11 个有
- `SparkTTSClone` —— 4/11 个有
- `ImageConcatMulti` —— 2/11 个有
- `PreviewImage` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
