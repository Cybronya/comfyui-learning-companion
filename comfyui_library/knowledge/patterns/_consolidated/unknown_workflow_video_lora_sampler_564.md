---
name: unknown_workflow_video_lora_sampler_564
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.95525
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/文生视频/1954421837595865089.json, 视频生成/文生视频/1952546698105163778.json, 视频生成/文生视频/1952688713274953729.json, 视频生成/文生视频/1950503507558387713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_564

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1954421837595865089.json、视频生成/文生视频/1952546698105163778.json、视频生成/文生视频/1952688713274953729.json、视频生成/文生视频/1950503507558387713.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `HunyuanImageToVideo` —— 1/4 个有
- `ShellAgentPluginInputImage` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 50% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
