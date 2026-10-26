---
name: unknown_workflow_video_lora_sampler_518
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9558
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/wan2.1文生视频官流【教学】_2001221263462891522.json, 视频生成/文生视频/【老金驿站】WAN8步电影级高清视频生成工作流_1933119779811012610.json, 视频生成/文生视频/文生视频 一分钟_2044216919120678914.json, 视频生成/文生视频/文生视频_2008504212048580610.json, 视频生成/文生视频/文生视频_2041095418389471234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_518

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/wan2.1文生视频官流【教学】_2001221263462891522.json、视频生成/文生视频/【老金驿站】WAN8步电影级高清视频生成工作流_1933119779811012610.json、视频生成/文生视频/文生视频 一分钟_2044216919120678914.json、视频生成/文生视频/文生视频_2008504212048580610.json、视频生成/文生视频/文生视频_2041095418389471234.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ApplySageAttention` —— 4/5 个有
- `TeaCache` —— 3/5 个有
- `wanBlock_Swap` —— 3/5 个有
- `Int` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 5 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，5 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
