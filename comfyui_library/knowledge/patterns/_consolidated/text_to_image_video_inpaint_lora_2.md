---
name: text_to_image_video_inpaint_lora_2
type: Text To Image
frequency: 7
level: strong
coverage: 0.915286
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, GetImageRangeFromBatch, Image To Mask, ImageConcatMulti, JjkText, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeForInpaint, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/LTX2.3视频去模糊高清放大｜iclora insight加持，画面细节全面还原_2107289339876171777.json, 图片生成/图生图/视频去模糊高清放大LTX2.3工作流，视频超分高清增强工具_2107528652815687682.json, 平台全量/LTX2.3去水印去字幕｜去模糊高清视频处理工作流_2093771544567828482.json, 视频生成/图生视频/LTX 2.3 iClora Insight视频去水印去字幕处理工作流_2102535340480360450.json, 视频生成/图生视频/LTX2.3免费去字幕去水印V1｜画面尺寸不变无痕清除，视频净化利器_2107467310356324353.json, 视频生成/图生视频/LTX2.3视频去模糊高清放大｜iclora_insight加持，画面细节全面还原_2107468474674147330.json, 视频生成/图生视频/去水印去字幕｜LTX2.3 iclora insight视频处理_2090917192840863746.json]
source: knowledge_consolidation
---

# text_to_image_video_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/LTX2.3视频去模糊高清放大｜iclora insight加持，画面细节全面还原_2107289339876171777.json、图片生成/图生图/视频去模糊高清放大LTX2.3工作流，视频超分高清增强工具_2107528652815687682.json、平台全量/LTX2.3去水印去字幕｜去模糊高清视频处理工作流_2093771544567828482.json、视频生成/图生视频/LTX 2.3 iClora Insight视频去水印去字幕处理工作流_2102535340480360450.json、视频生成/图生视频/LTX2.3免费去字幕去水印V1｜画面尺寸不变无痕清除，视频净化利器_2107467310356324353.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `Image To Mask`
- `ImageConcatMulti`
- `JjkText`
- `KSampler`
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
- `Seed (rgthree)`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 6/7 个有
- `easy imageSize` —— 6/7 个有
- `孤海注释` —— 5/7 个有
- `EmptyImage` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `ComfyMathExpression` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `ImageBatchMulti` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `Int` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `ToInt` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
