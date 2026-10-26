---
name: unknown_workflow_inpaint_lora_sampler_6
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.964583
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, Image To Mask, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo]
problems: []
missing: []
members: [图片生成/图生图/K老师_专属_去水印，去字幕，去模糊_2069077577020559362.json, 图片生成/图生图/YJ-ltx2.3去水印_2059470618550161409.json, 图片生成/图生图/全自动一键去水印+字幕+修复模糊+高清放大_2054218745601642497.json, 图片生成/图生图/去水印，去字幕（豆包水印去除)_2072800070940053506.json, 图片生成/文生图/LTX2.3-ICEdit-Insight去水印+去字幕_2073320595470770178.json, 图片生成/文生图/LTX2.3-ICEdit-Insight去水印_去字幕_去模糊_高清化_2073320398938267649.json, 图片生成/文生图/去模糊，高清LTX2.3_iclora_insight工作流_2057411893463179265.json, 图片生成/文生图/四合一去水印_字幕_修复模糊_高清放大_2057406073866379265.json, 图片生成/文生图/视频全自动一键去水印_字幕_修复模糊_高清放大全自动一键去水印_字幕_修复模糊_高清放大_2068564459328729090.json, 数字人/数字人/LTX2.3 iclora insight去水印去字幕高清_2053717870206562305.json, 数字人/数字人/去水印去字幕，去模糊，视频高清　　LTX2.3 Ｉclora Ｉnsight　极速_2054063768077914113.json, 数字人/数字人/多功能，去水印去字幕，去模糊，视频高清，　Iclora －insight   Ltx2.3_2054087077058359298.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/K老师_专属_去水印，去字幕，去模糊_2069077577020559362.json、图片生成/图生图/YJ-ltx2.3去水印_2059470618550161409.json、图片生成/图生图/全自动一键去水印+字幕+修复模糊+高清放大_2054218745601642497.json、图片生成/图生图/去水印，去字幕（豆包水印去除)_2072800070940053506.json、图片生成/文生图/LTX2.3-ICEdit-Insight去水印+去字幕_2073320595470770178.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 10/12 个有
- `SimpleMath+` —— 10/12 个有
- `VHS_VideoCombine` —— 10/12 个有
- `VHS_VideoInfoLoaded` —— 10/12 个有
- `easy imageSize` —— 10/12 个有
- `Text Multiline` —— 9/12 个有
- `ImageConcatMulti` —— 6/12 个有
- `Fast Groups Bypasser (rgthree)` —— 5/12 个有
- `INTConstant` —— 3/12 个有
- `Bjornulf_CombineTexts` —— 2/12 个有
- `ComfyMathExpression` —— 2/12 个有
- `CreateVideo` —— 2/12 个有
- `GetImageSize` —— 2/12 个有
- `ImageBatchMulti` —— 2/12 个有
- `ImpactSwitch` —— 2/12 个有
- `Int` —— 2/12 个有
- `LTXVAudioVAEDecode` —— 2/12 个有
- `PrimitiveInt` —— 2/12 个有
- `SaveVideo` —— 2/12 个有
- `ShowAnything|Mie` —— 2/12 个有
- `VHS_VideoInfo` —— 2/12 个有
- `BatchImagesNode` —— 1/12 个有
- `CR String To Combo` —— 1/12 个有
- `ImpactStringSelector` —— 1/12 个有
- `LoadVideoUI` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `PlaySound|pysssss` —— 1/12 个有
- `RIFE VFI` —— 1/12 个有
- `SplitStringByDelimiter` —— 1/12 个有
- `VAEDecode` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

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
