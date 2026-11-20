---
name: text_to_image_sampler_clip_vae_25
type: Text To Image
frequency: 5
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image（nunchaku）文生图V1_1959799817432150017.json, 图片生成/文生图/nunchaku Qwen image基础工作流_1959617318458437634.json, 图片生成/文生图/qwen-edit-2509-多角色自动识别基础工作流_1930910447648571394.json, 图片生成/文生图/qwen-edit-2509-文生图基础工作流_1991539446434709506.json, 图片生成/文生图/qwen文生图+双节棍流_1963549374519414785.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_25

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen-Image（nunchaku）文生图V1_1959799817432150017.json、图片生成/文生图/nunchaku Qwen image基础工作流_1959617318458437634.json、图片生成/文生图/qwen-edit-2509-多角色自动识别基础工作流_1930910447648571394.json、图片生成/文生图/qwen-edit-2509-文生图基础工作流_1991539446434709506.json、图片生成/文生图/qwen文生图+双节棍流_1963549374519414785.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 4/5 个有
- `TextEncodeQwenImageEditPlus` —— 2/5 个有
- `AV_VAELoader` —— 1/5 个有
- `CFGNorm` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `RH_Translator` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 904 - 1328 | 5 | 86% |
| 高度 | 1024 | 720 - 1328 | 5 | 74% |
| 采样步数 | 8 | 6 - 20 | 5 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.54 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 904 - 1328，5 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 720 - 1328，5 个样本
- 采样步数 中位数 8，观测区间 6 - 20，5 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.54，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
