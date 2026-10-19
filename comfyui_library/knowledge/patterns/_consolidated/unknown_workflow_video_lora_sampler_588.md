---
name: unknown_workflow_video_lora_sampler_588
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.965667
common_nodes: [BerniniStudio, CLIPLoader, Int, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2073592310989942786.json, 视频生成/图生视频/2073584193665331202.json, 视频生成/图生视频/2081973710835240961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_588

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2073592310989942786.json、视频生成/图生视频/2073584193665331202.json、视频生成/图生视频/2081973710835240961.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `BerniniStudio`
- `CLIPLoader`
- `Int`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyNumberConvert` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1.5 | 3 | 80% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1.5，3 个样本
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
