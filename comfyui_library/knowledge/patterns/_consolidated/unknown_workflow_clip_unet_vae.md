---
name: unknown_workflow_clip_unet_vae
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.852
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z_image_base+turbo_workflow_2018248328844156930.json, 图片生成/文生图/z_image_base_2016450301691174913.json, 图片生成/文生图/z_image_base_2019688358565384194.json, 图片生成/文生图/z_image_turbo-dog 宠物 狗狗 文生图 去AI_2069329755043876866.json, 图片生成/文生图/z_image_turbo_1994152061438722050.json, 图片生成/文生图/z_image_turbo_1994983879373152258.json, 图片生成/文生图/z_image_turbo_basic_文生图_v14.0_yaowanli_2079045413621026817.json, 图片生成/文生图/z_image_turbo_linlin 文生图 去AI_2066435120067858433.json, 图片生成/文生图/z_image_turbo_专属美女_airy_2071200704718528513.json, 图片生成/文生图/z_image_turbo文生图_2011271534962286593.json, 图片生成/文生图/zimage_turbo+lora 基础工作流_2084827520289038337.json, 图片生成/文生图/【Z-Image-Turbo LoRA 一站式炼丹教程】手把手教你训练自己的猫咪LoRA，让自家猫咪“出现”在世界各地！_2004888505304182785.json, 图片生成/文生图/【老金驿站】Z-imageBase高质量稳定直出工作流_2016671045016625154.json, 图片生成/文生图/千问Qwen-文生图工作流_2059617428597989377.json, 图片生成/文生图/千问文生图工作流_2050531241618882561.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/z_image_base+turbo_workflow_2018248328844156930.json、图片生成/文生图/z_image_base_2016450301691174913.json、图片生成/文生图/z_image_base_2019688358565384194.json、图片生成/文生图/z_image_turbo-dog 宠物 狗狗 文生图 去AI_2069329755043876866.json、图片生成/文生图/z_image_turbo_1994152061438722050.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 14/15 个有
- `PreviewImage` —— 6/15 个有
- `LoraLoader` —— 5/15 个有
- `LoraLoaderModelOnly` —— 5/15 个有
- `ConditioningZeroOut` —— 2/15 个有
- `TextInput_` —— 2/15 个有
- `CFGNorm` —— 1/15 个有
- `KSamplerAdvanced` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 30 | 14 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 15 | 0% |
| 采样算法 | euler | - | 15 | 60% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| LoRA 模型强度 | 0.87 | 0.6 - 1 | 5 | 83% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 30，14 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，15 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，15 个样本，一致性 60%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.87，观测区间 0.6 - 1，5 个样本，取值集中（一致性 83%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（8/15 个样本）：Steps较低可能导致细节不足
