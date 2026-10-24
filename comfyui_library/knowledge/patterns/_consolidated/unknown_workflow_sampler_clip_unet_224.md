---
name: unknown_workflow_sampler_clip_unet_224
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.843333
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QWen-Image 8步加速_1955523693487296514.json, 图片生成/文生图/QWen-Image8步加速中文渲染_1955336945507471361.json, 图片生成/文生图/QWen-Image中文字体直出（效果超过即梦+提示词自动优化版）_1954116380738109441.json, 图片生成/文生图/QWen-Image中文渲染+提示词扩写_1952923562652930050.json, 图片生成/文生图/QWen-bf16-Image表情包设计_1955835031454302210.json, 图片生成/文生图/【官版】Qwen Image-8步优化加速_1954798558370160641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_224

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/QWen-Image 8步加速_1955523693487296514.json、图片生成/文生图/QWen-Image8步加速中文渲染_1955336945507471361.json、图片生成/文生图/QWen-Image中文字体直出（效果超过即梦+提示词自动优化版）_1954116380738109441.json、图片生成/文生图/QWen-Image中文渲染+提示词扩写_1952923562652930050.json、图片生成/文生图/QWen-bf16-Image表情包设计_1955835031454302210.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/6 个有
- `RH_LLMAPI_NODE` —— 4/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `TTP_text_mix` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `ImpactSwitch` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `QwenImageModelLoader` —— 1/6 个有
- `RH_QwenImageGenerator` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `string_util_StrReplace` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 6 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 53% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
