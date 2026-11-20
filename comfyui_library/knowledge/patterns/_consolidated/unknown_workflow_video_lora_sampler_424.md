---
name: unknown_workflow_video_lora_sampler_424
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.449571
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/SCAIL2+动作迁移_角色替换+relighting+无限时长_2080312516533637121.json, 数字人/数字人/scail2_2068593062779121665.json, 视频生成/图生视频/10段换装 最终版本_2077357335839854594.json, 视频生成/图生视频/10段换装 补帧_2077460288709947393.json, 视频生成/图生视频/10段换装_2077288214603329538.json, 视频生成/图生视频/10段换装改_2077324573078548481.json, 视频生成/图生视频/SCAIL2 Animation & Replacement 动作迁移&角色替换_2075056544013709313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_424

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/SCAIL2+动作迁移_角色替换+relighting+无限时长_2080312516533637121.json、数字人/数字人/scail2_2068593062779121665.json、视频生成/图生视频/10段换装 最终版本_2077357335839854594.json、视频生成/图生视频/10段换装 补帧_2077460288709947393.json、视频生成/图生视频/10段换装_2077288214603329538.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DiffusionModelLoaderKJ` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `SamplerCustom` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `VAEDecode` —— 6/7 个有
- `WanSCAILToVideo` —— 6/7 个有
- `BatchImagesNode` —— 5/7 个有
- `ColorTransfer` —— 5/7 个有
- `ComfyMathExpression` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `GetImageRangeFromBatch` —— 5/7 个有
- `WanChunkFeedForward` —— 5/7 个有
- `PrimitiveBoolean` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `VHS_VideoInfo` —— 2/7 个有
- `FL_RIFE` —— 1/7 个有
- `GoogleTranslateTextNode` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `ModelPatchTorchSettings` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `PrimitiveString` —— 1/7 个有
- `SCAILAutoExtend` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `TTResolutionSelector` —— 1/7 个有
- `UNETLoader` —— 1/7 个有
- `WanContextWindowsManual` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
