---
name: unknown_workflow_video_lora_sampler_112
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.494769
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [图片生成/图生图/Scail2视频角色替换又快又好_2065296557842460673.json, 图片生成/图生图/【遇见AI】wan2.1 SCAIL2 角色替换 动作迁移 姿势参考_2065988482132168705.json, 图片生成/图生图/全新动作模仿 SCAIL2！单人or双人（懒人版）_2066568712282525697.json, 视频生成/图生视频/10段换装 最终版本_2077357335839854594.json, 视频生成/图生视频/10段换装 补帧_2077460288709947393.json, 视频生成/图生视频/10段换装_2077288214603329538.json, 视频生成/图生视频/10段换装改_2077324573078548481.json, "视频生成/图生视频/3号特工：SCAIL2动作迁移,效果岗岗的_2077367281839075329.json", 视频生成/图生视频/SCAIL2全新单双人动作模仿_2065273822449856514.json, 视频生成/图生视频/SCAIL2双人+单人角色替换！视频换人_2067601389454454786.json, 视频生成/图生视频/SCAIL2双人+单人角色替换！视频换人_2067602340542246914.json, 视频生成/图生视频/SCAIL2视频单双人动作模仿_2065718753207349250.json, 视频生成/图生视频/全新动作模仿 SCAIL2_2066834222895161346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Scail2视频角色替换又快又好_2065296557842460673.json、图片生成/图生图/【遇见AI】wan2.1 SCAIL2 角色替换 动作迁移 姿势参考_2065988482132168705.json、图片生成/图生图/全新动作模仿 SCAIL2！单人or双人（懒人版）_2066568712282525697.json、视频生成/图生视频/10段换装 最终版本_2077357335839854594.json、视频生成/图生视频/10段换装 补帧_2077460288709947393.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `ColorTransfer` —— 12/13 个有
- `WanChunkFeedForward` —— 12/13 个有
- `GetImageRangeFromBatch` —— 11/13 个有
- `GetNode` —— 11/13 个有
- `SetNode` —— 11/13 个有
- `PrimitiveInt` —— 10/13 个有
- `PreviewImage` —— 9/13 个有
- `ImageFromBatch` —— 8/13 个有
- `SimpleMath+` —— 8/13 个有
- `ttN int` —— 8/13 个有
- `ImageConcatMulti` —— 7/13 个有
- `PreviewAny` —— 7/13 个有
- `easy cleanGpuUsed` —— 7/13 个有
- `Seed` —— 6/13 个有
- `AILab_QwenVL` —— 5/13 个有
- `JjkText` —— 5/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `ComfyMathExpression` —— 3/13 个有
- `ShowText|pysssss` —— 3/13 个有
- `easy imageRemBg` —— 3/13 个有
- `InversionDemoLazySwitch` —— 2/13 个有
- `Label (rgthree)` —— 2/13 个有
- `PrimitiveBoolean` —— 2/13 个有
- `FL_RIFE` —— 1/13 个有
- `GetImageSizeAndCount` —— 1/13 个有
- `ImageScaleToTotalPixels` —— 1/13 个有
- `Int` —— 1/13 个有
- `PathchSageAttentionKJ` —— 1/13 个有
- `PurgeVRAM_UTK` —— 1/13 个有
- `SAM3_TrackPreview` —— 1/13 个有
- `SaveImage` —— 1/13 个有
- `Text` —— 1/13 个有
- `ZNGB_GetImageRangeFromBatch` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
