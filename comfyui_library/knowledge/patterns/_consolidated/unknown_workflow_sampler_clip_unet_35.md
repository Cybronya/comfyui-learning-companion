---
name: unknown_workflow_sampler_clip_unet_35
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.863286
common_nodes: [CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed, Text Multiline, CR SDXL Aspect Ratio]
members: [comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json, 图片生成/文生图/(2秒采样极速版)Qwen Image 4步文生图V1_1958755445714345985.json, 图片生成/文生图/1910297443941187586.json, 图片生成/文生图/1932345808937807873.json, 图片生成/文生图/1952919451249348609.json, 图片生成/文生图/1953065521521618946.json, 图片生成/文生图/1955336945507471361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_35

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/image_qwen_image_2512_with_2steps_lora.json、图片生成/文生图/(2秒采样极速版)Qwen Image 4步文生图V1_1958755445714345985.json、图片生成/文生图/1910297443941187586.json、图片生成/文生图/1932345808937807873.json、图片生成/文生图/1952919451249348609.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 6/7 个有
- `EmptySD3LatentImage` —— 6/7 个有
- `ModelSamplingAuraFlow` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `CR SDXL Aspect Ratio` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `DualCLIPLoader` —— 1/7 个有
- `SDXLAspectRatio` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 2 - 30 | 7 | 36% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 7 | 45% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 2 - 30，7 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，7 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、Text Multiline、CR SDXL Aspect Ratio
