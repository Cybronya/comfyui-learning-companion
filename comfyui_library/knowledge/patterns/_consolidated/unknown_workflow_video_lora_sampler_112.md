---
name: unknown_workflow_video_lora_sampler_112
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.7965
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/InfiniteTalk数字人动态加强版（对口型-唱歌）_1986084370261954561.json, 图片生成/图生图/InfiniteTalk数字人高动态（对口型-唱歌）_1986988244921421826.json, 图片生成/图生图/wanvideo_infinitetalk_单人工作流_1977379439782830082.json, 图片生成/图生图/数字人  对口型  图生视频_2062824879812071426.json, 图片生成/文生图/对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2112074166999539713.json, 平台全量/1.2_InfiniteTalk视频+音频对口型（效果好Z）_1958562037829890050.json, 平台全量/1.2_InfiniteTalk视频+音频对口型（效果好）_1963900839138136066.json, 平台全量/InfiniTetalk 超自然数字人对口型  情感口播  数字人 图生视频_2118657483341393922.json, 平台全量/InfiniTetalk 超自然数字人对口型  情感口播  数字人 图生视频_2118662460235403265.json, 平台全量/InfiniteTalk超自然数字人对口型单人最新版 企财盈5.13_2054124499871772674.json, 平台全量/InfiniteTalk超自然数字人对口型单人最新版 企财盈7.10_2075504787818369026.json, 数字人/数字人/1.1_infinitetalk视频双人对口型（效果最好）_1994720356055326722.json, 数字人/数字人/infinitetalk视频双人对口型_1980526429727313921.json, 数字人/数字人/infinitetalk视频对口型（hua）_1998027187120955394.json, 数字人/数字人/infinitetalk视频对口型（hua）_2006207828683395074.json, 视频生成/图生视频/InfiniteTalk图像双人对口型_1971843495331819522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/InfiniteTalk数字人动态加强版（对口型-唱歌）_1986084370261954561.json、图片生成/图生图/InfiniteTalk数字人高动态（对口型-唱歌）_1986988244921421826.json、图片生成/图生图/wanvideo_infinitetalk_单人工作流_1977379439782830082.json、图片生成/图生图/数字人  对口型  图生视频_2062824879812071426.json、图片生成/文生图/对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2112074166999539713.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 16 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 15/16 个有
- `AudioCrop` —— 13/16 个有
- `GetImageRangeFromBatch` —— 13/16 个有
- `VHS_LoadVideo` —— 10/16 个有
- `CR Text` —— 9/16 个有
- `ImageFromBatch+` —— 9/16 个有
- `LoadWanVideoT5TextEncoder` —— 9/16 个有
- `PrimitiveInt` —— 9/16 个有
- `SimpleMath+` —— 9/16 个有
- `WanVideoEncode` —— 9/16 个有
- `WanVideoTextEncode` —— 9/16 个有
- `WanVideoTorchCompileSettings` —— 9/16 个有
- `easy showAnything` —— 9/16 个有
- `GetNode` —— 8/16 个有
- `SetNode` —— 8/16 个有
- `GetImageSizeAndCount` —— 7/16 个有
- `LoadImage` —— 7/16 个有
- `PreviewAudio` —— 7/16 个有
- `WanVideoTextEncodeCached` —— 7/16 个有
- `ImageResizeKJv2` —— 6/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/16 个有
- `MathExpression|pysssss` —— 6/16 个有
- `PlaySound|pysssss` —— 6/16 个有
- `VHS_VideoInfo` —— 6/16 个有
- `PreviewImage` —— 4/16 个有
- `VHS_VideoInfoLoaded` —— 4/16 个有
- `ImageResize+` —— 3/16 个有
- `easy cleanGpuUsed` —— 3/16 个有
- `Anything Everywhere` —— 2/16 个有
- `GetAudioDurationFromAudio` —— 2/16 个有
- `SaveImage` —— 2/16 个有
- `easy int` —— 2/16 个有
- `INTConstant` —— 1/16 个有
- `JWFloat` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
