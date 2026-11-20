---
name: unknown_workflow_video_lora_sampler_69
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.697091
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/SteadDancer动作迁移终结者_1997512529716920321.json, 平台全量/SteadDancer动漫版动作迁移_1996208774207643650.json, 平台全量/SteadDancer视频动作迁移_1996159025114988545.json, 平台全量/SteadyDancer Video Style Transfer_2084124870522265601.json, 平台全量/SteadyDancer-姿势复刻_1996043226471677953.json, 平台全量/SteadyDancer动作迁移_1995846381677993986.json, 平台全量/SteadyDancer动作迁移_万物舞蹈_1996131432047263746.json, 平台全量/SteadyDancer动作迁移（适配各类型主体）_1983845688792485890.json, 平台全量/Wanvideo_SteadyDancer 动作迁移_1996402034372911106.json, 平台全量/动作迁移2.0SteadDancer（支持动漫人物）t人物一致性加强版（10s+）_1996119833295142913.json, 视频生成/图生视频/Wan+SteadyDancer+卡通姿势复刻_1995897801131409409.json, 视频生成/图生视频/人物舞蹈 美女跳舞（10s+时间加长版）动作迁移   SteadDancer 2.0（支持动漫人物）_2041689230266601473.json, 视频生成/图生视频/动作迁移2.0SteadDancer 人物一致性_2026927442052521986.json, 视频生成/图生视频/动作迁移2.0_2044626494164574210.json, 视频生成/图生视频/动作迁移2.0（支持动漫）t人物一致性加强版（10s+）_2042133544960528385.json, 视频生成/图生视频/动作迁移2.0（支持动漫）人物一致性加强版_2047574668227383297.json, 视频生成/图生视频/动漫人物动作迁移2.0SteadDancer_2042111838783021057.json, 视频生成/图生视频/图生视频动作迁移SteadDancer2.0 支持动漫人物Q版动物 人物一致性加强版（10s+）_2076831167663394817.json, 视频生成/图生视频/超长时间10s+ 图生视频角色人物动作姿势迁移 支持动漫人物  模特一致性加强版_2062707841848406017.json, 视频生成/图生视频/（10s+时间加长版）动作迁移 人物舞蹈 美女跳舞 SteadDancer 2.0（支持动漫人物）_2041680923317506050.json, 视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045730540698996738.json, 视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045733887124447234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_69

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（平台全量/SteadDancer动作迁移终结者_1997512529716920321.json、平台全量/SteadDancer动漫版动作迁移_1996208774207643650.json、平台全量/SteadDancer视频动作迁移_1996159025114988545.json、平台全量/SteadyDancer Video Style Transfer_2084124870522265601.json、平台全量/SteadyDancer-姿势复刻_1996043226471677953.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoBlockSwap`
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
- `DrawViTPose` —— 21/22 个有
- `OnnxDetectionModelLoader` —— 21/22 个有
- `PoseAndFaceDetection` —— 21/22 个有
- `WanVideoSetBlockSwap` —— 20/22 个有
- `WanVideoSetLoRAs` —— 20/22 个有
- `GetImageSizeAndCount` —— 19/22 个有
- `WanVideoScheduler` —— 19/22 个有
- `WanVideoTorchCompileSettings` —— 19/22 个有
- `GetNode` —— 18/22 个有
- `SetNode` —— 18/22 个有
- `ImageConcatMulti` —— 16/22 个有
- `Int` —— 15/22 个有
- `Text` —— 15/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/22 个有
- `PreviewImage` —— 14/22 个有
- `MathExpression|pysssss` —— 13/22 个有
- `DF_Int_to_Float` —— 12/22 个有
- `RH_Sora2_I2V` —— 11/22 个有
- `easy getNode` —— 8/22 个有
- `easy setNode` —— 8/22 个有
- `INTConstant` —— 5/22 个有
- `SimpleMath+` —— 3/22 个有
- `VHS_VideoInfo` —— 2/22 个有
- `easy showAnything` —— 2/22 个有
- `DWPreprocessor` —— 1/22 个有
- `FloatConstant` —— 1/22 个有
- `JWInteger` —— 1/22 个有
- `RH_Translator` —— 1/22 个有
- `VHS_VideoInfoLoaded` —— 1/22 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
