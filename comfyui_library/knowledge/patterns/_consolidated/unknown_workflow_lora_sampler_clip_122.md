---
name: unknown_workflow_lora_sampler_clip_122
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.935
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SimpleMath+, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_LoadVideo, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳_2050409773828452353.json, 平台全量/LTX-2.3_动作控制_2034291585524961281.json, 平台全量/图生视频--LTX-2.3_动作参考生视频 --深度-线条-姿势_2037757500941930497.json, 视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control_Distilled_2048943736339570690.json, 视频生成/图生视频/LTX-2.3_ICLoRA_outpaint_2044337798932598786.json, 视频生成/文生视频/LTX-2.3_ICLoRA_Union_Control_Distilled_2033749447833821185.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_122

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳_2050409773828452353.json、平台全量/LTX-2.3_动作控制_2034291585524961281.json、平台全量/图生视频--LTX-2.3_动作参考生视频 --深度-线条-姿势_2037757500941930497.json、视频生成/图生视频/LTX-2.3_ICLoRA_Union_Control_Distilled_2048943736339570690.json、视频生成/图生视频/LTX-2.3_ICLoRA_outpaint_2044337798932598786.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `CannyEdgePreprocessor` —— 4/6 个有
- `DWPreprocessor` —— 4/6 个有
- `DepthAnythingPreprocessor` —— 4/6 个有
- `PreviewAny` —— 4/6 个有
- `TextGenerateLTX2Prompt` —— 4/6 个有
- `CreateVideo` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `SaveVideo` —— 2/6 个有
- `CustomAddLabel` —— 1/6 个有
- `GetVideoComponents` —— 1/6 个有
- `Int` —— 1/6 个有
- `MultiTextConcatenate` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `TTResolutionSelector` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
