---
name: unknown_workflow_lora_sampler_vae_18
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.569667
common_nodes: [CFGNorm, CLIPLoader, GetNode, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetNode, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWen-Edit-0509-一致性增强版-基础版_1971905241866235905.json, 图片生成/图生图/Qwen image edit 2509plus人物换姿态、换装_1971498602206019585.json, 图片生成/图生图/Qwen2509多图参考_1970783378930868225.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_18

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QWen-Edit-0509-一致性增强版-基础版_1971905241866235905.json、图片生成/图生图/Qwen image edit 2509plus人物换姿态、换装_1971498602206019585.json、图片生成/图生图/Qwen2509多图参考_1970783378930868225.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetNode`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `TextEncodeQwenImageEdit` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
