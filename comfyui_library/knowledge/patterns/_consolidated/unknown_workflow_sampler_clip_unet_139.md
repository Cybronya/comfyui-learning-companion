---
name: unknown_workflow_sampler_clip_unet_139
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.838111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 文生图8步官方版+中文教程_1955564286744543234.json, 图片生成/文生图/Qwen Image 文生图官方版+中文教程+水印去除处理_1955432929541459969.json, 图片生成/文生图/Qwen Image 文生图，海报设计_1987149238826151938.json, 图片生成/文生图/Qwen Image+双Lora文生图- 双K采样器版本_1955600731353989122.json, 图片生成/文生图/Qwen Image-文生图-8步优化加速_1954817663203721218.json, 图片生成/文生图/Qwen-Image基础工作流_1954423623698280449.json, 图片生成/文生图/Qwen-image 文生图lora版-极致美感_1991719726550298625.json, 图片生成/文生图/【官版】Qwen Image-8步优化加速-增加宽高参数版本_1961085397939982338.json, 图片生成/文生图/【官版】Qwen Image-8步优化加速_1954222888989683714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_139

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Qwen Image 文生图8步官方版+中文教程_1955564286744543234.json、图片生成/文生图/Qwen Image 文生图官方版+中文教程+水印去除处理_1955432929541459969.json、图片生成/文生图/Qwen Image 文生图，海报设计_1987149238826151938.json、图片生成/文生图/Qwen Image+双Lora文生图- 双K采样器版本_1955600731353989122.json、图片生成/文生图/Qwen Image-文生图-8步优化加速_1954817663203721218.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
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
- `PreviewImage` —— 8/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `LayerUtility: ImageReel` —— 3/9 个有
- `LayerUtility: ImageReelComposit` —— 3/9 个有
- `CR Aspect Ratio` —— 2/9 个有
- `ImagePadKJ` —— 2/9 个有
- `JjkText` —— 2/9 个有
- `ImpactInt` —— 1/9 个有
- `Lora Loader Stack (rgthree)` —— 1/9 个有
- `LoraLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 30 | 9 | 44% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 9 | 45% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 30，9 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，9 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
