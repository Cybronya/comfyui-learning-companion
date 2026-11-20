---
name: text_to_image_lora_sampler_clip_44
type: Text To Image
frequency: 20
level: moderate
coverage: 0.9072
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image Turbo文生图 动漫角色设计快速生成工具_2114138338432208897.json, 图片生成/文生图/Z-Image Turbo文生图快速高质量处理工具_2101047351329771521.json, 图片生成/文生图/Z-Image-Turbo文生图｜高速出图质量在线新体验_2105251524116041729.json, 图片生成/文生图/Z-Image基本文生图处理生成工作流工具包_2101786053643431937.json, 图片生成/文生图/Z-image文生图 多风格高质量图片生成_2098860674293260290.json, 图片生成/文生图/Z-image文生图工作流 不油腻超写实人像生成_2099942321948282881.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2100177040510115842.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2100552637174341633.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2101481634838175746.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2101864171859173377.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2102210804346085377.json, 图片生成/文生图/Z-image文生图工作流｜不油腻超写实人像生成写实风_2100811509139066882.json, 图片生成/文生图/Z-image超写实文生图工作流 写实人像生成工具_2099942556120477697.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2100178170963128322.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2100551067837751298.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2101864963181731842.json, 图片生成/文生图/Z-image超写实文生图工作流｜写实人像生成利器_2100814802720481282.json, 图片生成/文生图/ZIT基础文生图工作流，高质量文本到图像生成方案_2106810710041911298.json, 图片生成/文生图/摄影质感文生图_2113993779647705089.json, 图片生成/文生图/摄影质感文生图工作流｜Z-image turbo快速出图生成_2096729113515089922.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Z-Image Turbo文生图 动漫角色设计快速生成工具_2114138338432208897.json、图片生成/文生图/Z-Image Turbo文生图快速高质量处理工具_2101047351329771521.json、图片生成/文生图/Z-Image-Turbo文生图｜高速出图质量在线新体验_2105251524116041729.json、图片生成/文生图/Z-Image基本文生图处理生成工作流工具包_2101786053643431937.json、图片生成/文生图/Z-image文生图 多风格高质量图片生成_2098860674293260290.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 17/20 个有
- `PreviewImage` —— 16/20 个有
- `ImageFromBatch` —— 14/20 个有
- `ImageUpscaleWithModel` —— 14/20 个有
- `UpscaleModelLoader` —— 14/20 个有
- `孤海注释` —— 11/20 个有
- `EmptyImage` —— 8/20 个有
- `LayerColor: BrightnessContrastV2` —— 7/20 个有
- `EmptySD3LatentImage` —— 4/20 个有
- `ModelSamplingAuraFlow` —— 3/20 个有
- `LayerColor: Brightness & Contrast` —— 2/20 个有
- `Text` —— 1/20 个有
- `TextEncodeZITSystemPrompt` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1440 | 20 | 0% |
| 高度 | 80 | 80 - 1920 | 20 | 0% |
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1440，20 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，20 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（27/20 个样本）：Steps较低可能导致细节不足
