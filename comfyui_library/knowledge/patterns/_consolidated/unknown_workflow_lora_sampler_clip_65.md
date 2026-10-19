---
name: unknown_workflow_lora_sampler_clip_65
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.98075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/文生视频工作流_2066457517043044354.json, 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2053378746035515394.json, 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json, 视频生成/文生视频/1949836969900687362.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_65

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/文生视频工作流_2066457517043044354.json、视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2053378746035515394.json、视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json、视频生成/文生视频/1949836969900687362.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `Int` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 5 | 4 - 9 | 4 | 64% |
| 采样算法 | 1 | 1 - 3.5 | 4 | 33% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 9，4 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
