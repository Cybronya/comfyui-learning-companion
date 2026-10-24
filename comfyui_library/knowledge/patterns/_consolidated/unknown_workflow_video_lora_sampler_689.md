---
name: unknown_workflow_video_lora_sampler_689
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.825
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, ImpactInt, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, wanBlockSwap]
problems: []
missing: []
members: [视频生成/文生视频/AI代码侠土豆-Wan2.2_SmoothMix_T2V_1979789891196325889.json, 视频生成/文生视频/Holo长视频生成 官方流 文生视频_1983758575547949058.json, 视频生成/文生视频/Holo长视频生成 官方流 文生视频_2045400394263699457.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_689

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/AI代码侠土豆-Wan2.2_SmoothMix_T2V_1979789891196325889.json、视频生成/文生视频/Holo长视频生成 官方流 文生视频_1983758575547949058.json、视频生成/文生视频/Holo长视频生成 官方流 文生视频_2045400394263699457.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `ImpactInt`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `EmptyHunyuanLatentVideo` —— 2/3 个有
- `Fast Bypasser (rgthree)` —— 2/3 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `WanImageToVideo` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 12 | 8 - 12 | 3 | 82% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | euler | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 12，观测区间 8 - 12，3 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，3 个样本，一致性 67%
