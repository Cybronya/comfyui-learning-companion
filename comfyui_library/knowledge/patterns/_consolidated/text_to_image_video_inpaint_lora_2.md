---
name: text_to_image_video_inpaint_lora_2
type: Text To Image
frequency: 5
level: strong
coverage: 0.9026
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, GetImageRangeFromBatch, Image To Mask, ImageConcatMulti, JjkText, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeForInpaint, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/LTX2.3视频去模糊高清放大｜iclora insight加持，画面细节全面还原_2107289339876171777.json, 视频生成/图生视频/LTX 2.3 iClora Insight视频去水印去字幕处理工作流_2102535340480360450.json, 视频生成/图生视频/LTX2.3免费去字幕去水印V1｜画面尺寸不变无痕清除，视频净化利器_2107467310356324353.json, 视频生成/图生视频/LTX2.3视频去模糊高清放大｜iclora_insight加持，画面细节全面还原_2107468474674147330.json, 视频生成/图生视频/去水印去字幕｜LTX2.3 iclora insight视频处理_2090917192840863746.json]
source: knowledge_consolidation
---

# text_to_image_video_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/LTX2.3视频去模糊高清放大｜iclora insight加持，画面细节全面还原_2107289339876171777.json、视频生成/图生视频/LTX 2.3 iClora Insight视频去水印去字幕处理工作流_2102535340480360450.json、视频生成/图生视频/LTX2.3免费去字幕去水印V1｜画面尺寸不变无痕清除，视频净化利器_2107467310356324353.json、视频生成/图生视频/LTX2.3视频去模糊高清放大｜iclora_insight加持，画面细节全面还原_2107468474674147330.json、视频生成/图生视频/去水印去字幕｜LTX2.3 iclora insight视频处理_2090917192840863746.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Text Multiline` —— 4/5 个有
- `easy imageSize` —— 4/5 个有
- `孤海注释` —— 3/5 个有
- `EmptyImage` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `ComfyMathExpression` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `ToInt` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
