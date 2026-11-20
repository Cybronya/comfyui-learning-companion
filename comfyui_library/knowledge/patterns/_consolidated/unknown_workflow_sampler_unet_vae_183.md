---
name: unknown_workflow_sampler_unet_vae_183
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.891857
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2104392510440304641.json, 图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2111994819705925633.json, 图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2113458816762339330.json, 图片生成/图生图/CHIEFAI-千问IMAGE2.1立面迁移工作流_2102217964954152961.json, 图片生成/图生图/QWEN_PANO360 全景图生成工作流_2109286054019817473.json, 图片生成/图生图/Qwen Image Edit 2511 3图编辑_2004437958134562817.json, 图片生成/图生图/Qwen2.1多图编辑工作流_2104849503940603905.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_183

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2104392510440304641.json、图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2111994819705925633.json、图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2113458816762339330.json、图片生成/图生图/CHIEFAI-千问IMAGE2.1立面迁移工作流_2102217964954152961.json、图片生成/图生图/QWEN_PANO360 全景图生成工作流_2109286054019817473.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `TextEncodeQwenImage21` —— 6/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `EmptyLatentImage` —— 3/7 个有
- `Get resolution [Crystools]` —— 3/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `AIO_Preprocessor` —— 1/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 30 | 7 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1440 | 1024 - 1536 | 3 | 83% |
| 高度 | 1920 | 768 - 2064 | 3 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 30，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1440，观测区间 1024 - 1536，3 个样本，取值集中（一致性 83%）
- 高度 中位数 1920，观测区间 768 - 2064，3 个样本
