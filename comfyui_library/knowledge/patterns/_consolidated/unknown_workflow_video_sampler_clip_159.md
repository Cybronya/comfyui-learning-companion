---
name: unknown_workflow_video_sampler_clip_159
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.9015
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/QwenVL视频反推提示词_文生视频_Comfyui官方流_1983421247163932674.json, 视频生成/文生视频/1950043620181237761.json, 视频生成/文生视频/1949879786422362114.json, 视频生成/文生视频/1949911446906912770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_159

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/QwenVL视频反推提示词_文生视频_Comfyui官方流_1983421247163932674.json、视频生成/文生视频/1950043620181237761.json、视频生成/文生视频/1949879786422362114.json、视频生成/文生视频/1949911446906912770.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `TeaCache` —— 2/4 个有
- `JjkText` —— 1/4 个有
- `MultiplePathsInput` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `VideoLoader` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 50% |
| Prompt 约束强度(CFG) | 14 | 8 - 20 | 4 | 57% |
| 采样算法 | 2.25 | 1 - 3.5 | 4 | 44% |
| 调度器 | euler | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 14，观测区间 8 - 20，4 个样本
- 采样算法 中位数 2.25，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 44%
- 调度器 最常用 euler，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
