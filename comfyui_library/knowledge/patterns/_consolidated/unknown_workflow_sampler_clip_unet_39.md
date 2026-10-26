---
name: unknown_workflow_sampler_clip_unet_39
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.913611
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image base开源 文生图_2016345667848900609.json, 图片生成/文生图/Z-image 文生图  工作流_2041789971740233730.json, 图片生成/文生图/Z-image 文生图工作流 超真实感 去AI感_2037780063164309505.json, 图片生成/文生图/Z-image 文生图工作流 超真实感 去AI感_2039198359260504065.json, 图片生成/文生图/Z-image 文生图工作流_1995511350388523010.json, 图片生成/文生图/Z-image-base  文生图_2016315853096099842.json, 图片生成/文生图/Z-image-base文生图_2028736606961672194.json, 图片生成/文生图/Z-image-base文生图_2034907693407805441.json, 图片生成/文生图/Z-image-base蛋挞质感增强_2026161469645135874.json, 图片生成/文生图/Z-image-base造相完全体模型_2016501183799631873.json, 图片生成/文生图/Z-image真实文生图_2020214420164583425.json, 图片生成/文生图/qwen2512-qwen-lora-文生图工作流_2008018384633466881.json, 图片生成/文生图/z_image_turbo-dog 宠物 狗狗 文生图 去AI_2069329755043876866.json, 图片生成/文生图/z_image_turbo_linlin 文生图 去AI_2066435120067858433.json, 图片生成/文生图/z_image_turbo_专属美女_airy_2071200704718528513.json, 图片生成/文生图/千问Qwen-文生图工作流_2059617428597989377.json, 图片生成/文生图/千问文生图工作流_2050531241618882561.json, 图片生成/文生图/去AI感_美女lora7_2050555417696194561.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_39

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/Z-image base开源 文生图_2016345667848900609.json、图片生成/文生图/Z-image 文生图  工作流_2041789971740233730.json、图片生成/文生图/Z-image 文生图工作流 超真实感 去AI感_2037780063164309505.json、图片生成/文生图/Z-image 文生图工作流 超真实感 去AI感_2039198359260504065.json、图片生成/文生图/Z-image 文生图工作流_1995511350388523010.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 17/18 个有
- `LoraLoader` —— 9/18 个有
- `PreviewImage` —— 7/18 个有
- `CR Text` —— 3/18 个有
- `TextInput_` —— 2/18 个有
- `DapaoImageRatioLimitNode` —— 1/18 个有
- `Note Plus (mtb)` —— 1/18 个有
- `SDXLEmptyLatentSizePicker+` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 8 - 50 | 18 | 37% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 18 | 47% |
| 采样算法 | res_multistep | - | 18 | 50% |
| 调度器 | simple | - | 18 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| LoRA 模型强度 | 0.8 | 0.3 - 1 | 9 | 71% |
| LoRA 文本强度 | 1 | 0.7 - 1 | 9 | 90% |
| 宽度 | 768x1344 (0.57) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22.5，观测区间 8 - 50，18 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，18 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 res_multistep，18 个样本，一致性 50%
- 调度器 最常用 simple，18 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.3 - 1，9 个样本
- LoRA 文本强度 中位数 1，观测区间 0.7 - 1，9 个样本，取值集中（一致性 90%）
