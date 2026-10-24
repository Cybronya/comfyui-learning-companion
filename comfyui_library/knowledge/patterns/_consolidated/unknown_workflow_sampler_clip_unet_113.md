---
name: unknown_workflow_sampler_clip_unet_113
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9524
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/JoyCaptionOne反推提示词+Qwen生图_1952963427289468930.json, 图片生成/文生图/Qwen Image文生图V1（QQ动漫版风格）_1954798087374987266.json, 图片生成/文生图/Qwen Image文生图V1（贞贞LORA版2500步）_1953815517956112386.json, 图片生成/文生图/Qwen Image，文生图 + Lora（人物写实）_1987158769756999681.json, 图片生成/文生图/Qwen_Image_2512_文生图_2038551608694415361.json, 图片生成/文生图/Qwen_Image_2512_文生图_bf16版本_2008392762101604354.json, 图片生成/文生图/Qwen_Image_2512文生图工作流_2063234247065948161.json, 图片生成/文生图/Qwen_Image_2512文生图生成模型工作流_2049713739422769154.json, 图片生成/文生图/Qwen_Image文生图_1955444251107606530.json, 图片生成/文生图/Qwen_image阿里_1952908666094743554.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_113

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/JoyCaptionOne反推提示词+Qwen生图_1952963427289468930.json、图片生成/文生图/Qwen Image文生图V1（QQ动漫版风格）_1954798087374987266.json、图片生成/文生图/Qwen Image文生图V1（贞贞LORA版2500步）_1953815517956112386.json、图片生成/文生图/Qwen Image，文生图 + Lora（人物写实）_1987158769756999681.json、图片生成/文生图/Qwen_Image_2512_文生图_2038551608694415361.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 9/10 个有
- `LoadImage` —— 3/10 个有
- `ShowText` —— 2/10 个有
- `Florence2ModelLoader` —— 1/10 个有
- `Florence2Run` —— 1/10 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/10 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/10 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 6 - 30 | 10 | 47% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 4 | 10 | 41% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 6 - 30，10 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 4，10 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（5/10 个样本）：Steps较低可能导致细节不足
