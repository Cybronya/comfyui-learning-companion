---
name: unknown_workflow_video_inpaint_lora_14
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.55775
common_nodes: [CFGGuider, CLIPTextEncode, DiffusionModelLoaderKJ, DualCLIPLoader, GetNode, ImageFromBatch, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, MaskPreview, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetNode, SolidMask, VAEDecodeTiled, VAEEncodeForInpaint, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/AI代码侠土豆-LTX-2.3 视频去字幕_动态水印_2054808421421076482.json, 平台全量/LTX-2.3 视频去字幕_动态水印_2062353654644043778.json, 平台全量/Ltx2.3视频去字幕水印_2086822719689154561.json, 视频生成/图生视频/视频去字幕_动态水印_2059527280287903746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_14

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/AI代码侠土豆-LTX-2.3 视频去字幕_动态水印_2054808421421076482.json、平台全量/LTX-2.3 视频去字幕_动态水印_2062353654644043778.json、平台全量/Ltx2.3视频去字幕水印_2086822719689154561.json、视频生成/图生视频/视频去字幕_动态水印_2059527280287903746.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `GetNode`
- `ImageFromBatch`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MaskPreview`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetNode`
- `SolidMask`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Float to Int` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `Image To Mask` —— 3/4 个有
- `LayerUtility: ColorImage` —— 3/4 个有
- `MaskComposite` —— 3/4 个有
- `RepeatImageBatch` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `LTXFloatToInt` —— 1/4 个有

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
