---
name: text_to_image_sampler_clip_vae_18
type: Text To Image
frequency: 7
level: moderate
coverage: 0.976857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, NunchakuQwenImageDiTLoader, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/单图编辑Qwen Edit 2509 nunchaku_1963473556313182209.json, 图片生成/图生图/参照姿势生图-qwen edit 2509-nunchaku_1970044561189969921.json, 图片生成/图生图/图片编辑，分镜调整，图片分镜，多参合图_2046747967197028353.json, 图片生成/文生图/20260107-2509-多角色自动识别基础工作流-动漫短剧文生图工作流_2008835608281620482.json, 图片生成/文生图/2031384466958061570.json, 图片生成/文生图/2031384673011638273.json, 图片生成/文生图/分镜图用这个_2023478342393008130.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_18

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/单图编辑Qwen Edit 2509 nunchaku_1963473556313182209.json、图片生成/图生图/参照姿势生图-qwen edit 2509-nunchaku_1970044561189969921.json、图片生成/图生图/图片编辑，分镜调整，图片分镜，多参合图_2046747967197028353.json、图片生成/文生图/20260107-2509-多角色自动识别基础工作流-动漫短剧文生图工作流_2008835608281620482.json、图片生成/文生图/2031384466958061570.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/7 个有
- `LoadImage` —— 4/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `AIO_Preprocessor` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `PrimitiveString` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 7 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 7 | 65% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 720 - 1280 | 7 | 76% |
| 高度 | 1280 | 720 - 1536 | 7 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，7 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1280，7 个样本
- 高度 中位数 1280，观测区间 720 - 1536，7 个样本
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
