---
name: unknown_workflow_lora_sampler_clip_73
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9788
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2041411003677679618.json, 视频生成/图生视频/2076552090461229058.json, 视频生成/图生视频/2000831805769084930.json, 视频生成/图生视频/1968555612659437570.json, 视频生成/文生视频/1968491886845546497.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2041411003677679618.json、视频生成/图生视频/2076552090461229058.json、视频生成/图生视频/2000831805769084930.json、视频生成/图生视频/1968555612659437570.json、视频生成/文生视频/1968491886845546497.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 4/5 个有
- `WanFirstLastFrameToVideo` —— 4/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `ModelPatchTorchSettings` —— 2/5 个有
- `EmptyHunyuanLatentVideo` —— 1/5 个有
- `ImpactFloat` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `VAEDecodeTiled` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
