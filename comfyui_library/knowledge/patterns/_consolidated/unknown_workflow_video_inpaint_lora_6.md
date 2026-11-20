---
name: unknown_workflow_video_inpaint_lora_6
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.97925
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, GetImageRangeFromBatch, Image To Mask, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, SamplerCustomAdvanced, Seed (rgthree), SimpleMath+, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine, easy imageSize]
problems: []
missing: []
members: [视频生成/文生视频/IC Edit去水印字幕_2054546081706463234.json, 视频生成/文生视频/IC Edit高清修复_2054546073984749570.json, 视频生成/文生视频/豆包视频去水印_2060846914807091201.json, 视频生成/文生视频/豆包视频去水印_全屏去水印_2091189802585649154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/IC Edit去水印字幕_2054546081706463234.json、视频生成/文生视频/IC Edit高清修复_2054546073984749570.json、视频生成/文生视频/豆包视频去水印_2060846914807091201.json、视频生成/文生视频/豆包视频去水印_全屏去水印_2091189802585649154.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
- `Image To Mask`
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
- `PathchSageAttentionKJ`
- `RandomNoise`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 2/4 个有
- `LTX2SamplingPreviewOverride` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `VHS_VideoInfoLoaded` —— 2/4 个有
- `easy imageCount` —— 2/4 个有
- `image_scale_pixel_v2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
