---
name: text_to_image_sampler_clip_unet_58
type: Text To Image
frequency: 11
level: moderate
coverage: 0.902364
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Y-qwen_image_workflow_1953349482882760705.json, 图片生成/文生图/Z image Art文生图_2017603451194187778.json, 图片生成/文生图/Z image Art文生图_2017821403277430785.json, 图片生成/文生图/Z image Art文生图_2019704255820599297.json, 图片生成/文生图/Z-Image Base 8步&4步加速_2022636633476046849.json, 图片生成/文生图/Z-Image-Turbo文生图标准工作流_2091176473360166914.json, 图片生成/文生图/Zimage-ART文生图_2017256373024722946.json, 图片生成/文生图/krea2文生图+lora工作流_2094980704298946561.json, 图片生成/文生图/qwen image文生图工作流_1953069809741271041.json, 图片生成/文生图/qwen文生图动漫人物_2010134432182706177.json, 图片生成/文生图/xingtong_base_v2_2061416410592669697.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_58

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Y-qwen_image_workflow_1953349482882760705.json、图片生成/文生图/Z image Art文生图_2017603451194187778.json、图片生成/文生图/Z image Art文生图_2017821403277430785.json、图片生成/文生图/Z image Art文生图_2019704255820599297.json、图片生成/文生图/Z-Image Base 8步&4步加速_2022636633476046849.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/11 个有
- `ModelSamplingAuraFlow` —— 6/11 个有
- `PrimitiveInt` —— 5/11 个有
- `ResolutionSelector` —— 2/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `SDXL Resolutions (JPS)` —— 1/11 个有
- `String Literal` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `easy anythingIndexSwitch` —— 1/11 个有
- `easy float` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 11 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 41% |
| 采样算法 | euler | - | 11 | 55% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1080 | 512 - 1280 | 11 | 81% |
| 高度 | 1472 | 512 - 1920 | 11 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，11 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，11 个样本，一致性 55%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1280，11 个样本，取值集中（一致性 81%）
- 高度 中位数 1472，观测区间 512 - 1920，11 个样本
- 高发问题（14/11 个样本）：Steps较低可能导致细节不足
