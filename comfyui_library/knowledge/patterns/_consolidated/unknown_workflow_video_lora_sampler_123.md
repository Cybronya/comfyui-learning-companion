---
name: unknown_workflow_video_lora_sampler_123
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.457231
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetImageRangeFromBatch, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2073324810372993026.json, 视频生成/图生视频/2064678206946496514.json, 视频生成/图生视频/2065273822449856514.json, 视频生成/图生视频/2067601389454454786.json, 视频生成/图生视频/2067602340542246914.json, 视频生成/图生视频/2065718753207349250.json, 视频生成/图生视频/2065006346432503810.json, 视频生成/图生视频/2066834222895161346.json, 视频生成/图生视频/2065258951524048898.json, 视频生成/图生视频/2067171226954584065.json, 视频生成/图生视频/2069078995290906625.json, 视频生成/图生视频/2066697586874085378.json, 视频生成/图生视频/2065406697937657858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_123

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2073324810372993026.json、视频生成/图生视频/2064678206946496514.json、视频生成/图生视频/2065273822449856514.json、视频生成/图生视频/2067601389454454786.json、视频生成/图生视频/2067602340542246914.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：46%

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
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveInt`
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
- `GetNode` —— 11/13 个有
- `ImageConcatMulti` —— 11/13 个有
- `ImageFromBatch` —— 11/13 个有
- `PreviewAny` —— 11/13 个有
- `SetNode` —— 11/13 个有
- `SimpleMath+` —— 11/13 个有
- `WanChunkFeedForward` —— 11/13 个有
- `ttN int` —— 11/13 个有
- `easy cleanGpuUsed` —— 10/13 个有
- `PreviewImage` —— 9/13 个有
- `JjkText` —— 8/13 个有
- `Seed` —— 7/13 个有
- `AILab_QwenVL` —— 6/13 个有
- `PrimitiveBoolean` —— 4/13 个有
- `easy imageRemBg` —— 4/13 个有
- `InversionDemoLazySwitch` —— 3/13 个有
- `ShowText|pysssss` —— 3/13 个有
- `Label (rgthree)` —— 2/13 个有
- `BOOLConstant` —— 1/13 个有
- `ComfyMathExpression` —— 1/13 个有
- `PrimitiveString` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `SaveImage` —— 1/13 个有
- `TT_img_enc` —— 1/13 个有
- `easy batchAnything` —— 1/13 个有
- `easy forLoopEnd` —— 1/13 个有
- `easy forLoopStart` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
