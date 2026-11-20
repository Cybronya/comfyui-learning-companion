---
name: text_to_image_sampler_clip_vae_12
type: Text To Image
frequency: 9
level: moderate
coverage: 0.984222
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/参照姿势生图-qwen edit 2509-nunchaku_1970044561189969921.json, 图片生成/图生图/图片编辑，分镜调整，图片分镜，多参合图_2046747967197028353.json, 图片生成/文生图/20260107-2509-多角色自动识别基础工作流-动漫短剧文生图工作流_2008835608281620482.json, 图片生成/文生图/2031384466958061570.json, 图片生成/文生图/2031384673011638273.json, 图片生成/文生图/qwen-edit-2509-多角色自动识别基础工作流_1930910447648571394.json, 图片生成/文生图/qwen-edit-2509-文生图基础工作流_1991539446434709506.json, 图片生成/文生图/分镜图用这个_2023478342393008130.json, 平台全量/qwen edit_plus （服装模特版）_1971410657902051330.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_12

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/参照姿势生图-qwen edit 2509-nunchaku_1970044561189969921.json、图片生成/图生图/图片编辑，分镜调整，图片分镜，多参合图_2046747967197028353.json、图片生成/文生图/20260107-2509-多角色自动识别基础工作流-动漫短剧文生图工作流_2008835608281620482.json、图片生成/文生图/2031384466958061570.json、图片生成/文生图/2031384673011638273.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuQwenImageDiTLoader` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 7/9 个有
- `LoadImage` —— 4/9 个有
- `AIO_Preprocessor` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `UNETLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 20 | 9 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 9 | 71% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1200 | 720 - 1280 | 9 | 76% |
| 高度 | 1280 | 720 - 1600 | 9 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 20，9 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1200，观测区间 720 - 1280，9 个样本
- 高度 中位数 1280，观测区间 720 - 1600，9 个样本
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
