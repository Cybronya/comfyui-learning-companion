---
name: unknown_workflow_lora_sampler_unet_117
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.917
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/服装提取qwen edit 2511_2087714207843311617.json, 图片生成/图生图/服装试穿-前后_2038441483426074626.json, 图片生成/图生图/竖中指LoRA——Qwen-Image-Edit应用_1965017377282904065.json, 图片生成/图生图/精准换头LoRA——Qwen-Image-Edit应用_1961739539767300097.json, 图片生成/文生图/2030304000674893825.json, 视频生成/图生视频/千问多图融合编辑_1982020667237384193.json, 视频生成/图生视频/手办LoRA——Qwen-Image-Edit应用_1961983511181856769.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_117

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/服装提取qwen edit 2511_2087714207843311617.json、图片生成/图生图/服装试穿-前后_2038441483426074626.json、图片生成/图生图/竖中指LoRA——Qwen-Image-Edit应用_1965017377282904065.json、图片生成/图生图/精准换头LoRA——Qwen-Image-Edit应用_1961739539767300097.json、图片生成/文生图/2030304000674893825.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEdit` —— 4/7 个有
- `TextEncodeQwenImageEditPlus` —— 4/7 个有
- `AddLabel` —— 1/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/7 个有
- `SizeSelector` —— 1/7 个有
- `Switch string [Crystools]` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 864 - 1024 | 7 | 94% |
| 高度 | 1024 | 768 - 1304 | 7 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 864 - 1024，7 个样本，取值集中（一致性 94%）
- 高度 中位数 1024，观测区间 768 - 1304，7 个样本，取值集中（一致性 86%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
