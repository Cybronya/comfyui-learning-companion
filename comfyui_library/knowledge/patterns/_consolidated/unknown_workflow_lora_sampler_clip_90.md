---
name: unknown_workflow_lora_sampler_clip_90
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.977
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveVideo, UNETLoader, VAEDecode, VAELoader, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1956947504362131458.json, 视频生成/图生视频/1957799142709100545.json, 视频生成/图生视频/1968502067780300801.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_90

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1956947504362131458.json、视频生成/图生视频/1957799142709100545.json、视频生成/图生视频/1968502067780300801.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有
- `easy promptReplace` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 4 - 14 | 3 | 53% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 14，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
