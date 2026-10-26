---
name: unknown_workflow_sampler_unet_vae_131
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.96825
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【遇见AI】_基础文生图_2059983485657509890.json, 图片生成/图生图/印花提取-Qwen-Edit-2511-V8_2044695357266862082.json, 图片生成/图生图/图片转美漫_2007627923578167297.json, 图片生成/图生图/提取纹理 Extract-Texture-Qwen-Image-Edit-2509_2038167839743414273.json, 图片生成/图生图/无需服装、化妆、道具，一键将日常照片转为cosplay照片v0.1_1981200369042841601.json, 图片生成/图生图/真人照片转动漫 Qwen-Image-Edit-Photo-to-AnimeV2.0_2007448629186924546.json, 图片生成/文生图/2511 多角度_2019257618123984898.json, 图片生成/文生图/文生图对比Z-Image VS Qwen_2019752105942196226.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_131

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/【遇见AI】_基础文生图_2059983485657509890.json、图片生成/图生图/印花提取-Qwen-Edit-2511-V8_2044695357266862082.json、图片生成/图生图/图片转美漫_2007627923578167297.json、图片生成/图生图/提取纹理 Extract-Texture-Qwen-Image-Edit-2509_2038167839743414273.json、图片生成/图生图/无需服装、化妆、道具，一键将日常照片转为cosplay照片v0.1_1981200369042841601.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 7/8 个有
- `TextEncodeQwenImageEditPlus` —— 7/8 个有
- `LoraLoader` —— 5/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `CLIPTextEncode` —— 2/8 个有
- `TextEncodeQwenImageEdit` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `FluxGuidance` —— 1/8 个有
- `GetImageSize+` —— 1/8 个有
- `ImageScaleBy` —— 1/8 个有
- `ImageScaleDownToSize` —— 1/8 个有
- `VAEEncode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 8 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 28% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 5 | 92% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
