---
name: unknown_workflow_video_lora_sampler_527
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.955167
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJ, ImageResizeKJv2, ImpactInt, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 首尾帧 +自动扩词【官方极速版】v1_1955930393901977601.json, 视频生成/图生视频/wan2.2 首尾帧 极速版_1952583825614409730.json, 视频生成/图生视频/wan2.2 首尾帧视频 lightx2v 加速_1995400759510544385.json, 视频生成/图生视频/万相首尾帧_1953403463789150209.json, 视频生成/图生视频/官方万相wan2.2 首尾帧 极速版+自动扩词_1953122188666802177.json, 视频生成/图生视频/首尾帧生视频_自动提示词_1955867522656555010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_527

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 首尾帧 +自动扩词【官方极速版】v1_1955930393901977601.json、视频生成/图生视频/wan2.2 首尾帧 极速版_1952583825614409730.json、视频生成/图生视频/wan2.2 首尾帧视频 lightx2v 加速_1995400759510544385.json、视频生成/图生视频/万相首尾帧_1953403463789150209.json、视频生成/图生视频/官方万相wan2.2 首尾帧 极速版+自动扩词_1953122188666802177.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
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
- `CR Text` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 2/6 个有
- `JWStringConcat` —— 2/6 个有
- `PIP_StringConcatenation` —— 2/6 个有
- `RH_Captioner` —— 2/6 个有
- `TextConcat` —— 2/6 个有
- `Wan22PromptSelector` —— 2/6 个有
- `CreateVideo` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `Joy_caption_two` —— 1/6 个有
- `Joy_caption_two_load` —— 1/6 个有
- `LayerUtility: TextJoin` —— 1/6 个有
- `PreViewVideo` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 83% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | lcm | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
