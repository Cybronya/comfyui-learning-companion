---
name: unknown_workflow_video_lora_sampler_521
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.97175
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, ImageResizeKJ, ImageResizeKJv2, ImpactInt, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/1955930393901977601.json, 视频生成/图生视频/1952583825614409730.json, 视频生成/图生视频/1953122188666802177.json, 视频生成/图生视频/1952542983688261634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_521

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1955930393901977601.json、视频生成/图生视频/1952583825614409730.json、视频生成/图生视频/1953122188666802177.json、视频生成/图生视频/1952542983688261634.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `JWStringConcat` —— 2/4 个有
- `PIP_StringConcatenation` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `TextConcat` —— 2/4 个有
- `Wan22PromptSelector` —— 2/4 个有
- `CreateVideo` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `PreViewVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
