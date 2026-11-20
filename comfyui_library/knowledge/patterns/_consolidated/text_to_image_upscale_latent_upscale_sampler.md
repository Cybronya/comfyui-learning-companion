---
name: text_to_image_upscale_latent_upscale_sampler
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7138
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LatentUpscaleBy, PreviewImage, SaveImage, UltimateSDUpscale, VAEDecode]
problems: [CFG值较高可能导致Prompt约束过强]
missing: []
members: [图片生成/文生图/ComfyUI基础+3种图片放大全流程工作流（零门槛上手）_2040718644417662977.json, 图片生成/文生图/三次放大效果工作流_2028755484269879298.json, 图片生成/文生图/图像增加细节和高清放大_1896189706760028161.json, 图片生成/文生图/小猫_1897084644569849857.json, 平台全量/SD工作流文生图原始图与三次放大_1971013257429426177.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/ComfyUI基础+3种图片放大全流程工作流（零门槛上手）_2040718644417662977.json、图片生成/文生图/三次放大效果工作流_2028755484269879298.json、图片生成/文生图/图像增加细节和高清放大_1896189706760028161.json、图片生成/文生图/小猫_1897084644569849857.json、平台全量/SD工作流文生图原始图与三次放大_1971013257429426177.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LatentUpscaleBy`
- `PreviewImage`
- `SaveImage`
- `UltimateSDUpscale`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 4/5 个有
- `UpscaleModelLoader` —— 4/5 个有
- `VAELoader` —— 3/5 个有
- `LoraLoader` —— 2/5 个有
- `CLIPSetLastLayer` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `UpscaleImageByUsingModel` —— 1/5 个有
- `UpscaleModelLoader_Optimized` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 5 | 89% |
| Prompt 约束强度(CFG) | 6.5 | 6.5 - 48.58 | 5 | 0% |
| 采样算法 | dpmpp_2m_sde | - | 5 | 60% |
| 调度器 | karras | - | 5 | 60% |
| 重绘幅度 | 0.5 | 0.5 - 0.55 | 5 | 96% |
| 宽度 | 512 | 216 - 768 | 5 | 63% |
| 高度 | 512 | 216 - 768 | 5 | 63% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| CFG值较高可能导致Prompt约束过强 | 1/5 | medium | CFG值较高，可能导致Prompt约束过强 → 建议尝试CFG 7-10 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 6.5 - 48.58，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m_sde，5 个样本，一致性 60%
- 调度器 最常用 karras，5 个样本，一致性 60%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.55，5 个样本，取值集中（一致性 96%）
- 宽度 中位数 512，观测区间 216 - 768，5 个样本
- 高度 中位数 512，观测区间 216 - 768，5 个样本
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 48.58，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
