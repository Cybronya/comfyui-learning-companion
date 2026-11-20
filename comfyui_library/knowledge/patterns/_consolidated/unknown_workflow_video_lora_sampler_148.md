---
name: unknown_workflow_video_lora_sampler_148
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.530929
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetImageRangeFromBatch, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageRemBg]
problems: []
missing: []
members: [平台全量/AI代码侠土豆-SCAIL2 全自动循环流_2066348710275145729.json, 平台全量/Good-SCAIL2 全自动循环流_2067269625750056962.json, 平台全量/SCAIL2-循环长视频v2_2064585033121353730.json, 平台全量/SCAIL2人物替换_2120433938278735873.json, 平台全量/SCAIL2动作迁移_人物替换工作流_2065699948632563714.json, 平台全量/Wan21_SCAIL2_多参（枪版）_2066098409261588482.json, 平台全量/单人_多人 动态迁移+人物替换二合一工作流_2065801868047114241.json, 数字人/数字人/视频动作模仿迁移SCAIL2-循环长视频_2065350192374837250.json, 视频生成/图生视频/Alan测-SCAIL2-循环长视频_2065033315945631746.json, 视频生成/图生视频/Scail2-动作迁移-AIGC大赏_2065273440239710209.json, 视频生成/图生视频/Scail2-动作迁移-AIGC大赏_2065316694119510016.json, 视频生成/图生视频/完美动作迁移-SCAIL2_多参考图_2071761838928384001.json, 视频生成/图生视频/最新SCAIL2动作迁移+人物替换极速工作流_2064927798959104002.json, 视频生成/图生视频/最新SCAIL2多人动作迁移+人物替换极速工作流_2065259619429212162.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_148

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/AI代码侠土豆-SCAIL2 全自动循环流_2066348710275145729.json、平台全量/Good-SCAIL2 全自动循环流_2067269625750056962.json、平台全量/SCAIL2-循环长视频v2_2064585033121353730.json、平台全量/SCAIL2人物替换_2120433938278735873.json、平台全量/SCAIL2动作迁移_人物替换工作流_2065699948632563714.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 14 个 workflow 都包含：
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
- `GetNode` —— 13/14 个有
- `SetNode` —— 13/14 个有
- `ImpactConditionalBranch` —— 12/14 个有
- `Int` —— 12/14 个有
- `MathExpression|pysssss` —— 12/14 个有
- `ModelSamplingSD3` —— 12/14 个有
- `PrimitiveBoolean` —— 12/14 个有
- `VHS_VideoInfoLoaded` —— 12/14 个有
- `Fast Groups Muter (rgthree)` —— 10/14 个有
- `ImageConcatMulti` —— 10/14 个有
- `Mute / Bypass Relay (rgthree)` —— 8/14 个有
- `Mute / Bypass Repeater (rgthree)` —— 8/14 个有
- `TTResolutionSelector` —— 6/14 个有
- `CR Text` —— 5/14 个有
- `easy showAnything` —— 5/14 个有
- `PathchSageAttentionKJ` —— 4/14 个有
- `ArchAi3D_HighPass_Blend` —— 2/14 个有
- `ComfyMathExpression` —— 2/14 个有
- `DF_Int_to_Float` —— 2/14 个有
- `ImageBatchMulti` —— 2/14 个有
- `MuyeTextEditOutput` —— 2/14 个有
- `SaveImage` —— 2/14 个有
- `SimpleMath+` —— 2/14 个有
- `TT_img_enc_v2` —— 2/14 个有
- `VHS_VideoInfo` —— 2/14 个有
- `easy int` —— 2/14 个有
- `Label (rgthree)` —— 1/14 个有
- `LoadImageGoohai` —— 1/14 个有
- `OpenposePreprocessor` —— 1/14 个有
- `easy getNode` —— 1/14 个有
- `easy setNode` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
