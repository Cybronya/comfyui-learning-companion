---
name: text_to_image_sampler_clip_unet_158
type: Text To Image
frequency: 4
level: strong
coverage: 0.84625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-turbo ControNet文生图姿势控制_2045229213636108290.json, 图片生成/文生图/Z-image-turbo-文生图（开源之王）_1997492012880433154.json, 图片生成/文生图/Z-image文生图_1993984303098953730.json, 图片生成/文生图/z image controlnet（cnet）【支持切换】_2001231394615554050.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_158

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo ControNet文生图姿势控制_2045229213636108290.json、图片生成/文生图/Z-image-turbo-文生图（开源之王）_1997492012880433154.json、图片生成/文生图/Z-image文生图_1993984303098953730.json、图片生成/文生图/z image controlnet（cnet）【支持切换】_2001231394615554050.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `JWInteger` —— 2/4 个有
- `ModelPatchLoader` —— 2/4 个有
- `QwenImageDiffsynthControlnet` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `DF_Float` —— 1/4 个有
- `DF_Text_Box` —— 1/4 个有
- `Image Switch (JPS)` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1080 | 768 - 1536 | 4 | 75% |
| 高度 | 1728 | 1024 - 1920 | 4 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 768 - 1536，4 个样本
- 高度 中位数 1728，观测区间 1024 - 1920，4 个样本
