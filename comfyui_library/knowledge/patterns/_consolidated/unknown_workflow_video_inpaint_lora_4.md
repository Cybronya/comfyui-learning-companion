---
name: unknown_workflow_video_inpaint_lora_4
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.896455
common_nodes: [CFGGuider, CLIPTextEncode, GetImageRangeFromBatch, Image To Mask, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy imageSize]
problems: []
missing: []
members: [平台全量/LTX-2.3-去字幕-去水印-去模糊-高清_2061293482291064833.json, 平台全量/LTX-2.3-高清修复_2055475041428615170.json, 平台全量/LTX2.3 -全自动视频一键去水印  _ 去字幕  _ 修复模糊 _ 高清放大_2054777044751396865.json, 平台全量/LTX2.3 -全自动视频一键去水印  _ 去字幕  _ 修复模糊 _ 高清放大_2055829743508959234.json, 平台全量/LTX2.3 -全自动视频一键去水印  _ 去字幕  _ 修复模糊 _ 高清放大_2056242378591264769.json, 平台全量/LTX2.3 -全自动视频一键去水印  _ 去字幕  _ 修复模糊 _ 高清放大_2056262522864496641.json, 平台全量/LTX2.3 -全自动视频一键去水印  _ 去字幕  _ 修复模糊 _ 高清放大_2079557924954923010.json, 平台全量/LTX2.3 -全自动视频一键去水印  _ 去字幕  _ 修复模糊 _ 高清放大_2087862839540281346.json, 平台全量/LTX2.3 一键去字幕_ 水印_修复模糊_高清放大_2054186745662590978.json, 平台全量/LTX2.3-全自动一键去水印+字幕+修复模糊+高清放大_2054198654357000194.json, 平台全量/LTX2.3-全自动一键去水印+字幕+修复模糊+高清放大_2054365102849175554.json, 平台全量/LTX2.3-全自动一键去水印+字幕+修复模糊+高清放大_2054489963667968001.json, 平台全量/LTX2.3-全自动视频一键去水印+去字幕+修复模糊+高清放大_2054412732757225473.json, 平台全量/LTX2.3LORA去除字幕工作流_2061689399418638338.json, 平台全量/LTX2.3去水印_2082402655921598465.json, 平台全量/LTX2.3去水印清除字幕 去水印，去字幕，去模糊 视频变高清 LTX2.3+iclora+insi_2055474102479147010.json, 平台全量/LTX2.3最强去字幕_去水印_视频高清_2054476144849760258.json, 平台全量/一键去字幕_水印_模糊修复_视频高清_2104084767720431618.json, 平台全量/一键去水印 _ 字幕_2058106991159107586.json, 平台全量/去水印_去字幕_去模糊_高清_2054049837154357250.json, 平台全量/四合一_全自动一键去_水印 _ 字幕 _ 修复模糊 _ 高清放大_2054118775930277890.json, 平台全量/漫剧 短视频 去水印（字幕）_2054143580117184513.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_4

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（平台全量/LTX-2.3-去字幕-去水印-去模糊-高清_2061293482291064833.json、平台全量/LTX-2.3-高清修复_2055475041428615170.json、平台全量/LTX2.3 -全自动视频一键去水印  _ 去字幕  _ 修复模糊 _ 高清放大_2054777044751396865.json、平台全量/LTX2.3 -全自动视频一键去水印  _ 去字幕  _ 修复模糊 _ 高清放大_2055829743508959234.json、平台全量/LTX2.3 -全自动视频一键去水印  _ 去字幕  _ 修复模糊 _ 高清放大_2056242378591264769.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 22 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `GetImageRangeFromBatch`
- `Image To Mask`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 21/22 个有
- `LTXAVTextEncoderLoader` —— 21/22 个有
- `LTXVAudioVAELoader` —— 21/22 个有
- `LoraLoaderModelOnly` —— 21/22 个有
- `Fast Groups Bypasser (rgthree)` —— 20/22 个有
- `Seed (rgthree)` —— 19/22 个有
- `Text Multiline` —— 19/22 个有
- `INTConstant` —— 17/22 个有
- `ImageConcatMulti` —— 17/22 个有
- `Int` —— 11/22 个有
- `easy anythingIndexSwitch` —— 10/22 个有
- `GetNode` —— 5/22 个有
- `SetNode` —— 5/22 个有
- `CR Prompt Text` —— 2/22 个有
- `DualCLIPLoader` —— 2/22 个有
- `LoadImage` —— 2/22 个有
- `UNETLoader` —— 2/22 个有
- `VAELoaderKJ` —— 2/22 个有
- `easy showAnything` —— 2/22 个有
- `EmptyLTXVLatentVideo` —— 1/22 个有
- `ImageConcanate` —— 1/22 个有
- `Label (rgthree)` —— 1/22 个有
- `PreviewAny` —— 1/22 个有
- `PrimitiveStringMultiline` —— 1/22 个有
- `Text` —— 1/22 个有
- `TextCombinerSix` —— 1/22 个有
- `easy getNode` —— 1/22 个有
- `easy promptList` —— 1/22 个有
- `easy setNode` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 22 | 100% |
| 高度 | 25 | 25 - 25 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，22 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，22 个样本，取值集中（一致性 100%）
