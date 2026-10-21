---
name: text_to_image_sampler_clip_unet_142
type: Text To Image
frequency: 3
level: moderate
coverage: 0.778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/全新Anima3动漫图像模型-文生图-高级工作流_2049713795706175490.json, 图片生成/文生图/强力模型Z-image，活人感图片生成_1993860368776757249.json, 图片生成/文生图/提示词工程合集  附带多方案+Z-IMAGE生图 2026.1.8更新_1996447311154790402.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_142

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/全新Anima3动漫图像模型-文生图-高级工作流_2049713795706175490.json、图片生成/文生图/强力模型Z-image，活人感图片生成_1993860368776757249.json、图片生成/文生图/提示词工程合集  附带多方案+Z-IMAGE生图 2026.1.8更新_1996447311154790402.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `RH_LLMAPI_Pro_Node` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `LoadImage` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 40 | 3 | 27% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | er_sde | - | 3 | 33% |
| 调度器 | beta57 | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 40，3 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 er_sde，3 个样本，一致性 33%
- 调度器 最常用 beta57，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
