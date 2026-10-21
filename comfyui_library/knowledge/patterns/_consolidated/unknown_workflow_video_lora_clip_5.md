---
name: unknown_workflow_video_lora_clip_5
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.961667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1952189425302360065.json, 视频生成/图生视频/2010691930170068994.json, 视频生成/图生视频/1950720072086147074.json, 视频生成/图生视频/1995400759510544385.json, 视频生成/图生视频/1953403463789150209.json, 视频生成/图生视频/1955867522656555010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_5

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1952189425302360065.json、视频生成/图生视频/2010691930170068994.json、视频生成/图生视频/1950720072086147074.json、视频生成/图生视频/1995400759510544385.json、视频生成/图生视频/1953403463789150209.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `WanFirstLastFrameToVideo` —— 5/6 个有
- `WanVideoNAG` —— 4/6 个有
- `ImageResizeKJ` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `ImpactInt` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `ImageListToBatch+` —— 1/6 个有
- `Joy_caption_two` —— 1/6 个有
- `Joy_caption_two_load` —— 1/6 个有
- `LayerUtility: TextJoin` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `WanImageToVideo` —— 1/6 个有
- `WanMoeKSampler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 8 | 6 - 10 | 6 | 86% |
| 采样算法 | 1 | 1 - 3.5 | 6 | 34% |
| 调度器 | lcm | - | 6 | 67% |
| 重绘幅度 | simple | - | 6 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 10，6 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 调度器 最常用 lcm，6 个样本，一致性 67%
- 重绘幅度 最常用 simple，6 个样本，一致性 83%
