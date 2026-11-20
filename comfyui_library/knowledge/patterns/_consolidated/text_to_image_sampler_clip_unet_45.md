---
name: text_to_image_sampler_clip_unet_45
type: Text To Image
frequency: 13
level: weak
coverage: 0.899308
common_nodes: [CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux风格选择器加速生图_2078378029721677826.json, 图片生成/文生图/Z-Image-Turbo-BF16文生图_2078377958095544321.json, 图片生成/文生图/Z-Image-Turbo写真｜一键蜂腰身材曲线自定义调整_2101548693785759746.json, 图片生成/文生图/Zimage 4步极速文生图 基础图像快速生成处理工具_2113045816763043842.json, 图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2097777800206970882.json, 图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2101478583771422722.json, 图片生成/文生图/好玩的文生图工作流｜人物类特效创意出图神器_2098761942302289921.json, 图片生成/文生图/手机摄影随地大小拍v2｜真实感lora暗光噪点文生图对抗单反感_2088759074585407489.json, 图片生成/文生图/手机随手拍质感文生图 随地大小拍v3模拟生活化摄影_2104273094792802306.json, 图片生成/文生图/手机随拍感文生图｜随地大小拍写实图片生成工作流_2087230285426548737.json, 图片生成/文生图/手机随拍感真实质感lora｜随地大小拍对抗单反完美感文生图_2088762070585143297.json, 图片生成/文生图/随地大小拍手机摄影v2文生图写真创作工作流_2081761338916954114.json, 图片生成/文生图/随地大小拍手机摄影v3｜文生图出大片 手机随手拍质感拉满_2104084816416305153.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_45

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Flux风格选择器加速生图_2078378029721677826.json、图片生成/文生图/Z-Image-Turbo-BF16文生图_2078377958095544321.json、图片生成/文生图/Z-Image-Turbo写真｜一键蜂腰身材曲线自定义调整_2101548693785759746.json、图片生成/文生图/Zimage 4步极速文生图 基础图像快速生成处理工具_2113045816763043842.json、图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2097777800206970882.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 12/13 个有
- `ConditioningZeroOut` —— 12/13 个有
- `LoraLoaderModelOnly` —— 12/13 个有
- `solarL_SaveImagesToZip` —— 11/13 个有
- `孤海注释` —— 10/13 个有
- `EmptySD3LatentImage` —— 7/13 个有
- `CLIPLoaderGGUF` —— 6/13 个有
- `ResolutionSelector` —— 6/13 个有
- `Int` —— 3/13 个有
- `DualCLIPLoader` —— 2/13 个有
- `FluxGuidance` —— 2/13 个有
- `ModelSamplingAuraFlow` —— 2/13 个有
- `ModelSamplingFlux` —— 1/13 个有
- `easy stylesSelector` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1200 | 13 | 0% |
| 高度 | 80 | 80 - 1600 | 13 | 0% |
| 采样步数 | 4 | 4 - 12 | 13 | 50% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 13 | 68% |
| 采样算法 | er_sde | - | 13 | 85% |
| 调度器 | beta | - | 13 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1200，13 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1600，13 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 12，13 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，13 个样本
- 采样算法 最常用 er_sde，13 个样本，一致性 85%
- 调度器 最常用 beta，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（19/13 个样本）：Steps较低可能导致细节不足
