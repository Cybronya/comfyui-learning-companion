---
name: text_to_image_upscale_sampler_clip_10
type: Text To Image
frequency: 6
level: moderate
coverage: 0.907667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, ImageUpscaleWithModel, KSampler, SaveImage, UpscaleModelLoader, VAEDecode]
problems: [CFG值较高可能导致Prompt约束过强]
missing: [ImageResize+]
members: [图片生成/文生图/1934989569676746753.json, 图片生成/文生图/1959857918407553025.json, 图片生成/文生图/AI真人短剧风格 _ SDXL电影级写真 _ 4倍超分高清修复 _ 一键出片_2074013871483998209.json, 图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json, 图片生成/文生图/图像增加细节和高清放大_1896189706760028161.json, 图片生成/文生图/小猫_1897084644569849857.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1934989569676746753.json、图片生成/文生图/1959857918407553025.json、图片生成/文生图/AI真人短剧风格 _ SDXL电影级写真 _ 4倍超分高清修复 _ 一键出片_2074013871483998209.json、图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json、图片生成/文生图/图像增加细节和高清放大_1896189706760028161.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 3/6 个有
- `UltimateSDUpscale` —— 3/6 个有
- `VAEEncode` —— 3/6 个有
- `ImageScale` —— 2/6 个有
- `LoraLoader` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `CLIPSetLastLayer` —— 1/6 个有
- `ImageResize+` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 6 | 69% |
| 高度 | 768 | 512 - 1248 | 6 | 67% |
| 采样步数 | 20 | 12 - 50 | 6 | 49% |
| Prompt 约束强度(CFG) | 8 | 5 - 48.58 | 6 | 0% |
| 采样算法 | dpmpp_2m_sde | - | 6 | 50% |
| 调度器 | karras | - | 6 | 50% |
| 重绘幅度 | 0.5 | 0.4 - 1 | 6 | 66% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| CFG值较高可能导致Prompt约束过强 | 1/6 | medium | CFG值较高，可能导致Prompt约束过强 → 建议尝试CFG 7-10 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，6 个样本
- 高度 中位数 768，观测区间 512 - 1248，6 个样本
- 采样步数 中位数 20，观测区间 12 - 50，6 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 8，观测区间 5 - 48.58，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m_sde，6 个样本，一致性 50%
- 调度器 最常用 karras，6 个样本，一致性 50%
- 重绘幅度 中位数 0.5，观测区间 0.4 - 1，6 个样本
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 48.58，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：ImageResize+
