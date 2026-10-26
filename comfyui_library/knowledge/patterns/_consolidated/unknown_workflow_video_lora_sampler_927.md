---
name: unknown_workflow_video_lora_sampler_927
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5285
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, CustomAddLabel, Float, GetNode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_Pro_Node, SetNode, ShowText, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoNAG, easy anythingIndexSwitch]
problems: []
missing: []
members: [视频生成/图生视频/video_wan2_2_14B_i2v_高动态_根据时长_自动结构化提示词_2014690276282998786.json, 视频生成/图生视频/video_wan2_2_14B_i2v_高动态_自动提示词_2013261998393397250.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_927

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/video_wan2_2_14B_i2v_高动态_根据时长_自动结构化提示词_2014690276282998786.json、视频生成/图生视频/video_wan2_2_14B_i2v_高动态_自动提示词_2013261998393397250.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CustomAddLabel`
- `Float`
- `GetNode`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_Pro_Node`
- `SetNode`
- `ShowText`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoNAG`
- `easy anythingIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 1/2 个有
- `MultiTextConcatenate` —— 1/2 个有
- `RH_Utils` —— 1/2 个有
- `Text` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | lcm | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
