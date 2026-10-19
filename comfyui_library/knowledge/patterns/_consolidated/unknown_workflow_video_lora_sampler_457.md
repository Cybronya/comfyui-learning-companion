---
name: unknown_workflow_video_lora_sampler_457
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8096
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/文生视频/1954421837595865089.json, 视频生成/文生视频/video_wan2_2_14B_Smooth Mix_1980199127709552641.json, 视频生成/文生视频/1966051284912607234.json, 视频生成/文生视频/1952546698105163778.json, 视频生成/文生视频/1952688713274953729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_457

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/1954421837595865089.json、视频生成/文生视频/video_wan2_2_14B_Smooth Mix_1980199127709552641.json、视频生成/文生视频/1966051284912607234.json、视频生成/文生视频/1952546698105163778.json、视频生成/文生视频/1952688713274953729.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `UnetLoaderGGUF` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `HunyuanImageToVideo` —— 1/5 个有
- `ShellAgentPluginInputImage` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 5 | 89% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，5 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
