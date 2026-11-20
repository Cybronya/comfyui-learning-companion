---
name: unknown_workflow_video_lora_sampler_197
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.974667
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_LoadVideo, VHS_VideoCombine, easy imageSize]
problems: []
missing: []
members: [平台全量/电商视频一键去水印字幕 最长15秒 Ltx2.3_2053753733829414913.json, 平台全量/绝不高尚——高清+水印+字幕+修复 一条龙_2054859246126280706.json, 平台全量/视频-去水印字幕-ltx2.3-IC+Edit_2054786725641236481.json, 平台全量/视频-高清修复-ltx2.3-IC+Edit_2054786746356912130.json, 平台全量/视频去字幕+去动态水印_2118246152654118913.json, 平台全量/视频去字幕LTX2.3_2055475100765442050.json, 平台全量/视频去字幕去动态水印 ltx2.3_2104112225635102721.json, 平台全量/👾怪獸-LTX2.3-ICLora视频去字幕、水印工作流👾_2054562475563069442.json, 平台全量/👾怪獸-LTX2.3-ICLora视频高清+修复工作流👾_2054568962419118082.json, 视频生成/图生视频/LTX-2.3-ICLORA斗鸡眼+自动优化提示词版V1_2067532074952781825.json, 视频生成/图生视频/YJ-ltx2.3去水印 (1)_2069702802959589378.json, 视频生成/图生视频/图生视频去水印_2061290081482264578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_197

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/电商视频一键去水印字幕 最长15秒 Ltx2.3_2053753733829414913.json、平台全量/绝不高尚——高清+水印+字幕+修复 一条龙_2054859246126280706.json、平台全量/视频-去水印字幕-ltx2.3-IC+Edit_2054786725641236481.json、平台全量/视频-高清修复-ltx2.3-IC+Edit_2054786746356912130.json、平台全量/视频去字幕+去动态水印_2118246152654118913.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ColorImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Image To Mask` —— 11/12 个有
- `LTXICLoRALoaderModelOnly` —— 11/12 个有
- `RepeatImageBatch` —— 11/12 个有
- `SimpleMath+` —— 11/12 个有
- `VAEEncodeForInpaint` —— 11/12 个有
- `LTX2SamplingPreviewOverride` —— 10/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/12 个有
- `LoraLoaderModelOnly` —— 10/12 个有
- `PathchSageAttentionKJ` —— 10/12 个有
- `Seed (rgthree)` —— 10/12 个有
- `VHS_VideoInfoLoaded` —— 10/12 个有
- `ResizeImageMaskNode` —— 9/12 个有
- `ImageConcanate` —— 6/12 个有
- `MathExpression|pysssss` —— 5/12 个有
- `CR Prompt Text` —— 4/12 个有
- `Int` —— 4/12 个有
- `CR Text` —— 2/12 个有
- `GetImageSizeAndCount` —— 2/12 个有
- `ImageStitch` —— 2/12 个有
- `Label (rgthree)` —— 2/12 个有
- `PrimitiveFloat` —— 2/12 个有
- `easy imageCount` —— 2/12 个有
- `easy seed` —— 2/12 个有
- `CreateVideo` —— 1/12 个有
- `EmptyLTXVLatentVideo` —— 1/12 个有
- `ImageBatchMulti` —— 1/12 个有
- `JjkText` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `RHLLMChatNode` —— 1/12 个有
- `easy getNode` —— 1/12 个有
- `easy setNode` —— 1/12 个有
- `easy showAnything` —— 1/12 个有
- `image_scale_pixel_v2` —— 1/12 个有

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
