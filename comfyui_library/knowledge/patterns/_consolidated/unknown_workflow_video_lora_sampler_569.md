---
name: unknown_workflow_video_lora_sampler_569
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5162
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, DiffusionModelLoaderKJ, GetImageRangeFromBatch, GetNode, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [平台全量/A-12 SCAIL2 动作迁移 长视频_2088830577804931074.json, 平台全量/SCAIL-2无限时动作克隆角色替换_2064625965908709377.json, 视频生成/图生视频/SCAIL 2无限动作迁移_2065286628096167938.json, 视频生成/图生视频/SCAIL 2视频角色替换3D动作迁移_2064555210772668418.json, 视频生成/图生视频/SCAIL-2分镜视频动作模仿_2064715450155618306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_569

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/A-12 SCAIL2 动作迁移 长视频_2088830577804931074.json、平台全量/SCAIL-2无限时动作克隆角色替换_2064625965908709377.json、视频生成/图生视频/SCAIL 2无限动作迁移_2065286628096167938.json、视频生成/图生视频/SCAIL 2视频角色替换3D动作迁移_2064555210772668418.json、视频生成/图生视频/SCAIL-2分镜视频动作模仿_2064715450155618306.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `DiffusionModelLoaderKJ`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `RMBG` —— 4/5 个有
- `TextInput_` —— 4/5 个有
- `VHS_GetImageCount` —— 4/5 个有
- `VHS_VideoInfo` —— 4/5 个有
- `WanChunkFeedForward` —— 4/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `AutoCropFaces` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `ExtractStoryboards_xuhuan1024` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `ImageSharpen` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `IntBatchSize_xuhuan1024` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `SplitStringByDelimiter` —— 1/5 个有
- `StringToInt` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
