---
name: text_to_image_sampler_clip_unet_13
type: Text To Image
frequency: 21
level: moderate
coverage: 0.852762
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ZImage 光速高清文生图_1988965178039480322.json, 图片生成/文生图/ZImage3.0-SUPER 文生图_2017812013216436226.json, 图片生成/文生图/Z_image_turbo快速文生图 自用版_2097176754392756226.json, 图片生成/文生图/Z_image_turbo快速文生图_2051577152918835202.json, 图片生成/文生图/Zimage图像模型（支持真人的国产加速模型）_2028268832682418177.json, 图片生成/文生图/Zimage文生图-基础_2003639567171395585.json, 图片生成/文生图/Zimage文生图_1993848041241329666.json, 图片生成/文生图/Zimage文生图_2013426591489069057.json, 图片生成/文生图/Zimage文生图工作流-国产、认识中文、认识明星_1954438175747928065.json, 图片生成/文生图/Zimage超越Flux2的国产图像模型（支持真人的国产加速模型）_1993888771909369858.json, 图片生成/文生图/Zimage超越Flux2的国产图像模型（支持真人的国产加速模型）_1995004425267818497.json, 图片生成/文生图/Zimage超越Flux2的国产图像模型（支持真人的国产加速模型）_2038275878496505858.json, 图片生成/文生图/Zimage（支持真人的国产加速模型）_2027694676630835201.json, 图片生成/文生图/Zimage（支持真人的国产加速模型）_2027695408717238273.json, 图片生成/文生图/[众馨]最新王炸Z-Image超快速超细节生图_1994245198530150402.json, 图片生成/文生图/aidir-文生图-krea2_2078304053796364290.json, 图片生成/文生图/anima_preview2 二次元动漫角色自由~ & RTX Video 超分放大~_2036407166378184705.json, 图片生成/文生图/krea 2 文生图工作流_2079525843776393218.json, 图片生成/文生图/krea-2-turbo 文生图_1903742090277195777.json, 图片生成/文生图/realism_engine_krea2（自动扩写提示词）_2072599087316299777.json, 图片生成/文生图/极速美学版-Krea2 Turbo-文生图-美学不错_2070037389308944386.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/ZImage 光速高清文生图_1988965178039480322.json、图片生成/文生图/ZImage3.0-SUPER 文生图_2017812013216436226.json、图片生成/文生图/Z_image_turbo快速文生图 自用版_2097176754392756226.json、图片生成/文生图/Z_image_turbo快速文生图_2051577152918835202.json、图片生成/文生图/Zimage图像模型（支持真人的国产加速模型）_2028268832682418177.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 20/21 个有
- `PrimitiveInt` —— 10/21 个有
- `PrimitiveStringMultiline` —— 10/21 个有
- `RTXVideoSuperResolution` —— 4/21 个有
- `ResolutionSelector` —— 4/21 个有
- `PreviewAny` —— 3/21 个有
- `StringConcatenate` —— 3/21 个有
- `TextGenerate` —— 3/21 个有
- `LoraLoader` —— 2/21 个有
- `Image Comparer (rgthree)` —— 1/21 个有
- `LoadImage` —— 1/21 个有
- `LoraLoaderModelOnly` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1920 | 21 | 62% |
| 高度 | 1024 | 512 - 1920 | 21 | 55% |
| 采样步数 | 10 | 8 - 35 | 21 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 5.5 | 21 | 17% |
| 采样算法 | euler | - | 21 | 90% |
| 调度器 | simple | - | 21 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| LoRA 模型强度 | 0.6 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1920，21 个样本
- 高度 中位数 1024，观测区间 512 - 1920，21 个样本
- 采样步数 中位数 10，观测区间 8 - 35，21 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5.5，21 个样本，取值分散，一致性仅 17%
- 采样算法 最常用 euler，21 个样本，一致性 90%
- 调度器 最常用 simple，21 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
