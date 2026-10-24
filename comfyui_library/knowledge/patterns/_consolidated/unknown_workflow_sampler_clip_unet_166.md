---
name: unknown_workflow_sampler_clip_unet_166
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.905625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z_image_高清放大_2002351849619505154.json, 图片生成/文生图/Z_image告别图片单一性（蓝色多脑盒）_2000908501360799745.json, 图片生成/文生图/lora生图_2_2019229829660418050.json, 图片生成/文生图/lora生图_3_api_2019356189305348098.json, 图片生成/文生图/lora生图_4_api_2019591115476836353.json, 图片生成/文生图/lora生图_5_api_2019618073682124802.json, 图片生成/文生图/​动漫角色融合现实_2068958522259369986.json, 图片生成/文生图/女团生成器_Zimage_2003080375004012545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_166

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z_image_高清放大_2002351849619505154.json、图片生成/文生图/Z_image告别图片单一性（蓝色多脑盒）_2000908501360799745.json、图片生成/文生图/lora生图_2_2019229829660418050.json、图片生成/文生图/lora生图_3_api_2019356189305348098.json、图片生成/文生图/lora生图_4_api_2019591115476836353.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `LoraLoader|pysssss` —— 3/8 个有
- `SeedVR2ExtraArgs` —— 3/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `DuckHideNode` —— 1/8 个有
- `MultiLinePromptIndex` —— 1/8 个有
- `StringConcatenate` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 1 - 12 | 8 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | res_multistep | - | 8 | 50% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 0.8 - 1 | 8 | 93% |
| LoRA 模型强度 | 1 | 0 - 1 | 3 | 29% |
| LoRA 文本强度 | 1 | 0 - 1 | 3 | 29% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 1 - 12，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，8 个样本，取值集中（一致性 93%）
- LoRA 模型强度 中位数 1，观测区间 0 - 1，3 个样本，取值分散，一致性仅 29%
- LoRA 文本强度 中位数 1，观测区间 0 - 1，3 个样本，取值分散，一致性仅 29%
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
