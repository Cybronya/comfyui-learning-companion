---
name: unknown_workflow_video_lora_sampler_898
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.958
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, CR Text, Fast Groups Muter (rgthree), ImageResizeKJ, ImageResizeKJv2, ImpactInt, JWStringConcat, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PIP_StringConcatenation, PathchSageAttentionKJ, RH_Captioner, RH_LLMAPI_NODE, SimpleMath+, TextConcat, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, Wan22PromptSelector, WanFirstLastFrameToVideo, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 首尾帧 +自动扩词【官方极速版】v1_1955930393901977601.json, 视频生成/图生视频/官方万相wan2.2 首尾帧 极速版+自动扩词_1953122188666802177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_898

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 首尾帧 +自动扩词【官方极速版】v1_1955930393901977601.json、视频生成/图生视频/官方万相wan2.2 首尾帧 极速版+自动扩词_1953122188666802177.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CR Text`
- `Fast Groups Muter (rgthree)`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImpactInt`
- `JWStringConcat`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PIP_StringConcatenation`
- `PathchSageAttentionKJ`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `SimpleMath+`
- `TextConcat`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanFirstLastFrameToVideo`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `PreViewVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | lcm | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
