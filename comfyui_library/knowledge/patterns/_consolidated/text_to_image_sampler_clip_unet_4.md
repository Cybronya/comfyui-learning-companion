---
name: text_to_image_sampler_clip_unet_4
type: Text To Image
frequency: 24
level: weak
coverage: 0.946208
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Zimage图片处理（4K文生图）_2016847780504936449.json, 图片生成/文生图/Zimage基础文生图工作流-入门学习版_2079907512651964418.json, 图片生成/文生图/[众馨]最新王炸Z-Image超快速超细节生图_1994245198530150402.json, 图片生成/文生图/aidir-文生图-krea2_2078304053796364290.json, 图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json, 图片生成/文生图/anima文生图3lora工作流_2059246446616080386.json, 图片生成/文生图/b-最新krea2文生图_2070050778475220994.json, 图片生成/文生图/boogu base文生图_2067452727042592770.json, 图片生成/文生图/boogu image turbo 文生图_2069087085788749825.json, 图片生成/文生图/boogu turbo文生图_2067882978142941186.json, 图片生成/文生图/boogu. image电商海报_2040459014437347330.json, 图片生成/文生图/boogu_base 文生图_2068898981547171841.json, 图片生成/文生图/boogu_turbo_2069417901609799682.json, 图片生成/文生图/boogu_turbo文生图_2068959350126891010.json, 图片生成/文生图/boogu文生图_2069052782014984193.json, 图片生成/文生图/image_Z-16秒_2013832572974927874.json, 图片生成/文生图/krea-2文生图_2070065443259375617.json, 图片生成/文生图/z_image_Doodle style 风格工作流_2014354573992927233.json, 图片生成/文生图/手机摄影随地大小拍v2｜真实感lora暗光噪点文生图对抗单反感_2088759074585407489.json, 图片生成/文生图/手机随手拍质感文生图 随地大小拍v3模拟生活化摄影_2104273094792802306.json, 图片生成/文生图/手机随拍感文生图｜随地大小拍写实图片生成工作流_2087230285426548737.json, 图片生成/文生图/手机随拍感真实质感lora｜随地大小拍对抗单反完美感文生图_2088762070585143297.json, 图片生成/文生图/随地大小拍手机摄影v2文生图写真创作工作流_2081761338916954114.json, 图片生成/文生图/随地大小拍手机摄影v3｜文生图出大片 手机随手拍质感拉满_2104084816416305153.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/文生图/Zimage图片处理（4K文生图）_2016847780504936449.json、图片生成/文生图/Zimage基础文生图工作流-入门学习版_2079907512651964418.json、图片生成/文生图/[众馨]最新王炸Z-Image超快速超细节生图_1994245198530150402.json、图片生成/文生图/aidir-文生图-krea2_2078304053796364290.json、图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 23/24 个有
- `ConditioningZeroOut` —— 20/24 个有
- `JjkText` —— 12/24 个有
- `LoraLoaderModelOnly` —— 10/24 个有
- `CLIPLoaderGGUF` —— 7/24 个有
- `ResolutionSelector` —— 7/24 个有
- `EmptySD3LatentImage` —— 6/24 个有
- `solarL_SaveImagesToZip` —— 6/24 个有
- `孤海注释` —— 5/24 个有
- `RH_Translator` —— 4/24 个有
- `Int` —— 2/24 个有
- `DyPE_FLUX` —— 1/24 个有
- `PIP_StringConcatenation` —— 1/24 个有
- `Text _O` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 2560 | 24 | 30% |
| 高度 | 1024 | 80 - 1536 | 24 | 42% |
| 采样步数 | 8 | 4 - 50 | 24 | 0% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 6.5 | 24 | 34% |
| 采样算法 | er_sde | - | 24 | 42% |
| 调度器 | simple | - | 24 | 46% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 2560，24 个样本，取值分散，一致性仅 30%
- 高度 中位数 1024，观测区间 80 - 1536，24 个样本，取值分散，一致性仅 42%
- 采样步数 中位数 8，观测区间 4 - 50，24 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 6.5，24 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 er_sde，24 个样本，一致性 42%
- 调度器 最常用 simple，24 个样本，一致性 46%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（23/24 个样本）：Steps较低可能导致细节不足
