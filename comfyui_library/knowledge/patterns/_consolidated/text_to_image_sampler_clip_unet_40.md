---
name: text_to_image_sampler_clip_unet_40
type: Text To Image
frequency: 13
level: moderate
coverage: 0.927769
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Y-qwen_image_workflow_1953349482882760705.json, 图片生成/文生图/Z image Art文生图_2017603451194187778.json, 图片生成/文生图/Z image Art文生图_2017821403277430785.json, 图片生成/文生图/Z image Art文生图_2019704255820599297.json, 图片生成/文生图/Z-IMAGE 文生图工作流_2071465207611871233.json, 图片生成/文生图/Z-Image Base 8步&4步加速_2022636633476046849.json, 图片生成/文生图/Z-image + LoRA 文生图工作流_2058875529981415425.json, 图片生成/文生图/Z-image 文生图工作流（含加速器）_2046950465908252673.json, 图片生成/文生图/Z-image-turbo文生图3D国漫CG风格_2074209841383567362.json, 图片生成/文生图/Z-image-turbo文生图赛璐璐平涂动漫风格_2077821791761948673.json, 图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_2076587497584414722.json, 图片生成/文生图/Z-image-turbo文生图超写实真人摄影风格_V2.0_2114235650760339458.json, 图片生成/文生图/【GUGU】CG唯美画风LORA工作流_2001845384953643010.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Y-qwen_image_workflow_1953349482882760705.json、图片生成/文生图/Z image Art文生图_2017603451194187778.json、图片生成/文生图/Z image Art文生图_2017821403277430785.json、图片生成/文生图/Z image Art文生图_2019704255820599297.json、图片生成/文生图/Z-IMAGE 文生图工作流_2071465207611871233.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/13 个有
- `ModelSamplingAuraFlow` —— 8/13 个有
- `CR Latent Input Switch` —— 4/13 个有
- `PreviewImage` —— 3/13 个有
- `PrimitiveInt` —— 3/13 个有
- `PathchSageAttentionKJ` —— 2/13 个有
- `ConditioningZeroOut` —— 1/13 个有
- `SDXL Resolutions (JPS)` —— 1/13 个有
- `String Literal` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 13 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 13 | 45% |
| 采样算法 | euler | - | 13 | 54% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1080 | 512 - 1536 | 13 | 76% |
| 高度 | 1536 | 512 - 1920 | 13 | 64% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，13 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，13 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，13 个样本，一致性 54%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1536，13 个样本
- 高度 中位数 1536，观测区间 512 - 1920，13 个样本
- 高发问题（18/13 个样本）：Steps较低可能导致细节不足
