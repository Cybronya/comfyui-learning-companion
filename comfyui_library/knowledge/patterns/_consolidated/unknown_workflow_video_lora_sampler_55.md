---
name: unknown_workflow_video_lora_sampler_55
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.6476
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2004915777457319937.json, 视频生成/图生视频/1995897801131409409.json, 视频生成/图生视频/2006239451319635970.json, 视频生成/图生视频/1996231020791873537.json, 视频生成/图生视频/2042801321077641218.json, 视频生成/图生视频/2041737868690853890.json, 视频生成/图生视频/1995382364060758018.json, 视频生成/图生视频/【推荐】SteadyDancer_骨骼迁移_不限时长版_2008549771673346050.json, 视频生成/图生视频/2041689230266601473.json, 视频生成/图生视频/2026927442052521986.json, 视频生成/图生视频/2044626494164574210.json, 视频生成/图生视频/2042133544960528385.json, 视频生成/图生视频/2047574668227383297.json, 视频生成/图生视频/2042111838783021057.json, 视频生成/图生视频/2076831167663394817.json, 视频生成/图生视频/1995812205289410562.json, 视频生成/图生视频/2062707841848406017.json, 视频生成/图生视频/2041680923317506050.json, 视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045730540698996738.json, 视频生成/文生视频/10s+图生视频+时间加长版 人物舞蹈+美女跳舞 动作迁移+++SteadDancer+2.0（支持_2045733887124447234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_55

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/2004915777457319937.json、视频生成/图生视频/1995897801131409409.json、视频生成/图生视频/2006239451319635970.json、视频生成/图生视频/1996231020791873537.json、视频生成/图生视频/2042801321077641218.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 20 个 workflow 都包含：
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
- `WanVideoScheduler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 19/20 个有
- `ImageConcatMulti` —— 19/20 个有
- `WanVideoBlockSwap` —— 18/20 个有
- `WanVideoSetBlockSwap` —— 18/20 个有
- `DrawViTPose` —— 16/20 个有
- `PoseAndFaceDetection` —— 16/20 个有
- `Int` —— 15/20 个有
- `PreviewImage` —— 15/20 个有
- `WanVideoTorchCompileSettings` —— 13/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/20 个有
- `Text` —— 12/20 个有
- `DF_Int_to_Float` —— 11/20 个有
- `MathExpression|pysssss` —— 11/20 个有
- `RH_Sora2_I2V` —— 10/20 个有
- `easy getNode` —— 7/20 个有
- `easy setNode` —— 7/20 个有
- `PoseDetectionOneToAllAnimation` —— 5/20 个有
- `CR Prompt Text` —— 3/20 个有
- `TextInput_` —— 2/20 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/20 个有
- `GIMMVFI_interpolate` —— 1/20 个有
- `INTConstant` —— 1/20 个有
- `LayerUtility: PurgeVRAM V2` —— 1/20 个有
- `Text Multiline` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
