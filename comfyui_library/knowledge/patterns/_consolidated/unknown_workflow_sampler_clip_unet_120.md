---
name: unknown_workflow_sampler_clip_unet_120
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.836182
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 文生图8步官方版+中文教程_1955564286744543234.json, 图片生成/文生图/Qwen Image 文生图官方版+中文教程+水印去除处理_1955432929541459969.json, 图片生成/文生图/Qwen Image 文生图，海报设计_1987149238826151938.json, 图片生成/文生图/Qwen Image-文生图-8步优化加速_1954817663203721218.json, 图片生成/文生图/Qwen Image文生图V1（QQ动漫版风格）_1954798087374987266.json, 图片生成/文生图/Qwen Image文生图V1（贞贞LORA版2500步）_1953815517956112386.json, 图片生成/文生图/Qwen Image，文生图 + Lora（人物写实）_1987158769756999681.json, 图片生成/文生图/Qwen image pruning——权重瘦身版_2073209712295899137.json, 图片生成/文生图/Qwen 文生图(二次元)_2057795247358435330.json, 图片生成/文生图/Qwen-Image-2512基础文生图 T2I_2065613919451963393.json, 图片生成/文生图/Qwen-Image-2512基础文生图 T2I_2076908888892469249.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_120

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Qwen Image 文生图8步官方版+中文教程_1955564286744543234.json、图片生成/文生图/Qwen Image 文生图官方版+中文教程+水印去除处理_1955432929541459969.json、图片生成/文生图/Qwen Image 文生图，海报设计_1987149238826151938.json、图片生成/文生图/Qwen Image-文生图-8步优化加速_1954817663203721218.json、图片生成/文生图/Qwen Image文生图V1（QQ动漫版风格）_1954798087374987266.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/11 个有
- `PreviewImage` —— 5/11 个有
- `Text` —— 3/11 个有
- `CR Aspect Ratio` —— 2/11 个有
- `GetNode` —— 2/11 个有
- `ImagePadKJ` —— 2/11 个有
- `Int` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `LayerUtility: TextJoin` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 20 | 11 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 11 | 46% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 20，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，11 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（7/11 个样本）：Steps较低可能导致细节不足
