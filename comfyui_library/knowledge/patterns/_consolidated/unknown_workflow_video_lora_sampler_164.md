---
name: unknown_workflow_video_lora_sampler_164
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.534
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetImageRangeFromBatch, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/Alan测-SCAIL2-循环长视频_2065033315945631746.json, 视频生成/图生视频/SCAIL2 全自动循环流+替换人物+动作模仿_2067092376300122114.json, 视频生成/图生视频/SCAIL2视频人物替换无限时长替换人物动作迁移人物替换_2065218467845988354.json, 视频生成/图生视频/Scail2-动作迁移-AIGC大赏_2065273440239710209.json, 视频生成/图生视频/Scail2-动作迁移-AIGC大赏_2065316694119510016.json, 视频生成/图生视频/完美动作迁移-SCAIL2_多参考图_2071761838928384001.json, 视频生成/图生视频/新王驾到 SCAIL2-人物替换，极速循环长视频_2065696343452110850.json, 视频生成/图生视频/新王驾到 SCAIL2-动作迁移，极速循环长视频_2065580332925145090.json, 视频生成/图生视频/最新SCAIL2动作迁移+人物替换极速工作流_2064927798959104002.json, 视频生成/图生视频/最新SCAIL2多人动作迁移+人物替换极速工作流_2065259619429212162.json, 视频生成/文生视频/SCAIL2-动作迁移（二创、跳舞、动作）_2064755609194549249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_164

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Alan测-SCAIL2-循环长视频_2065033315945631746.json、视频生成/图生视频/SCAIL2 全自动循环流+替换人物+动作模仿_2067092376300122114.json、视频生成/图生视频/SCAIL2视频人物替换无限时长替换人物动作迁移人物替换_2065218467845988354.json、视频生成/图生视频/Scail2-动作迁移-AIGC大赏_2065273440239710209.json、视频生成/图生视频/Scail2-动作迁移-AIGC大赏_2065316694119510016.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 10/11 个有
- `Int` —— 10/11 个有
- `MathExpression|pysssss` —— 10/11 个有
- `ModelSamplingSD3` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `VHS_VideoInfoLoaded` —— 10/11 个有
- `ImpactConditionalBranch` —— 9/11 个有
- `PrimitiveBoolean` —— 9/11 个有
- `Fast Groups Muter (rgthree)` —— 8/11 个有
- `ImageConcatMulti` —— 8/11 个有
- `Mute / Bypass Relay (rgthree)` —— 8/11 个有
- `Mute / Bypass Repeater (rgthree)` —— 8/11 个有
- `SimpleMath+` —— 3/11 个有
- `TTResolutionSelector` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `SaveImage` —— 2/11 个有
- `TT_img_enc_v2` —— 2/11 个有
- `ArchAi3D_HighPass_Blend` —— 1/11 个有
- `ComfyMathExpression` —— 1/11 个有
- `DF_Int_to_Float` —— 1/11 个有
- `ImageBatchMulti` —— 1/11 个有
- `LoadImageGoohai` —— 1/11 个有
- `MuyeTextEditOutput` —— 1/11 个有
- `Primitive integer [Crystools]` —— 1/11 个有
- `VHS_VideoInfo` —— 1/11 个有
- `easy boolean` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
