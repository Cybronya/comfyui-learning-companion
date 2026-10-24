---
name: text_to_image_sampler_clip_checkpoint_19
type: Text To Image
frequency: 4
level: moderate
coverage: 0.8005
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/中文提示词文生图工作流_2046093591214297090.json, 图片生成/文生图/中西合璧古典美人一键生成_1889372369155448834.json, 图片生成/文生图/工作流基础篇-2-文生图带翻译工作流（翻译Alek节点）_2012411720182013954.json, 图片生成/文生图/文生图（翻译Alek节点）_1946045185828548610.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_19

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/中文提示词文生图工作流_2046093591214297090.json、图片生成/文生图/中西合璧古典美人一键生成_1889372369155448834.json、图片生成/文生图/工作流基础篇-2-文生图带翻译工作流（翻译Alek节点）_2012411720182013954.json、图片生成/文生图/文生图（翻译Alek节点）_1946045185828548610.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 3/4 个有
- `DeepTranslatorTextNode` —— 2/4 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `JoinStrings` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 640 | 512 - 1024 | 4 | 70% |
| 高度 | 768 | 512 - 1024 | 4 | 67% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 5.5 - 8 | 4 | 85% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 640，观测区间 512 - 1024，4 个样本
- 高度 中位数 768，观测区间 512 - 1024，4 个样本
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 5.5 - 8，4 个样本，取值集中（一致性 85%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
