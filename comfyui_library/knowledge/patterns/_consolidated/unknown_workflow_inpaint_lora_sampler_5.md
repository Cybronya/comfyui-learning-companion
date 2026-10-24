---
name: unknown_workflow_inpaint_lora_sampler_5
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.968818
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, Image To Mask, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [图片生成/图生图/K老师_专属_去水印，去字幕，去模糊_2069077577020559362.json, 图片生成/图生图/YJ-ltx2.3去水印_2059470618550161409.json, 图片生成/图生图/全自动一键去水印+字幕+修复模糊+高清放大_2054218745601642497.json, 图片生成/图生图/去水印，去字幕（豆包水印去除)_2072800070940053506.json, 图片生成/文生图/LTX2.3-ICEdit-Insight去水印+去字幕_2073320595470770178.json, 图片生成/文生图/LTX2.3-ICEdit-Insight去水印_去字幕_去模糊_高清化_2073320398938267649.json, 图片生成/文生图/去模糊，高清LTX2.3_iclora_insight工作流_2057411893463179265.json, 图片生成/文生图/四合一去水印_字幕_修复模糊_高清放大_2057406073866379265.json, 图片生成/文生图/视频全自动一键去水印_字幕_修复模糊_高清放大全自动一键去水印_字幕_修复模糊_高清放大_2068564459328729090.json, 视频生成/图生视频/LTX-2.3-ICLORA斗鸡眼+自动优化提示词版V1_2067532074952781825.json, 视频生成/图生视频/LTX-2.3-ICLORA视频高清化+修复组合版V1_2053727074506035201.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/K老师_专属_去水印，去字幕，去模糊_2069077577020559362.json、图片生成/图生图/YJ-ltx2.3去水印_2059470618550161409.json、图片生成/图生图/全自动一键去水印+字幕+修复模糊+高清放大_2054218745601642497.json、图片生成/图生图/去水印，去字幕（豆包水印去除)_2072800070940053506.json、图片生成/文生图/LTX2.3-ICEdit-Insight去水印+去字幕_2073320595470770178.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
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
- `Seed (rgthree)` —— 9/11 个有
- `SimpleMath+` —— 9/11 个有
- `VHS_VideoCombine` —— 9/11 个有
- `easy imageSize` —— 9/11 个有
- `Text Multiline` —— 6/11 个有
- `ImageConcatMulti` —— 5/11 个有
- `CreateVideo` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `INTConstant` —— 3/11 个有
- `CR Prompt Text` —— 2/11 个有
- `ComfyMathExpression` —— 2/11 个有
- `GetImageSize` —— 2/11 个有
- `ImageConcanate` —— 2/11 个有
- `LTXVAudioVAEDecode` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `SaveVideo` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `BatchImagesNode` —— 1/11 个有
- `CR String To Combo` —— 1/11 个有
- `ImpactStringSelector` —— 1/11 个有
- `Int` —— 1/11 个有
- `MathExpression|pysssss` —— 1/11 个有
- `PlaySound|pysssss` —— 1/11 个有
- `RHLLMChatNode` —— 1/11 个有
- `RIFE VFI` —— 1/11 个有
- `SplitStringByDelimiter` —— 1/11 个有
- `VAEDecode` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 25 | 25 - 25 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
