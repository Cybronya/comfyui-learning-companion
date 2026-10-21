---
name: text_to_image_sampler_clip_vae_10
type: Text To Image
frequency: 9
level: moderate
coverage: 0.990778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM]
members: [图片生成/文生图/1959799817432150017.json, 图片生成/文生图/1963549374519414785.json, 图片生成/文生图/20260107-2509-多角色自动识别基础工作流-动漫短剧文生图工作流_2008835608281620482.json, 图片生成/文生图/qwen-edit-2509-文生图基础工作流_1991539446434709506.json, 图片生成/文生图/万象AI+Runninghub文生图工作流（横屏）1280_720 V：dxyc2291获取软件_2019545477716381698.json, 图片生成/文生图/万象AI+Runninghub文生图工作流（横屏）_2018646916669644802.json, 图片生成/文生图/万象AI+Runninghub文生图工作流（竖屏）720_1280 V：dxyc2291获取软件_2019547644695158786.json, 图片生成/文生图/万象AI+Runninghub文生图工作流（竖屏）_2018648567409287169.json, 图片生成/文生图/分镜图用这个_2023478342393008130.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_10

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1959799817432150017.json、图片生成/文生图/1963549374519414785.json、图片生成/文生图/20260107-2509-多角色自动识别基础工作流-动漫短剧文生图工作流_2008835608281620482.json、图片生成/文生图/qwen-edit-2509-文生图基础工作流_1991539446434709506.json、图片生成/文生图/万象AI+Runninghub文生图工作流（横屏）1280_720 V：dxyc2291获取软件_2019545477716381698.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 8/9 个有
- `TextEncodeQwenImageEditPlus` —— 7/9 个有
- `AV_VAELoader` —— 1/9 个有
- `CFGNorm` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 720 - 1328 | 9 | 76% |
| 高度 | 1024 | 720 - 1328 | 9 | 73% |
| 采样步数 | 6 | 6 - 20 | 9 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.54 | 9 | 59% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 720 - 1328，9 个样本
- 高度 中位数 1024，观测区间 720 - 1328，9 个样本
- 采样步数 中位数 6，观测区间 6 - 20，9 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.54，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM
