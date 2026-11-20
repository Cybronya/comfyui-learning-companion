---
name: unknown_workflow_video_lora_sampler_973
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.932
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CM_FloatToInt, EmptyLTXVLatentVideo, FL_Switch, GetImageSize, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/LTX2.5 - CQ Enhancer lora video workflow V2.json_2100759147024310274.json, 数字人/数字人/LTX2.5 - CQ Enhancer lora video 视频高清修复放大工具-小宣喧-RH_2100842998178340866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_973

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX2.5 - CQ Enhancer lora video workflow V2.json_2100759147024310274.json、数字人/数字人/LTX2.5 - CQ Enhancer lora video 视频高清修复放大工具-小宣喧-RH_2100842998178340866.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `FL_Switch`
- `GetImageSize`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 1/2 个有
- `LG_Color_Match_V2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
