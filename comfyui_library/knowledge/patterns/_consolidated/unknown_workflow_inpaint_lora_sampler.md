---
name: unknown_workflow_inpaint_lora_sampler
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.96775
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, Image To Mask, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3-ICEdit-Insight去水印+去字幕_2073320595470770178.json, 图片生成/文生图/LTX2.3-ICEdit-Insight去水印_去字幕_去模糊_高清化_2073320398938267649.json, 图片生成/文生图/去模糊，高清LTX2.3_iclora_insight工作流_2057411893463179265.json, 图片生成/文生图/四合一去水印_字幕_修复模糊_高清放大_2057406073866379265.json, 图片生成/文生图/视频全自动一键去水印_字幕_修复模糊_高清放大全自动一键去水印_字幕_修复模糊_高清放大_2068564459328729090.json, 视频生成/图生视频/2067532074952781825.json, 视频生成/图生视频/2053727074506035201.json, 视频生成/图生视频/一键去字幕水印去模糊_2094407100247134209.json, 视频生成/图生视频/2059081651447222274.json, 视频生成/图生视频/视频去水印，去字幕LTX2.3 iclora insight工作流_2054762008184147969.json, 视频生成/图生视频/2054733348798509058.json, 视频生成/图生视频/2054767077927473153.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/LTX2.3-ICEdit-Insight去水印+去字幕_2073320595470770178.json、图片生成/文生图/LTX2.3-ICEdit-Insight去水印_去字幕_去模糊_高清化_2073320398938267649.json、图片生成/文生图/去模糊，高清LTX2.3_iclora_insight工作流_2057411893463179265.json、图片生成/文生图/四合一去水印_字幕_修复模糊_高清放大_2057406073866379265.json、图片生成/文生图/视频全自动一键去水印_字幕_修复模糊_高清放大全自动一键去水印_字幕_修复模糊_高清放大_2068564459328729090.json…）

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
- `SimpleMath+` —— 10/12 个有
- `VHS_VideoCombine` —— 10/12 个有
- `easy imageSize` —— 10/12 个有
- `Seed (rgthree)` —— 8/12 个有
- `ImageConcatMulti` —— 7/12 个有
- `Text Multiline` —— 6/12 个有
- `Fast Groups Bypasser (rgthree)` —— 4/12 个有
- `INTConstant` —— 4/12 个有
- `CreateVideo` —— 3/12 个有
- `CR Prompt Text` —— 2/12 个有
- `ComfyMathExpression` —— 2/12 个有
- `GetImageSize` —— 2/12 个有
- `ImageConcanate` —— 2/12 个有
- `LTXVAudioVAEDecode` —— 2/12 个有
- `PrimitiveInt` —— 2/12 个有
- `SaveVideo` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `CR String To Combo` —— 1/12 个有
- `ImpactStringSelector` —— 1/12 个有
- `RHLLMChatNode` —— 1/12 个有
- `SplitStringByDelimiter` —— 1/12 个有

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
