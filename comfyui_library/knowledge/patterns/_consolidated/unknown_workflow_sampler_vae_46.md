---
name: unknown_workflow_sampler_vae_46
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.94975
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2509多图参考API专用_1999488679565553665.json, 图片生成/图生图/【遇见AI】Qwen-image 文生图基础_2050874058291593218.json, 图片生成/图生图/千问Edit-指定区域编辑-qwen image Edit_1983058606935420929.json, 图片生成/图生图/👾怪獸-多姿态生成保持一致性👾_2046223752928698369.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_46

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen2509多图参考API专用_1999488679565553665.json、图片生成/图生图/【遇见AI】Qwen-image 文生图基础_2050874058291593218.json、图片生成/图生图/千问Edit-指定区域编辑-qwen image Edit_1983058606935420929.json、图片生成/图生图/👾怪獸-多姿态生成保持一致性👾_2046223752928698369.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `easy int` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `InpaintModelConditioning` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 40 | 4 | 18% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 40，4 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
