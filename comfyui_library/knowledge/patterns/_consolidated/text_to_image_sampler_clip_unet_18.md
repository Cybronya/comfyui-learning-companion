---
name: text_to_image_sampler_clip_unet_18
type: Text To Image
frequency: 19
level: weak
coverage: 0.934684
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-瑶光版-超真实细节增强_2049457426226749441.json, 图片生成/文生图/Z-Image-瑶光版-适合人像创作_2102648327572647937.json, 图片生成/文生图/Z-Image-瑶光版-适合人像创作_2108742472506626050.json, 图片生成/文生图/Z-Image-瑶光版-适合人像创作_2110185721926602754.json, 图片生成/文生图/Z-Image基础简易文生图_2003471072429260801.json, 图片生成/文生图/Z-Image文生图基础工作流_1997889845496283138.json, 图片生成/文生图/Z-Image瑶光版文生图｜人像创作质感出片首选_2104572471079952385.json, 图片生成/文生图/Z-image Kook-写实文生图_2036359445025923074.json, 图片生成/文生图/Z-image Kook-写实文生图_2085557272251555841.json, 图片生成/文生图/Z-image Kook-写实文生图_2085561609514213377.json, 图片生成/文生图/Z-image Kook-写实文生图_2085563036080885761.json, 图片生成/文生图/Z-image turbo 极致真实人像工作流_2111660832429002753.json, 图片生成/文生图/Z_image角色生成【文生图】_2050492161661128706.json, 图片生成/文生图/image2.0文生图全能图像G_2086535340189380610.json, 图片生成/文生图/krea2-turbo极简极速文生图｜小说配图专用 文生图秒出插画_2104056464099864578.json, 图片生成/文生图/丰盈美女人像写真生成｜文生图高质量出图工作流_2094542170748448770.json, 图片生成/文生图/小说配图极速直出 krea2 turbo极简文生图工作流_2104314139870060545.json, 平台全量/Z-image_turbo_极致真实人像工作流_2119266775853518850.json, 平台全量/Z-image_turbo_极致真实人像工作流_2119380503294996482.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_18

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Z-Image-瑶光版-超真实细节增强_2049457426226749441.json、图片生成/文生图/Z-Image-瑶光版-适合人像创作_2102648327572647937.json、图片生成/文生图/Z-Image-瑶光版-适合人像创作_2108742472506626050.json、图片生成/文生图/Z-Image-瑶光版-适合人像创作_2110185721926602754.json、图片生成/文生图/Z-Image基础简易文生图_2003471072429260801.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 18/19 个有
- `FastFilmGrain` —— 13/19 个有
- `LayerColor: BrightnessContrastV2` —— 13/19 个有
- `CR Text` —— 9/19 个有
- `Fast Groups Bypasser (rgthree)` —— 6/19 个有
- `JjkText` —— 5/19 个有
- `solarL_SaveImagesToZip` —— 5/19 个有
- `孤海注释` —— 5/19 个有
- `ConditioningZeroOut` —— 3/19 个有
- `Seed (rgthree)` —— 2/19 个有
- `AnyAspectRatio` —— 1/19 个有
- `RH_RhartImageG2TextToImage` —— 1/19 个有
- `ResolutionSelector` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | 80 - 1280 | 19 | 42% |
| 高度 | 1024 | 80 - 1920 | 19 | 36% |
| 采样步数 | 8 | 4 - 20 | 19 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 19 | 24% |
| 采样算法 | res_2s | - | 19 | 47% |
| 调度器 | bong_tangent | - | 19 | 47% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 832，观测区间 80 - 1280，19 个样本，取值分散，一致性仅 42%
- 高度 中位数 1024，观测区间 80 - 1920，19 个样本，取值分散，一致性仅 36%
- 采样步数 中位数 8，观测区间 4 - 20，19 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，19 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 res_2s，19 个样本，一致性 47%
- 调度器 最常用 bong_tangent，19 个样本，一致性 47%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（22/19 个样本）：Steps较低可能导致细节不足
