---
name: unknown_workflow_video_inpaint_lora_3
type: Unknown Workflow
frequency: 25
level: strong
coverage: 0.92064
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, ManualSigmas, RandomNoise, RepeatImageBatch, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/0917修复一键视频去字幕+自动删除水印_2055479255714279425.json, 平台全量/IC Edit去水印字幕_2057705781973311489.json, 平台全量/K老师_专属_去水印，去字幕，去模糊_2065370917630472193.json, 平台全量/LTX-2.3-100%视频去水印_2054126422163247105.json, 平台全量/LTX-2.3-ICLORA 去短视频平台水印V1_2053695689246420994.json, 平台全量/LTX-2.3-ICLORA 应用去字幕+_2067423300111912961.json, 平台全量/LTX-2.3-ICLORA剃胡子+自动优化提示词版V1_2067550088351797250.json, 平台全量/LTX-2.3-ICLORA多参生视频+自动优化提示词版V1_2067543864751255553.json, 平台全量/LTX-2.3-ICLORA玩水+自动优化提示词版V1_2067550997978902530.json, 平台全量/LTX-2.3-ICLORA白天变黑夜+自动优化提示词版V1_2067535158579912706.json, 平台全量/LTX-2.3-ICLORA视频上色+自动优化提示词版V1_2067520572413792258.json, 平台全量/LTX-2.3-ICLORA视频修复V1_2053692292787122178.json, 平台全量/LTX-2.3-ICLORA视频去伪影+自动优化提示词版V1_2067540864875978754.json, 平台全量/LTX-2.3-ICLORA视频去字幕V1_2053696025675743233.json, 平台全量/LTX-2.3-ICLORA视频去模糊+自动优化提示词版V1_2067536587910639617.json, 平台全量/LTX-2.3-ICLORA视频高清化V1+全节点注释_2053719967635390465.json, 平台全量/LTX-2.3-ICLORA视频高清化V1_2053696033393262593.json, 平台全量/LTX-2.3-ICLORA进阶应用去字幕+水印V1(高质量版)_2053718417894592514.json, 平台全量/LTX-2.3-IClora_视频去水印_字幕_2053714608061464578.json, 平台全量/LTX-2.3-IClora_视频模糊修复+高清增强_2053795447445172226.json, 平台全量/LTX-2.3-免费去字幕去水印-画面尺寸不变-V1_2081196419028963330.json, 平台全量/LTX-2.3-去字幕去水印2_2091448171368116225.json, 平台全量/LTX2.3_去字幕_去水印_模糊变高清_视频高清_2054125837057830914.json, 平台全量/LTX2.3_去字幕_去水印_模糊变高清_视频高清_2054474343786270721.json, 平台全量/LTX2.3全自动一键去水印 _ 字幕 _ 修复模糊 _ 高清放大全面优化解决开头水印残留_2054917620780019714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_3

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（平台全量/0917修复一键视频去字幕+自动删除水印_2055479255714279425.json、平台全量/IC Edit去水印字幕_2057705781973311489.json、平台全量/K老师_专属_去水印，去字幕，去模糊_2065370917630472193.json、平台全量/LTX-2.3-100%视频去水印_2054126422163247105.json、平台全量/LTX-2.3-ICLORA 去短视频平台水印V1_2053695689246420994.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 25 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
- `KSamplerSelect`
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
- `ManualSigmas`
- `RandomNoise`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTX2SamplingPreviewOverride` —— 24/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 24/25 个有
- `LoraLoaderModelOnly` —— 24/25 个有
- `PathchSageAttentionKJ` —— 24/25 个有
- `Image To Mask` —— 23/25 个有
- `ResizeImageMaskNode` —— 23/25 个有
- `Seed (rgthree)` —— 23/25 个有
- `VHS_VideoInfoLoaded` —— 23/25 个有
- `easy imageSize` —— 22/25 个有
- `CR Prompt Text` —— 14/25 个有
- `ImageConcanate` —— 14/25 个有
- `easy showAnything` —— 10/25 个有
- `CreateVideo` —— 7/25 个有
- `RHLLMChatNode` —— 7/25 个有
- `Text Multiline` —— 5/25 个有
- `INTConstant` —— 4/25 个有
- `ImageBatchMulti` —— 4/25 个有
- `Fast Groups Bypasser (rgthree)` —— 3/25 个有
- `GetNode` —— 3/25 个有
- `ImageConcatMulti` —— 3/25 个有
- `LoadImage` —— 3/25 个有
- `SetNode` —— 3/25 个有
- `ToInt` —— 3/25 个有
- `ComfyMathExpression` —— 2/25 个有
- `GetImageSize` —— 2/25 个有
- `ImageResizeKJv2` —— 2/25 个有
- `ImageToMask` —— 2/25 个有
- `PrimitiveStringMultiline` —— 2/25 个有
- `Float` —— 1/25 个有
- `MathExpression|pysssss` —— 1/25 个有
- `PreviewImage` —— 1/25 个有
- `PrimitiveFloat` —— 1/25 个有
- `TextCombinerSix` —— 1/25 个有
- `easy imageCount` —— 1/25 个有
- `ttN int` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 25 | 100% |
| 高度 | 25 | 25 - 25 | 25 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，25 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，25 个样本，取值集中（一致性 100%）
