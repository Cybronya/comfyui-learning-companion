---
name: unknown_workflow_video_lora_sampler_665
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.93575
common_nodes: [BasicScheduler, CLIPTextEncode, CM_FloatToInt, CR Text, DualCLIPLoader, KSamplerSelect, LTXVAddGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoraLoaderModelOnly, SamplerCustom, UNETLoader, VAEDecode, VAEEncode, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/LTX2.3 Edit Anything视频编辑_风格转绘_物体移除_2052715103241416706.json, 平台全量/LTX2.3 视频一键换装与场景替换工作流_2058448678020542466.json, 平台全量/[ComfyUI]LTX2.3视频编辑1_2052017192589381634.json, 平台全量/视频-编辑_转绘_移除-LTX2.3-Edit Anything_2055203510806949889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_665

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/LTX2.3 Edit Anything视频编辑_风格转绘_物体移除_2052715103241416706.json、平台全量/LTX2.3 视频一键换装与场景替换工作流_2058448678020542466.json、平台全量/[ComfyUI]LTX2.3视频编辑1_2052017192589381634.json、平台全量/视频-编辑_转绘_移除-LTX2.3-Edit Anything_2055203510806949889.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXVAddGuide`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `CLIPLoader` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `Float` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `Int` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `StringConcatenate` —— 1/4 个有
- `TextGenerate` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy seed` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
