---
name: unknown_workflow_video_lora_sampler_167
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.618545
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/SteadyDancer动作迁移视频生视频_1996042760450981890.json, 视频生成/图生视频/SteadyDancer动作迁移视频生视频_2069666439010807809.json, 视频生成/图生视频/SteadyDancer动作迁移高级版_1996065856805355521.json, 视频生成/图生视频/SteadyDancer跳舞动作迁移_2051153118703955970.json, 视频生成/图生视频/SteadyDancer骨骼迁移~不限时长版，绝！_2049307460728524802.json, 视频生成/图生视频/SteadyDancer骨骼迁移~不限时长版，绝！_2049678404324208642.json, 视频生成/图生视频/SteadyDancer（最高质量版-视线完美）所有参数清楚明白_2009099537780056065.json, 视频生成/图生视频/SteadyDance最强人物一致性迁移工作流_1999779350897717249.json, 视频生成/图生视频/WAN SteadyDancer  舞蹈生成 动作姿态迁移 （不限时长版）_2004915777457319937.json, 视频生成/图生视频/Wan+SteadyDancer+卡通姿势复刻_1995897801131409409.json, 视频生成/图生视频/Wan_SteadyDancer_视频动作迁移(单人)_2006239451319635970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_167

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/SteadyDancer动作迁移视频生视频_1996042760450981890.json、视频生成/图生视频/SteadyDancer动作迁移视频生视频_2069666439010807809.json、视频生成/图生视频/SteadyDancer动作迁移高级版_1996065856805355521.json、视频生成/图生视频/SteadyDancer跳舞动作迁移_2051153118703955970.json、视频生成/图生视频/SteadyDancer骨骼迁移~不限时长版，绝！_2049307460728524802.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 10/11 个有
- `WanVideoScheduler` —— 10/11 个有
- `WanVideoSetLoRAs` —— 9/11 个有
- `Int` —— 8/11 个有
- `PoseDetectionOneToAllAnimation` —— 8/11 个有
- `WanVideoBlockSwap` —— 8/11 个有
- `ImageConcatMulti` —— 7/11 个有
- `DrawViTPose` —— 6/11 个有
- `PoseAndFaceDetection` —— 6/11 个有
- `WanVideoSetBlockSwap` —— 6/11 个有
- `PreviewImage` —— 5/11 个有
- `WanVideoTorchCompileSettings` —— 4/11 个有
- `CR Prompt Text` —— 3/11 个有
- `INTConstant` —— 3/11 个有
- `TextInput_` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `LayerUtility: PurgeVRAM V2` —— 2/11 个有
- `SimpleMath+` —— 2/11 个有
- `easy clearCacheAll` —— 2/11 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/11 个有
- `GIMMVFI_interpolate` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `PrimitiveFloat` —— 1/11 个有
- `Text` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `WanVideoLoraSelectMulti` —— 1/11 个有
- `easy convertAnything` —— 1/11 个有
- `ttN text` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
