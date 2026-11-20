---
name: text_to_image_sampler_clip_unet_9
type: Text To Image
frequency: 26
level: weak
coverage: 0.933346
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-瑶光版-超真实细节增强_2049457426226749441.json, 图片生成/文生图/Z-Image-瑶光版-适合人像创作_2102648327572647937.json, 图片生成/文生图/Z-Image-瑶光版-适合人像创作_2108742472506626050.json, 图片生成/文生图/Z-Image-瑶光版-适合人像创作_2110185721926602754.json, 图片生成/文生图/Z-Image基础简易文生图_2003471072429260801.json, 图片生成/文生图/Z-Image文生图基础工作流_2004808008284733442.json, 图片生成/文生图/Z-Image瑶光版文生图｜人像创作质感出片首选_2104572471079952385.json, 图片生成/文生图/Z-image Kook-写实文生图_2036359445025923074.json, 图片生成/文生图/Z-image Kook-写实文生图_2085557272251555841.json, 图片生成/文生图/Z-image Kook-写实文生图_2085561609514213377.json, 图片生成/文生图/Z-image Kook-写实文生图_2085563036080885761.json, 图片生成/文生图/Z-image文生图工作流 不油腻超写实人像生成_2099942321948282881.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2100177040510115842.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2100552637174341633.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2101481634838175746.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2101864171859173377.json, 图片生成/文生图/Z-image文生图工作流_不油腻超写实人像生成_2102210804346085377.json, 图片生成/文生图/Z-image文生图工作流｜不油腻超写实人像生成写实风_2100811509139066882.json, 图片生成/文生图/Z-image超写实文生图工作流 写实人像生成工具_2099942556120477697.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2100178170963128322.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2100551067837751298.json, 图片生成/文生图/Z-image超写实文生图工作流_写实人像生成工具_2101864963181731842.json, 图片生成/文生图/Z-image超写实文生图工作流｜写实人像生成利器_2100814802720481282.json, 图片生成/文生图/z-image文生图工作流（不油腻超写实）_2099020153999675394.json, 图片生成/文生图/z-image文生图工作流（不油腻超写实）_2099402532144635906.json, 图片生成/文生图/z-image文生图工作流（超写实）_2100510837722148865.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/Z-Image-瑶光版-超真实细节增强_2049457426226749441.json、图片生成/文生图/Z-Image-瑶光版-适合人像创作_2102648327572647937.json、图片生成/文生图/Z-Image-瑶光版-适合人像创作_2108742472506626050.json、图片生成/文生图/Z-Image-瑶光版-适合人像创作_2110185721926602754.json、图片生成/文生图/Z-Image基础简易文生图_2003471072429260801.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 25/26 个有
- `LayerColor: BrightnessContrastV2` —— 19/26 个有
- `ConditioningZeroOut` —— 15/26 个有
- `ImageFromBatch` —— 15/26 个有
- `ImageUpscaleWithModel` —— 15/26 个有
- `PreviewImage` —— 15/26 个有
- `UpscaleModelLoader` —— 15/26 个有
- `JjkText` —— 13/26 个有
- `solarL_SaveImagesToZip` —— 13/26 个有
- `FastFilmGrain` —— 9/26 个有
- `EmptyImage` —— 8/26 个有
- `CR Text` —— 5/26 个有
- `孤海注释` —— 5/26 个有
- `AILab_QwenVL` —— 1/26 个有
- `CR Text Concatenate` —— 1/26 个有
- `QWEN_TextDisplay` —— 1/26 个有
- `ZML_LoadImage` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 80 - 1920 | 26 | 16% |
| 高度 | 992 | 80 - 1920 | 26 | 12% |
| 采样步数 | 6 | 4 - 20 | 26 | 48% |
| Prompt 约束强度(CFG) | 4 | 1 - 4.5 | 26 | 40% |
| 采样算法 | er_sde | - | 26 | 50% |
| 调度器 | beta | - | 26 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 80 - 1920，26 个样本，取值分散，一致性仅 16%
- 高度 中位数 992，观测区间 80 - 1920，26 个样本，取值分散，一致性仅 12%
- 采样步数 中位数 6，观测区间 4 - 20，26 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4.5，26 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 er_sde，26 个样本，一致性 50%
- 调度器 最常用 beta，26 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 高发问题（25/26 个样本）：Steps较低可能导致细节不足
