---
name: unknown_workflow_video_lora_sampler_68
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.6515
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/SteadyDancer视频动作迁移【1.0】_1995877090840961026.json, 视频生成/图生视频/steadydancer跳舞工作流_1996231020791873537.json, 视频生成/图生视频/wan22 wan2.2  动作迁移 SteadyDancer 角色替换_2042801321077641218.json, 视频生成/图生视频/wan22 动作迁移 SteadyDancer 角色替换_2041737868690853890.json, 视频生成/图生视频/wanvideo_SteadyDancer_1995382364060758018.json, 视频生成/图生视频/【推荐】SteadyDancer_骨骼迁移_不限时长版_2008549771673346050.json, 视频生成/图生视频/人物舞蹈 美女跳舞（10s+时间加长版）动作迁移   SteadDancer 2.0（支持动漫人物）_2041689230266601473.json, 视频生成/图生视频/动作迁移2.0SteadDancer 人物一致性_2026927442052521986.json, 视频生成/图生视频/动作迁移2.0_2044626494164574210.json, 视频生成/图生视频/动作迁移2.0（支持动漫）t人物一致性加强版（10s+）_2042133544960528385.json, 视频生成/图生视频/动作迁移2.0（支持动漫）人物一致性加强版_2047574668227383297.json, 视频生成/图生视频/动漫人物动作迁移2.0SteadDancer_2042111838783021057.json, 视频生成/图生视频/图生视频动作迁移SteadDancer2.0 支持动漫人物Q版动物 人物一致性加强版（10s+）_2076831167663394817.json, 视频生成/图生视频/超好用🔥一键复刻跳舞视频-动作迁移-不限时长版-表情复刻-最新_2057722585600843777.json, 视频生成/图生视频/超长时间10s+ 图生视频角色人物动作姿势迁移 支持动漫人物  模特一致性加强版_2062707841848406017.json, 视频生成/图生视频/骨骼迁移_不限时长版_2021769557274271746.json, 视频生成/图生视频/（10s+时间加长版）动作迁移 人物舞蹈 美女跳舞 SteadDancer 2.0（支持动漫人物）_2041680923317506050.json, 视频生成/图生视频/（KJ版）SteadDancer视频姿势参考（新增骨骼绑定）_1995843794539098113.json, 视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045730540698996738.json, 视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045733887124447234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_68

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/SteadyDancer视频动作迁移【1.0】_1995877090840961026.json、视频生成/图生视频/steadydancer跳舞工作流_1996231020791873537.json、视频生成/图生视频/wan22 wan2.2  动作迁移 SteadyDancer 角色替换_2042801321077641218.json、视频生成/图生视频/wan22 动作迁移 SteadyDancer 角色替换_2041737868690853890.json、视频生成/图生视频/wanvideo_SteadyDancer_1995382364060758018.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 20 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 19/20 个有
- `ImageConcatMulti` —— 19/20 个有
- `OnnxDetectionModelLoader` —— 19/20 个有
- `WanVideoLoraSelect` —— 19/20 个有
- `WanVideoScheduler` —— 19/20 个有
- `PreviewImage` —— 17/20 个有
- `WanVideoBlockSwap` —— 17/20 个有
- `WanVideoSetBlockSwap` —— 17/20 个有
- `DrawViTPose` —— 14/20 个有
- `Int` —— 14/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/20 个有
- `PoseAndFaceDetection` —— 14/20 个有
- `WanVideoTorchCompileSettings` —— 14/20 个有
- `DF_Int_to_Float` —— 11/20 个有
- `MathExpression|pysssss` —— 11/20 个有
- `Text` —— 11/20 个有
- `RH_Sora2_I2V` —— 10/20 个有
- `easy getNode` —— 7/20 个有
- `easy setNode` —— 7/20 个有
- `PoseDetectionOneToAllAnimation` —— 6/20 个有
- `TextInput_` —— 3/20 个有
- `CR Prompt Text` —— 2/20 个有
- `ImpactInt` —— 2/20 个有
- `INTConstant` —— 1/20 个有
- `RHHiddenNodes` —— 1/20 个有
- `SimpleMath+` —— 1/20 个有
- `VHS_VideoInfo` —— 1/20 个有
- `easy int` —— 1/20 个有
- `easy positive` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
