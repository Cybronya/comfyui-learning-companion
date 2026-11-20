---
name: unknown_workflow_lora_sampler_clip_238
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.970333
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/一种借助wan2.2模型使用首尾帧生成补间视频的工作流_2073397315003572225.json, 视频生成/文生视频/【阡陌】wan2.2 GGUF+light4步加速lora文生视频工作流_1967793949974867969.json, 视频生成/文生视频/【阡陌】wan2.2+light4步加速lora文生视频工作流_1967560743048581122.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_238

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/一种借助wan2.2模型使用首尾帧生成补间视频的工作流_2073397315003572225.json、视频生成/文生视频/【阡陌】wan2.2 GGUF+light4步加速lora文生视频工作流_1967793949974867969.json、视频生成/文生视频/【阡陌】wan2.2+light4步加速lora文生视频工作流_1967560743048581122.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 2/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `CM_IntToNumber` —— 1/3 个有
- `Int` —— 1/3 个有
- `Number Multiple Of` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `WanFunInpaintToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
