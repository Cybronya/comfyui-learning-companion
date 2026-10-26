---
name: unknown_workflow_video_lora_sampler_286
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.452
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetNode, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [数字人/数字人/scail2_2068593062779121665.json, 视频生成/图生视频/10段换装 最终版本_2077357335839854594.json, 视频生成/图生视频/10段换装 补帧_2077460288709947393.json, 视频生成/图生视频/10段换装_2077288214603329538.json, 视频生成/图生视频/10段换装改_2077324573078548481.json, 视频生成/图生视频/SCAIL 2无限动作迁移_2065286628096167938.json, 视频生成/图生视频/SCAIL 2视频角色替换3D动作迁移_2064555210772668418.json, 视频生成/图生视频/SCAIL-2分镜视频动作模仿_2064715450155618306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_286

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/scail2_2068593062779121665.json、视频生成/图生视频/10段换装 最终版本_2077357335839854594.json、视频生成/图生视频/10段换装 补帧_2077460288709947393.json、视频生成/图生视频/10段换装_2077288214603329538.json、视频生成/图生视频/10段换装改_2077324573078548481.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 7/8 个有
- `ColorTransfer` —— 7/8 个有
- `DiffusionModelLoaderKJ` —— 7/8 个有
- `GetImageRangeFromBatch` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `WanChunkFeedForward` —— 7/8 个有
- `ComfyMathExpression` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `VHS_VideoInfo` —— 4/8 个有
- `ComfySwitchNode` —— 3/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `RMBG` —— 3/8 个有
- `TextInput_` —— 3/8 个有
- `VHS_GetImageCount` —— 3/8 个有
- `easy forLoopEnd` —— 3/8 个有
- `easy forLoopStart` —— 3/8 个有
- `ExtractStoryboards_xuhuan1024` —— 1/8 个有
- `FL_RIFE` —— 1/8 个有
- `IntBatchSize_xuhuan1024` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `SplitStringByDelimiter` —— 1/8 个有
- `StringToInt` —— 1/8 个有
- `TTResolutionSelector` —— 1/8 个有
- `UNETLoader` —— 1/8 个有
- `WanContextWindowsManual` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
