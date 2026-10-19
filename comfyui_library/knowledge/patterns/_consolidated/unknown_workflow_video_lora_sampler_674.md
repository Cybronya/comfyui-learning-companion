---
name: unknown_workflow_video_lora_sampler_674
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.979333
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/单图生视频_2083552023793979393.json, 视频生成/图生视频/2033358933443747841.json, 视频生成/图生视频/2023806370599931905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_674

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/单图生视频_2083552023793979393.json、视频生成/图生视频/2033358933443747841.json、视频生成/图生视频/2023806370599931905.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `WanVideoSampler` —— 1/3 个有
- `WanVideoTeaCache` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 14 | 3 | 36% |
| 采样算法 | 1 | 1 - 1.1 | 3 | 95% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 14，3 个样本，取值分散，一致性仅 36%
- 采样算法 中位数 1，观测区间 1 - 1.1，3 个样本，取值集中（一致性 95%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
