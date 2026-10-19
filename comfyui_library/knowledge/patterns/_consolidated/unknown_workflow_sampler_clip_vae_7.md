---
name: unknown_workflow_sampler_clip_vae_7
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.939857
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR SDXL Aspect Ratio, StringFunction|pysssss]
members: [图片生成/文生图/1955880153337483265.json, 图片生成/文生图/1963484613191749634.json, 图片生成/文生图/1965257014656028674.json, 图片生成/文生图/1966317820562878466.json, 图片生成/文生图/1966728561858162689.json, 图片生成/文生图/1967210141957361665.json, 图片生成/文生图/1967455683580923905.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_7

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1955880153337483265.json、图片生成/文生图/1963484613191749634.json、图片生成/文生图/1965257014656028674.json、图片生成/文生图/1966317820562878466.json、图片生成/文生图/1966728561858162689.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `EmptySD3LatentImage` —— 5/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `EmptyHunyuanLatentVideo` —— 1/7 个有
- `ShellAgentPluginInputText` —— 1/7 个有
- `ShellAgentPluginSaveImage` —— 1/7 个有
- `StringFunction|pysssss` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 7 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 38% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，7 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR SDXL Aspect Ratio、StringFunction|pysssss
