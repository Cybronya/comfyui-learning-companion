---
name: unknown_workflow_lora_sampler_unet_238
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.896667
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy getNode, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/角色资产创建（性价比最高）_2052301263978676226.json, 图片生成/文生图/Qwen2511 物体四视图_2066481102876921857.json, 图片生成/文生图/角色资产创建（开源版）_2052229242536116226.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_238

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/角色资产创建（性价比最高）_2052301263978676226.json、图片生成/文生图/Qwen2511 物体四视图_2066481102876921857.json、图片生成/文生图/角色资产创建（开源版）_2052229242536116226.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `SeedVR2` —— 2/3 个有
- `SeedVR2BlockSwap` —— 2/3 个有
- `SeedVR2ExtraArgs` —— 2/3 个有
- `easy int` —— 2/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `DF_Get_image_size` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `JoinImages` —— 1/3 个有
- `RH_RhartImageNProEdit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足
