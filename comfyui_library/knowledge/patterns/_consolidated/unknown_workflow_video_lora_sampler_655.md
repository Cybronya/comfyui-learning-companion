---
name: unknown_workflow_video_lora_sampler_655
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2005191583471468545.json, 视频生成/图生视频/1987781988037931010.json, 视频生成/图生视频/1980678850906603522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_655

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2005191583471468545.json、视频生成/图生视频/1987781988037931010.json、视频生成/图生视频/1980678850906603522.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `WanFirstLastFrameToVideo` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `WanFourFrameReferenceUltimate` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 5 | 4 - 8 | 3 | 70% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 8，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
