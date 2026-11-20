---
name: unknown_workflow_video_inpaint_lora_5
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.890385
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoConditionOnly, LTXVPreprocess, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy imageSize]
problems: []
missing: []
members: [平台全量/视频去字幕、去水印、去模糊、高清修复，LTX-2.3-IC-edit-insight编辑Lora_2056737993813221378.json, 平台全量/视频去模糊高清放大LTX2.3 iclora insight工作流_2054805130561769474.json, 平台全量/视频去水印 LTX2.3时长加长版 去字幕去模糊高清 全能视频编辑_2061246795195441153.json, 平台全量/视频去水印 去字幕去模糊变高清  增加时长 LTX2.3  全能视频消除文字_2069579502979739649.json, 平台全量/视频去水印 去字幕去模糊变高清_2071790510506856450.json, 平台全量/视频去水印、去字幕、高清修复_2054459254823768066.json, 平台全量/视频去水印去字幕_2073946723587809282.json, 平台全量/视频去水印去字幕去除_2075599313127952385.json, 平台全量/视频去水印去字幕无痕-豆包、即梦、小云雀、剪映智能去水印_2080130573015797761.json, 平台全量/视频去水印字幕高清修复完整多功能三合一工作流_2065005380689813505.json, 平台全量/视频去水印字幕高清修复完整多功能工作流_2064198187778396162.json, 平台全量/超好用高质量LTX2.3极速版全自动一键同时去动静态水印+视频字幕 _ 修复模糊 _ 视频高清3选1_2054080479787274242.json, 视频生成/图生视频/视频去水印去字幕 LTX2.3时长加长_2068856868998565889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_5

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（平台全量/视频去字幕、去水印、去模糊、高清修复，LTX-2.3-IC-edit-insight编辑Lora_2056737993813221378.json、平台全量/视频去模糊高清放大LTX2.3 iclora insight工作流_2054805130561769474.json、平台全量/视频去水印 LTX2.3时长加长版 去字幕去模糊高清 全能视频编辑_2061246795195441153.json、平台全量/视频去水印 去字幕去模糊变高清  增加时长 LTX2.3  全能视频消除文字_2069579502979739649.json、平台全量/视频去水印 去字幕去模糊变高清_2071790510506856450.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Image To Mask` —— 12/13 个有
- `LTX2SamplingPreviewOverride` —— 12/13 个有
- `LTXVAudioVAELoader` —— 12/13 个有
- `LTXVConcatAVLatent` —— 12/13 个有
- `LTXVEmptyLatentAudio` —— 12/13 个有
- `LTXVSeparateAVLatent` —— 12/13 个有
- `LoraLoaderModelOnly` —— 12/13 个有
- `Text Multiline` —— 12/13 个有
- `ImageConcatMulti` —— 11/13 个有
- `SimpleMath+` —— 10/13 个有
- `MathExpression|pysssss` —— 9/13 个有
- `Seed (rgthree)` —— 9/13 个有
- `Int` —— 6/13 个有
- `ImageFromBatch+` —— 5/13 个有
- `BasicScheduler` —— 3/13 个有
- `GetNode` —— 3/13 个有
- `LTXVChunkFeedForward` —— 3/13 个有
- `LayerColor: ColorAdapter` —— 3/13 个有
- `LoadImage` —— 3/13 个有
- `ModelPatchTorchSettings` —— 3/13 个有
- `SetNode` —— 3/13 个有
- `easy anythingIndexSwitch` —— 3/13 个有
- `easy convertAnything` —— 3/13 个有
- `easy int` —— 3/13 个有
- `easy seed` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `CR Text Input Switch (4 way)` —— 1/13 个有
- `ImageToMask` —— 1/13 个有
- `ImpactInt` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `SamplerCustom` —— 1/13 个有
- `SeedVR2BlockSwap` —— 1/13 个有
- `SeedVR2ExtraArgs` —— 1/13 个有
- `SeedVR2GGUF` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
