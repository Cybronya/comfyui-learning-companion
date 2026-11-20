---
name: text_to_image_sampler_clip_unet_132
type: Text To Image
frequency: 6
level: weak
coverage: 0.986167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima_api_2075524651396198402.json, 图片生成/文生图/anima_preview2 二次元动漫角色自由~ & RTX Video 超分放大~_2036407166378184705.json, 图片生成/文生图/krea 2 文生图工作流_2079525843776393218.json, 图片生成/文生图/【阿良绘】boogu_turbo文生图工作流_2071226103880044545.json, 图片生成/文生图/布谷boogu_image_turbo文生图_2074490110728560642.json, 图片生成/文生图/豹豹喵呜制作：百度模型和Z-image对比测试_2045066482610081794.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_132

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/anima_api_2075524651396198402.json、图片生成/文生图/anima_preview2 二次元动漫角色自由~ & RTX Video 超分放大~_2036407166378184705.json、图片生成/文生图/krea 2 文生图工作流_2079525843776393218.json、图片生成/文生图/【阿良绘】boogu_turbo文生图工作流_2071226103880044545.json、图片生成/文生图/布谷boogu_image_turbo文生图_2074490110728560642.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `RTXVideoSuperResolution` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `SeedNode` —— 1/6 个有
- `TT_img_enc` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 6 | 18% |
| Prompt 约束强度(CFG) | 1 | 0.8 - 4 | 6 | 27% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 744 | 512 - 1024 | 6 | 77% |
| 高度 | 1024 | 512 - 1280 | 6 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，6 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.8 - 4，6 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 744，观测区间 512 - 1024，6 个样本
- 高度 中位数 1024，观测区间 512 - 1280，6 个样本
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
