---
name: unknown_workflow_video_lora_sampler_73
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.918143
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, FantasyPortraitFaceDetector, FantasyPortraitModelLoader, ImageConcatMulti, ImageResizeKJv2, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, SoundFlow_Fade, SoundFlow_GetLength, ToInt, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAddFantasyPortrait, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/AI万相表情迁移Aniwan2.1+FantasyPortrait_2019581673943339010.json, 平台全量/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2079560731955130369.json, 平台全量/工作流视频篇5-AI短剧表情迁移万相-面部表情迁移_2018227188155289601.json, 平台全量/表情迁移-无声版（FantasyPortrait）_1956565544726134786.json, 平台全量/表情迁移-有声版（FantasyPortrait+multitalk））_1956966083056865282.json, 视频生成/图生视频/AI 短剧 表情迁移万相Aniwan2.1 FantasyPortrait InfiniteTalk_2009933373376040962.json, 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_1957074909769949186.json, 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2012855338562752513.json, 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2013833454928007170.json, 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2017131239425183745.json, 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2047205643727147009.json, 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2051915621100732418.json, 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2056919279173455873.json, 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2066892858690461697.json, 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2100890914960007169.json, 视频生成/图生视频/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2100931090323169281.json, 视频生成/图生视频/Aiwood-FantasyPortrait+Multitalk_1956039334631755778.json, 视频生成/图生视频/MultiTalk+AniWan+FantasyPortrait高动态表情追踪对口型数字人V1_1956275503990755329.json, 视频生成/图生视频/人物表情迁移数字人FantasyPortraitk_1957739014727237633.json, 视频生成/图生视频/表情迁移Aniwan2.1+FantasyPortrait+InfiniteTalk_2011700732822560770.json, 视频生成/图生视频/🥱表情复刻+对口型工作流【FantasyPortrait+Multitalk】🥱_1956623622469287937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_73

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（平台全量/AI万相表情迁移Aniwan2.1+FantasyPortrait_2019581673943339010.json、平台全量/AI短剧表情迁移万相Aniwan2.1+FantasyPortrait+InfiniteTalk_2079560731955130369.json、平台全量/工作流视频篇5-AI短剧表情迁移万相-面部表情迁移_2018227188155289601.json、平台全量/表情迁移-无声版（FantasyPortrait）_1956565544726134786.json、平台全量/表情迁移-有声版（FantasyPortrait+multitalk））_1956966083056865282.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `FantasyPortraitFaceDetector`
- `FantasyPortraitModelLoader`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `SoundFlow_Fade`
- `SoundFlow_GetLength`
- `ToInt`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAddFantasyPortrait`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 20/21 个有
- `JWInteger` —— 18/21 个有
- `Fast Groups Bypasser (rgthree)` —— 17/21 个有
- `GetNode` —— 6/21 个有
- `SetNode` —— 5/21 个有
- `INTConstant` —— 3/21 个有
- `PrimitiveStringMultiline` —— 2/21 个有
- `AudioSeparation` —— 1/21 个有
- `CM_IntBinaryOperation` —— 1/21 个有
- `CM_IntToFloat` —— 1/21 个有
- `CR Text` —— 1/21 个有
- `ImpactInt` —— 1/21 个有
- `Note Plus (mtb)` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
