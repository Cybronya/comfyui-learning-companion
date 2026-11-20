---
name: text_to_image_sampler_clip_unet_59
type: Text To Image
frequency: 12
level: weak
coverage: 0.91125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/【开箱即用】KREA-2-FP8_文生图基础流_新任生图王者_风格万变_2069375033096622081.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_V2版_2105216145447014402.json, 图片生成/文生图/【通义-ZImage文生图】最强小参数大猛兽！ 极致速度、极致质量、极致性价比。_1994129975662100482.json, 图片生成/文生图/【遇见AI】Krea2 Lip BIting 咬嘴唇lora_2082379890434854914.json, 图片生成/文生图/【遇见AI】Krea2文生图基础工作流_2069621635891679234.json, 图片生成/文生图/【遇见AI】Z-image turbo基础文生图_2053775081775611905.json, 图片生成/文生图/【遇见AI】Z-image 基础文生图_2053780457782816769.json, 图片生成/文生图/【遇见AI】boogu image base基础工作流_2067907838378340354.json, 图片生成/文生图/【遇见AI】boogu image turbo 基础工作流_2067908137574813697.json, 图片生成/文生图/丰盈美女_2094380168788922369.json, 图片生成/文生图/丰盈美女写真生成｜文生图人像一键高清出图工作流_2094808157049671682.json, 图片生成/文生图/全能图片2.1工作流合集 图像编辑一站式方案_2109731020932210690.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_59

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/【开箱即用】KREA-2-FP8_文生图基础流_新任生图王者_风格万变_2069375033096622081.json、图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_V2版_2105216145447014402.json、图片生成/文生图/【通义-ZImage文生图】最强小参数大猛兽！ 极致速度、极致质量、极致性价比。_1994129975662100482.json、图片生成/文生图/【遇见AI】Krea2 Lip BIting 咬嘴唇lora_2082379890434854914.json、图片生成/文生图/【遇见AI】Krea2文生图基础工作流_2069621635891679234.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 11/12 个有
- `ConditioningZeroOut` —— 10/12 个有
- `LoadImage` —— 9/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `JjkText` —— 2/12 个有
- `ResolutionSelector` —— 2/12 个有
- `solarL_SaveImagesToZip` —— 2/12 个有
- `孤海注释` —— 2/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `ImageStitch` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `RH_RhartImageNNb21ImageToImage` —— 1/12 个有
- `RH_RhartImageNNb21TextToImage` —— 1/12 个有
- `VAEDecodeTiled` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 40 | 12 | 8% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 12 | 26% |
| 采样算法 | er_sde | - | 12 | 50% |
| 调度器 | simple | - | 12 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1024 | 80 - 1920 | 12 | 43% |
| 高度 | 1052 | 80 - 1536 | 12 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/12 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 40，12 个样本，取值分散，一致性仅 8%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，12 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 er_sde，12 个样本，一致性 50%
- 调度器 最常用 simple，12 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1920，12 个样本，取值分散，一致性仅 43%
- 高度 中位数 1052，观测区间 80 - 1536，12 个样本
- 高发问题（11/12 个样本）：Steps较低可能导致细节不足
