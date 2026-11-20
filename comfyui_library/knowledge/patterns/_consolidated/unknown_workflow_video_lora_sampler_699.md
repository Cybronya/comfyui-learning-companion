---
name: unknown_workflow_video_lora_sampler_699
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.6605
common_nodes: [AILab_MiniCPM_4_V, CLIPLoader, CLIPTextEncode, CreateVideo, DiffusionModelLoaderKJ, Florence2ModelLoader, Florence2Run, GetImageSizeAndCount, GetNode, INTConstant, ImageConcanate, ImageFromBatch, ImageFromBatch+, ImageResizeKJv2, ImpactFloat, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, MathExpression|pysssss, MemoryCleaner, PreviewImage, PrimitiveFloat, RH_Captioner, SaveImage, SetNode, ShowText|pysssss, StringFunction|pysssss, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanImageToVideoSVIPro, easy imageSize, easy int, easy positive, easy promptReplace, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [平台全量/视频-视频生视频(分割)-wan2.2-SVI+2.0+Pro_2048578301354057730.json, 平台全量/视频-视频生视频-wan2.2-SVI 2.0 Pro-smooth-官方_2018179536462024706.json, 平台全量/视频-视频生视频参考图(分割)-wan2.2-SVI 2.0 Pro-smooth-官方_2019642874224185345.json, 视频生成/图生视频/视频-视频生视频(分割)-wan2.2-SVI 2.0 Pro-smooth-官方_2019299975187931138.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_699

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/视频-视频生视频(分割)-wan2.2-SVI+2.0+Pro_2048578301354057730.json、平台全量/视频-视频生视频-wan2.2-SVI 2.0 Pro-smooth-官方_2018179536462024706.json、平台全量/视频-视频生视频参考图(分割)-wan2.2-SVI 2.0 Pro-smooth-官方_2019642874224185345.json、视频生成/图生视频/视频-视频生视频(分割)-wan2.2-SVI 2.0 Pro-smooth-官方_2019299975187931138.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_MiniCPM_4_V`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `DiffusionModelLoaderKJ`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `ImpactFloat`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MemoryCleaner`
- `PreviewImage`
- `PrimitiveFloat`
- `RH_Captioner`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanImageToVideoSVIPro`
- `easy imageSize`
- `easy int`
- `easy positive`
- `easy promptReplace`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `AnyBatchSliceNode` —— 3/4 个有
- `CFGGuider` —— 3/4 个有
- `CM_IntToBool` —— 3/4 个有
- `CM_IntUnaryOperation` —— 3/4 个有
- `CR Float To Integer` —— 3/4 个有
- `CR String To Number` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `EmptyFlux2LatentImage` —— 3/4 个有
- `EmptyLatentImage` —— 3/4 个有
- `FL_VideoCadence` —— 3/4 个有
- `Float` —— 3/4 个有
- `Flux2Scheduler` —— 3/4 个有
- `GODMT_ListToBatch` —— 3/4 个有
- `ImageToDevice+` —— 3/4 个有
- `ImpactInt` —— 3/4 个有
- `Int` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `ModelPatchLoader` —— 3/4 个有
- `RandomNoise` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `SamplerCustomAdvanced` —— 3/4 个有
- `SegmentFrameAdjuster` —— 3/4 个有
- `Switch any [Crystools]` —— 3/4 个有
- `Text List to Text` —— 3/4 个有
- `TextSplitByDelimiter` —— 3/4 个有
- `ZImageFunControlnet` —— 3/4 个有
- `easy batchAnything` —— 3/4 个有
- `easy forLoopEnd` —— 3/4 个有
- `easy forLoopStart` —— 3/4 个有
- `easy lengthAnything` —— 3/4 个有
- `easy mathInt` —— 3/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `easy anythingInversedSwitch` —— 2/4 个有
- `AutoCropFaces` —— 1/4 个有
- `HunyuanVideoFoley` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 10 | 8 - 10 | 4 | 91% |
| 采样算法 | 1 | 1 - 2 | 4 | 65% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |
| 宽度 | 1920 | 1920 - 1920 | 3 | 100% |
| 高度 | 1080 | 1080 - 1080 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 2，4 个样本
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 宽度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
