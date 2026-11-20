---
name: unknown_workflow_video_lora_sampler_485
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.937167
common_nodes: [BerniniConditioningReferenceSlots, CLIPLoader, CLIPTextEncode, CreateVideo, Evaluate Integers, GetImageRangeFromBatch, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, RHLLMChatNode, SimpleMath+, Text, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanContextWindowsManual]
problems: []
missing: []
members: [平台全量/Bernini-视频去水印字幕_2080471697173602306.json, 平台全量/bernini全能视频编辑  提示词自动反推版_2078123633691684866.json, 平台全量/bernini视频编辑_2080476205601607682.json, 平台全量/超强bernini一键去除字幕水印 ！14b满血版_2074508004959023106.json, 平台全量/超快速bernini一键去除字幕水印 ！_2063549104537563137.json, 平台全量/超快速bernini一键去除字幕水印 ！_2073345710306902016.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_485

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Bernini-视频去水印字幕_2080471697173602306.json、平台全量/bernini全能视频编辑  提示词自动反推版_2078123633691684866.json、平台全量/bernini视频编辑_2080476205601607682.json、平台全量/超强bernini一键去除字幕水印 ！14b满血版_2074508004959023106.json、平台全量/超快速bernini一键去除字幕水印 ！_2063549104537563137.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `BerniniConditioningReferenceSlots`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `Evaluate Integers`
- `GetImageRangeFromBatch`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `RHLLMChatNode`
- `SimpleMath+`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanContextWindowsManual`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 4/6 个有
- `Seed (rgthree)` —— 4/6 个有
- `BerniniPromptEnhancer` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `StringFunction|pysssss` —— 2/6 个有
- `TTResolutionSelector` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
