---
name: unknown_workflow_video_lora_sampler_290
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.433429
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetImageRangeFromBatch, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [数字人/数字人/Scail2_v01_2096895345262424066.json, 数字人/数字人/Scail2多参工作流_2096877747174989825.json, 数字人/数字人/一键复刻爆款视频_2097251150608297986.json, 数字人/数字人/女装带货_2089734181499789314.json, 视频生成/图生视频/2065286628096167938.json, 视频生成/图生视频/2064555210772668418.json, 视频生成/图生视频/2064715450155618306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_290

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/Scail2_v01_2096895345262424066.json、数字人/数字人/Scail2多参工作流_2096877747174989825.json、数字人/数字人/一键复刻爆款视频_2097251150608297986.json、数字人/数字人/女装带货_2089734181499789314.json、视频生成/图生视频/2065286628096167938.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 7 个 workflow 都包含：
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
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 6/7 个有
- `ModelSamplingSD3` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `ComfyMathExpression` —— 4/7 个有
- `GetNode` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `VHS_VideoInfo` —— 4/7 个有
- `easy batchAnything` —— 4/7 个有
- `easy imageRemBg` —— 4/7 个有
- `BatchImagesNode` —— 3/7 个有
- `ColorTransfer` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `RMBG` —— 3/7 个有
- `SingleBooleanTrigger` —— 3/7 个有
- `TextInput_` —— 3/7 个有
- `VHS_GetImageCount` —— 3/7 个有
- `WanChunkFeedForward` —— 3/7 个有
- `Float` —— 2/7 个有
- `ImageBatchMultiple+` —— 2/7 个有
- `ImageFromBatch` —— 2/7 个有
- `Int` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `SaveVideoRGBA` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `DF_Int_to_Float` —— 1/7 个有
- `ExtractStoryboards_xuhuan1024` —— 1/7 个有
- `IntBatchSize_xuhuan1024` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `SplitStringByDelimiter` —— 1/7 个有
- `StringToInt` —— 1/7 个有
- `TTResolutionSelector` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
