---
name: unknown_workflow_video_lora_sampler_127
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.467786
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DiffusionModelLoaderKJ, GetImageRangeFromBatch, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [数字人/数字人/SCAIL-2替换人物_动作迁移_2065095439338270721.json, 数字人/数字人/SCAIL2人物替换_2064916188177719298.json, 数字人/数字人/scail动作迁移_2004737349160497153.json, 数字人/数字人/女装带货_2089734181499789314.json, 数字人/数字人/视频动作模仿迁移SCAIL2-循环长视频_2065350192374837250.json, 视频生成/图生视频/Alan测-SCAIL2-循环长视频_2065033315945631746.json, 视频生成/图生视频/SCAIL2 全自动循环流+替换人物+动作模仿_2067092376300122114.json, 视频生成/图生视频/SCAIL2视频人物替换无限时长替换人物动作迁移人物替换_2065218467845988354.json, 视频生成/图生视频/Scail2-动作迁移-AIGC大赏_2065273440239710209.json, 视频生成/图生视频/Scail2-动作迁移-AIGC大赏_2065316694119510016.json, 视频生成/图生视频/新王驾到 SCAIL2-人物替换，极速循环长视频_2065696343452110850.json, 视频生成/图生视频/新王驾到 SCAIL2-动作迁移，极速循环长视频_2065580332925145090.json, 视频生成/图生视频/最新SCAIL2动作迁移+人物替换极速工作流_2064927798959104002.json, 视频生成/图生视频/最新SCAIL2多人动作迁移+人物替换极速工作流_2065259619429212162.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_127

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（数字人/数字人/SCAIL-2替换人物_动作迁移_2065095439338270721.json、数字人/数字人/SCAIL2人物替换_2064916188177719298.json、数字人/数字人/scail动作迁移_2004737349160497153.json、数字人/数字人/女装带货_2089734181499789314.json、数字人/数字人/视频动作模仿迁移SCAIL2-循环长视频_2065350192374837250.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DiffusionModelLoaderKJ`
- `GetImageRangeFromBatch`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 13/14 个有
- `ImageResizeKJv2` —— 13/14 个有
- `Int` —— 13/14 个有
- `PreviewImage` —— 13/14 个有
- `SAM3_VideoTrack` —— 13/14 个有
- `SCAIL2ColoredMask` —— 13/14 个有
- `easy batchAnything` —— 13/14 个有
- `easy forLoopEnd` —— 13/14 个有
- `easy forLoopStart` —— 13/14 个有
- `easy imageRemBg` —— 13/14 个有
- `ModelSamplingSD3` —— 12/14 个有
- `MathExpression|pysssss` —— 11/14 个有
- `VHS_VideoInfoLoaded` —— 11/14 个有
- `ImageConcatMulti` —— 10/14 个有
- `ImpactConditionalBranch` —— 9/14 个有
- `Fast Groups Muter (rgthree)` —— 8/14 个有
- `Mute / Bypass Relay (rgthree)` —— 8/14 个有
- `Mute / Bypass Repeater (rgthree)` —— 8/14 个有
- `PrimitiveBoolean` —— 8/14 个有
- `easy showAnything` —— 6/14 个有
- `CR Text` —— 4/14 个有
- `TTResolutionSelector` —— 4/14 个有
- `SimpleMath+` —— 3/14 个有
- `ComfyMathExpression` —— 2/14 个有
- `DF_Int_to_Float` —— 2/14 个有
- `PathchSageAttentionKJ` —— 2/14 个有
- `SaveImage` —— 2/14 个有
- `TT_img_enc_v2` —— 2/14 个有
- `VHS_VideoInfo` —— 2/14 个有
- `ArchAi3D_HighPass_Blend` —— 1/14 个有
- `BatchImagesNode` —— 1/14 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/14 个有
- `GIMMVFI_interpolate` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `LoadImageGoohai` —— 1/14 个有
- `Primitive integer [Crystools]` —— 1/14 个有
- `WanChunkFeedForward` —— 1/14 个有
- `easy boolean` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
