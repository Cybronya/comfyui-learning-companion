---
name: text_to_image_sampler_clip_unet_53
type: Text To Image
frequency: 12
level: weak
coverage: 0.856583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image-base 多采样器对比工作流_2016377804211888130.json, 图片生成/文生图/z-image-turbo 文生图_1997981712913195009.json, 图片生成/文生图/z-image-turbo-基础工作流_2010586668142698498.json, 图片生成/文生图/【尺素】krea2 turbo文生图_2069950720853499905.json, 图片生成/文生图/【阡陌】Z-Image最强极速文生图工作流_1993971431174242306.json, 图片生成/文生图/【阿良绘】boogu_turbo文生图工作流_2071226103880044545.json, 图片生成/文生图/文生图-boogu_turbo-模板_2090689514200195074.json, 图片生成/文生图/文生图Krea2_2080302375230857217.json, 图片生成/文生图/文生图z-image-turbo_2080295709659713538.json, 图片生成/文生图/文生图千问qwen2512文生图阿里最新文生图开源模型_2006970243293388801.json, 图片生成/文生图/森哥AI文生图-超自然人像-20秒快速出图_2051690409042161666.json, 图片生成/文生图/（Z-image）dpmpp-2m-sde对比euler-文生图_1995128750184574977.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_53

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/z-image-base 多采样器对比工作流_2016377804211888130.json、图片生成/文生图/z-image-turbo 文生图_1997981712913195009.json、图片生成/文生图/z-image-turbo-基础工作流_2010586668142698498.json、图片生成/文生图/【尺素】krea2 turbo文生图_2069950720853499905.json、图片生成/文生图/【阡陌】Z-Image最强极速文生图工作流_1993971431174242306.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/12 个有
- `GetNode` —— 4/12 个有
- `SetNode` —— 4/12 个有
- `TTResolutionSelector` —— 3/12 个有
- `CR Prompt Text` —— 2/12 个有
- `CR Text` —— 2/12 个有
- `INTConstant` —— 2/12 个有
- `easy promptLine` —— 2/12 个有
- `LoadImage` —— 1/12 个有
- `Text Multiline` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 50 | 12 | 12% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 12 | 33% |
| 采样算法 | euler | - | 12 | 50% |
| 调度器 | simple | - | 12 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1024 | 512 - 1536 | 12 | 72% |
| 高度 | 1508 | 512 - 1920 | 12 | 61% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 50，12 个样本，取值分散，一致性仅 12%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，12 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，12 个样本，一致性 50%
- 调度器 最常用 simple，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1536，12 个样本
- 高度 中位数 1508，观测区间 512 - 1920，12 个样本
