---
name: unknown_workflow_sampler_clip_vae_24
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.933125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku-qwen image文生图_1965030044580069377.json, 图片生成/文生图/Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945.json, 图片生成/文生图/Nunchaku超级加速 Qwen Image文生图_1966409848168624130.json, 图片生成/文生图/Qwen Image封面生成-日拱一卒_1958095012225495041.json, 图片生成/文生图/Qwen Image文生图_1954799878556704770.json, 图片生成/文生图/Qwen image pruning——权重瘦身版_2073209712295899137.json, 图片生成/文生图/Qwen 文生图(二次元)_2057795247358435330.json, 图片生成/文生图/文生图-产品创意海报_2059206447187193858.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_24

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Nunchaku-qwen image文生图_1965030044580069377.json、图片生成/文生图/Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945.json、图片生成/文生图/Nunchaku超级加速 Qwen Image文生图_1966409848168624130.json、图片生成/文生图/Qwen Image封面生成-日拱一卒_1958095012225495041.json、图片生成/文生图/Qwen Image文生图_1954799878556704770.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 5/8 个有
- `JjkText` —— 4/8 个有
- `CFGNorm` —— 3/8 个有
- `LoadImage` —— 3/8 个有
- `NunchakuQwenImageDiTLoader` —— 3/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `Text` —— 2/8 个有
- `CR SDXL Aspect Ratio` —— 1/8 个有
- `LayerUtility: TextJoin` —— 1/8 个有
- `TextCombinerTwo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 8 | 59% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 8 | 67% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，8 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
