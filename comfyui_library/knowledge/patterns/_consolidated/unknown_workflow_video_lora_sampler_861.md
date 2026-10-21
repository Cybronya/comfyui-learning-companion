---
name: unknown_workflow_video_lora_sampler_861
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.564
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), FramePackFindNearestBucket, GetNode, ImageResize+, Int, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, SeedVR2, SetNode, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanImageToVideo, WanVideoNAG, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/1956043576671174657.json, 视频生成/图生视频/1957310369100394498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_861

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1956043576671174657.json、视频生成/图生视频/1957310369100394498.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `FramePackFindNearestBucket`
- `GetNode`
- `ImageResize+`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SeedVR2`
- `SetNode`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoNAG`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `StringReplace` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | uni_pc | - | 2 | 100% |
| 重绘幅度 | beta | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 uni_pc，2 个样本，一致性 100%
- 重绘幅度 最常用 beta，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
