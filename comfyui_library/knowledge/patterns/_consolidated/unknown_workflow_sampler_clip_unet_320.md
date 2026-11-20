---
name: unknown_workflow_sampler_clip_unet_320
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8365
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, KSampler, ModelSamplingAuraFlow, RH_LLMAPI_NODE, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QWen-Image中文字体直出（效果超过即梦+提示词自动优化版）_1954116380738109441.json, 图片生成/文生图/QWen-Image中文渲染+提示词扩写_1952923562652930050.json, 图片生成/文生图/QWen-bf16-Image表情包设计_1955835031454302210.json, 图片生成/文生图/【官版】Qwen Image-8步优化加速_1954798558370160641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_320

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/QWen-Image中文字体直出（效果超过即梦+提示词自动优化版）_1954116380738109441.json、图片生成/文生图/QWen-Image中文渲染+提示词扩写_1952923562652930050.json、图片生成/文生图/QWen-bf16-Image表情包设计_1955835031454302210.json、图片生成/文生图/【官版】Qwen Image-8步优化加速_1954798558370160641.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `TTP_text_mix` —— 3/4 个有
- `ImpactSwitch` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `QwenImageModelLoader` —— 1/4 个有
- `RH_QwenImageGenerator` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `string_util_StrReplace` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 4 | 57% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
