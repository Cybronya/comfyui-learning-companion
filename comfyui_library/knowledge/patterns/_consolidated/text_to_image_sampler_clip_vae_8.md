---
name: text_to_image_sampler_clip_vae_8
type: Text To Image
frequency: 14
level: moderate
coverage: 0.938857
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku-Qwen-Image文生图lora版_1982417831478345730.json, 图片生成/文生图/Qwen-image-2.1-文生图_2101847911167520770.json, 图片生成/文生图/Z image 文生图_1993886895799205889.json, 图片生成/文生图/Z-Image文生图_2094304743563812866.json, 图片生成/文生图/Z-image 全能模型_1994451694316625922.json, 图片生成/文生图/Z-image 文生图_2006288280186265601.json, 图片生成/文生图/Z-image 最新模型 文生图工作流V1.0_1993835227038629890.json, 图片生成/文生图/Z-image-turbo：最简文生图工作流_1996508267809480705.json, 图片生成/文生图/Z-image_1996868918985773057.json, 图片生成/文生图/Z-image文生图——25年末的超级王炸_1994392372287053826.json, 图片生成/文生图/boogu_base_文生图-支持复杂提示词_2069073383496708097.json, 图片生成/文生图/krea2基础工作流_2071862532075253761.json, 图片生成/文生图/百度ERNIE-image-turbo-文生图_2044322834406707202.json, 图片生成/文生图/百度ERNIE-image-turbo-文生图_2044665456572764161.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_8

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Nunchaku-Qwen-Image文生图lora版_1982417831478345730.json、图片生成/文生图/Qwen-image-2.1-文生图_2101847911167520770.json、图片生成/文生图/Z image 文生图_1993886895799205889.json、图片生成/文生图/Z-Image文生图_2094304743563812866.json、图片生成/文生图/Z-image 全能模型_1994451694316625922.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 13/14 个有
- `PreviewImage` —— 7/14 个有
- `NunchakuQwenImageDiTLoader` —— 1/14 个有
- `NunchakuQwenImageLoraLoader` —— 1/14 个有
- `NunchakuQwenImageLoraStack` —— 1/14 个有
- `QwenImage21Cache` —— 1/14 个有
- `Text _O` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 40 | 14 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 14 | 36% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | 512 - 1920 | 14 | 70% |
| 高度 | 1280 | 512 - 2160 | 14 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 40，14 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，14 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1920，14 个样本
- 高度 中位数 1280，观测区间 512 - 2160，14 个样本
- 高发问题（8/14 个样本）：Steps较低可能导致细节不足
