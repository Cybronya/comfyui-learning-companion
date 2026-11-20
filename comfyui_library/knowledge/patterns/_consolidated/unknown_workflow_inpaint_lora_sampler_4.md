---
name: unknown_workflow_inpaint_lora_sampler_4
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.953125
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, Image To Mask, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [图片生成/图生图/K老师_专属_去水印，去字幕，去模糊_2069077577020559362.json, 图片生成/图生图/YJ-ltx2.3去水印_2059470618550161409.json, 图片生成/图生图/全自动一键去水印+字幕+修复模糊+高清放大_2054218745601642497.json, 图片生成/图生图/去水印，去字幕（豆包水印去除)_2072800070940053506.json, 图片生成/文生图/LTX2.3-ICEdit-Insight去水印+去字幕_2073320595470770178.json, 图片生成/文生图/LTX2.3-ICEdit-Insight去水印_去字幕_去模糊_高清化_2073320398938267649.json, 图片生成/文生图/去模糊，高清LTX2.3_iclora_insight工作流_2057411893463179265.json, 图片生成/文生图/四合一去水印_字幕_修复模糊_高清放大_2057406073866379265.json, 图片生成/文生图/视频全自动一键去水印_字幕_修复模糊_高清放大全自动一键去水印_字幕_修复模糊_高清放大_2068564459328729090.json, 平台全量/(自用) LTX2.3 字幕水印修复、高清、去模糊工作流_2059272599074594817.json, 平台全量/LTX2.3极速去水印去字幕去模糊高清即梦豆包去水印_2101873762080747522.json, 平台全量/ltx23智能一键去字幕_2074494133229674497.json, 平台全量/seedance2.0视频处理工具去水印、去字幕（ltx2.3模型最新lora）_2055285710722215938.json, 平台全量/视频去字幕_去模糊_高清化_2074861201686876162.json, 视频生成/图生视频/一键去字幕水印去模糊_2094407100247134209.json, 视频生成/图生视频/四合一去水印+_+字幕+_+修复模糊+_+高清放大_2059081651447222274.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/K老师_专属_去水印，去字幕，去模糊_2069077577020559362.json、图片生成/图生图/YJ-ltx2.3去水印_2059470618550161409.json、图片生成/图生图/全自动一键去水印+字幕+修复模糊+高清放大_2054218745601642497.json、图片生成/图生图/去水印，去字幕（豆包水印去除)_2072800070940053506.json、图片生成/文生图/LTX2.3-ICEdit-Insight去水印+去字幕_2073320595470770178.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
- `Image To Mask`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 12/16 个有
- `SimpleMath+` —— 12/16 个有
- `VHS_VideoCombine` —— 12/16 个有
- `easy imageSize` —— 12/16 个有
- `Text Multiline` —— 10/16 个有
- `ImageConcatMulti` —— 9/16 个有
- `Fast Groups Bypasser (rgthree)` —— 5/16 个有
- `INTConstant` —— 5/16 个有
- `ComfyMathExpression` —— 4/16 个有
- `CreateVideo` —— 4/16 个有
- `GetImageSize` —— 4/16 个有
- `Int` —— 4/16 个有
- `LTXVAudioVAEDecode` —— 4/16 个有
- `PrimitiveInt` —— 4/16 个有
- `SaveVideo` —— 4/16 个有
- `CR String To Combo` —— 3/16 个有
- `ImpactStringSelector` —— 3/16 个有
- `MathExpression|pysssss` —— 3/16 个有
- `SplitStringByDelimiter` —— 3/16 个有
- `easy showAnything` —— 3/16 个有
- `BatchImagesNode` —— 1/16 个有
- `CR Prompt Text` —— 1/16 个有
- `LoadVideo` —— 1/16 个有
- `PlaySound|pysssss` —— 1/16 个有
- `RIFE VFI` —— 1/16 个有
- `VAEDecode` —— 1/16 个有
- `忽略多组孤海` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 16 | 100% |
| 高度 | 25 | 25 - 25 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，16 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，16 个样本，取值集中（一致性 100%）
