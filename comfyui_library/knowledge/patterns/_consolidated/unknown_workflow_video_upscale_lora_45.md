---
name: unknown_workflow_video_upscale_lora_45
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.97
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Integer, EmptyHunyuanLatentVideo, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, ModelPatchTorchSettings, MuyeTextEditOutput, PathchSageAttentionKJ, RH_LLMAPI_NODE, SaveImage, SimpleMath+, Text Multiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy getNode, easy setNode, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/wan2.2自动提示词-文生视频+文生图加速版14B-fp8_2072970189112700930.json, 视频生成/文生视频/wan2.2自动提示词-文生视频+文生图极速版_1998605787012431874.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_45

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/wan2.2自动提示词-文生视频+文生图加速版14B-fp8_2072970189112700930.json、视频生成/文生视频/wan2.2自动提示词-文生视频+文生图极速版_1998605787012431874.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Integer`
- `EmptyHunyuanLatentVideo`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `MuyeTextEditOutput`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SimpleMath+`
- `Text Multiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `easy getNode`
- `easy setNode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | euler | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，2 个样本，一致性 100%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
