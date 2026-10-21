---
name: unknown_workflow_lora_sampler_clip_72
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9862
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveVideo, UNETLoader, VAEDecode, VAELoader, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1956947504362131458.json, 视频生成/图生视频/2053650114769637377.json, 视频生成/图生视频/2054459129242103809.json, 视频生成/图生视频/2046114491431133185.json, 视频生成/图生视频/2066869280796405762.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1956947504362131458.json、视频生成/图生视频/2053650114769637377.json、视频生成/图生视频/2054459129242103809.json、视频生成/图生视频/2046114491431133185.json、视频生成/图生视频/2066869280796405762.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
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
- `CFGZeroStar` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有
- `easy promptReplace` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 20 | 14 - 20 | 5 | 87% |
| 采样算法 | 3.5 | 1 - 3.5 | 5 | 67% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 14 - 20，5 个样本，取值集中（一致性 87%）
- 采样算法 中位数 3.5，观测区间 1 - 3.5，5 个样本
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
