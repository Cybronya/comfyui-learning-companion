---
name: unknown_workflow_lora_sampler_clip_308
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4645
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, CreateVideo, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), GetNode, INTConstant, ImageResizeKJv2, ImpactSwitch, Int, InversionDemoLazyMixImages, Joy_caption_two_advanced, Joy_caption_two_load, Joy_extra_options, KSamplerAdvanced, LayerUtility: DeepSeekAPI, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RMBG, SaveVideo, SetNode, ShowText|pysssss, SolidColorBatched, TextInputNode, UNETLoader, VAEDecode, VAELoader, WanFirstLastFrameToVideo, WanSkipEndFrameImages_F2, easy cleanGpuUsed, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2-RemixV2-I2V完美循环工作流_2013492650959179778.json, 视频生成/图生视频/WAN2.2完美动画首尾循环，速度快，效果好_2049402530379075585.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_308

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WAN2.2-RemixV2-I2V完美循环工作流_2013492650959179778.json、视频生成/图生视频/WAN2.2完美动画首尾循环，速度快，效果好_2049402530379075585.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `Int`
- `InversionDemoLazyMixImages`
- `Joy_caption_two_advanced`
- `Joy_caption_two_load`
- `Joy_extra_options`
- `KSamplerAdvanced`
- `LayerUtility: DeepSeekAPI`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RMBG`
- `SaveVideo`
- `SetNode`
- `ShowText|pysssss`
- `SolidColorBatched`
- `TextInputNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanFirstLastFrameToVideo`
- `WanSkipEndFrameImages_F2`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
