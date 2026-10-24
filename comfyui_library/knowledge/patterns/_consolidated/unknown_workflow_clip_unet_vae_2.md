---
name: unknown_workflow_clip_unet_vae_2
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.9115
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z_image_base+turbo_workflow_2018248328844156930.json, 图片生成/文生图/z_image_base_2016450301691174913.json, 图片生成/文生图/z_image_base_2019688358565384194.json, 图片生成/文生图/z_image_turbo-dog 宠物 狗狗 文生图 去AI_2069329755043876866.json, 图片生成/文生图/z_image_turbo_1994152061438722050.json, 图片生成/文生图/z_image_turbo_1994983879373152258.json, 图片生成/文生图/z_image_turbo_basic_文生图_v14.0_yaowanli_2079045413621026817.json, 图片生成/文生图/z_image_turbo_gap_focus_2015970628842557442.json, 图片生成/文生图/z_image_turbo_linlin 文生图 去AI_2066435120067858433.json, 图片生成/文生图/z_image_turbo_ultra_fast_1994239876770054145.json, 图片生成/文生图/z_image_turbo_专属美女_airy_2071200704718528513.json, 图片生成/文生图/z_image_turbo文生图_2011271534962286593.json, 图片生成/文生图/z_image_turbo文生图_2067946808487276545.json, 图片生成/文生图/z_image_turbo文生图透明_2067952553903611905.json, 图片生成/文生图/zimage-turbo-文生图工作流-lora人像_2048255863974010881.json, 图片生成/文生图/亚秒级生成！Zimage超快图片生成器官方工作流_2035604076301393921.json, 图片生成/文生图/千问Qwen_image文生图海报_fp8_官方版26125_2015389169786294274.json, 图片生成/文生图/千问文生图，极简加速版（Qwen4-8步））_1958431884814479361.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/z_image_base+turbo_workflow_2018248328844156930.json、图片生成/文生图/z_image_base_2016450301691174913.json、图片生成/文生图/z_image_base_2019688358565384194.json、图片生成/文生图/z_image_turbo-dog 宠物 狗狗 文生图 去AI_2069329755043876866.json、图片生成/文生图/z_image_turbo_1994152061438722050.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 17/18 个有
- `ConditioningZeroOut` —— 6/18 个有
- `LoraLoader` —— 4/18 个有
- `LoraLoaderModelOnly` —— 4/18 个有
- `PreviewImage` —— 4/18 个有
- `BiRefNetRMBG` —— 1/18 个有
- `KSamplerAdvanced` —— 1/18 个有
- `RH_Translator` —— 1/18 个有
- `ShowText` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 30 | 17 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 18 | 0% |
| 采样算法 | euler | - | 18 | 56% |
| 调度器 | simple | - | 18 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| LoRA 模型强度 | 0.835 | 0.6 - 0.95 | 4 | 84% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 30，17 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，18 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，18 个样本，一致性 56%
- 调度器 最常用 simple，18 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.835，观测区间 0.6 - 0.95，4 个样本，取值集中（一致性 84%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（11/18 个样本）：Steps较低可能导致细节不足
