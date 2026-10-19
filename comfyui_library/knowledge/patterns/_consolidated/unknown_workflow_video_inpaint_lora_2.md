---
name: unknown_workflow_video_inpaint_lora_2
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9696
common_nodes: [CFGGuider, CLIPTextEncode, GetImageRangeFromBatch, Image To Mask, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ColorImage, ManualSigmas, PathchSageAttentionKJ, RandomNoise, RepeatImageBatch, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VAEEncodeForInpaint, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2053854443006898178.json, 视频生成/图生视频/2042927263661957121.json, 视频生成/图生视频/2054757647898955778.json, 视频生成/图生视频/视频去水印，去字幕LTX2.3 iclora insight工作流_2054762008184147969.json, 视频生成/图生视频/2054733348798509058.json, 视频生成/图生视频/2054767077927473153.json, 视频生成/文生视频/IC Edit去水印字幕_2054546081706463234.json, 视频生成/文生视频/IC Edit高清修复_2054546073984749570.json, 视频生成/文生视频/豆包视频去水印_2060846914807091201.json, 视频生成/文生视频/豆包视频去水印_全屏去水印_2091189802585649154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2053854443006898178.json、视频生成/图生视频/2042927263661957121.json、视频生成/图生视频/2054757647898955778.json、视频生成/图生视频/视频去水印，去字幕LTX2.3 iclora insight工作流_2054762008184147969.json、视频生成/图生视频/2054733348798509058.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `GetImageRangeFromBatch`
- `Image To Mask`
- `KSamplerSelect`
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
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAEEncodeForInpaint`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 8/10 个有
- `LTX2SamplingPreviewOverride` —— 8/10 个有
- `LTXAVTextEncoderLoader` —— 8/10 个有
- `LTXVAudioVAELoader` —— 8/10 个有
- `ResizeImageMaskNode` —— 8/10 个有
- `VHS_VideoInfoLoaded` —— 8/10 个有
- `easy imageSize` —— 8/10 个有
- `ImageConcatMulti` —— 6/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `Seed (rgthree)` —— 5/10 个有
- `Text Multiline` —— 3/10 个有
- `ComfyMathExpression` —— 2/10 个有
- `DualCLIPLoader` —— 2/10 个有
- `GetImageSize` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `UNETLoader` —— 2/10 个有
- `VAELoaderKJ` —— 2/10 个有
- `easy imageCount` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `image_scale_pixel_v2` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
