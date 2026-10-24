---
name: unknown_workflow_video_lora_sampler_682
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.889667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, CreateCFGScheduleFloatList, Fast Bypasser (rgthree), GetNode, ImageResizeKJv2, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, Primitive integer [Crystools], RHHiddenNodes, RIFE VFI, SetNode, SimpleMath+, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy getNode, easy setNode, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/球球抖动弹跳~TIPTOK引流专用_2028753060067020801.json, 视频生成/图生视频/球球抖动弹跳引流专用_1997167105533480961.json, 视频生成/图生视频/🦺【大炮擦边】球球抖动弹跳~TIPTOK引流专用_1990714282465779714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_682

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/球球抖动弹跳~TIPTOK引流专用_2028753060067020801.json、视频生成/图生视频/球球抖动弹跳引流专用_1997167105533480961.json、视频生成/图生视频/🦺【大炮擦边】球球抖动弹跳~TIPTOK引流专用_1990714282465779714.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CreateCFGScheduleFloatList`
- `Fast Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RIFE VFI`
- `SetNode`
- `SimpleMath+`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanMoeKSampler`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy getNode`
- `easy setNode`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | euler_ancestral | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，3 个样本，一致性 100%
