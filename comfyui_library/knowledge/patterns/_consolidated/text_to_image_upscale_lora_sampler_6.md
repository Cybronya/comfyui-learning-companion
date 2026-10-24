---
name: text_to_image_upscale_lora_sampler_6
type: Text To Image
frequency: 15
level: strong
coverage: 0.874667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader, WujiUpscaler2, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwein-image2.1分镜专用空镜｜有人无人两版任选｜场景道具分镜素材库_2112090371961475074.json, 图片生成/图生图/Qwen Image 2.1加Vosr2加DLSS5角色定妆照文生图生工作流，角色一致性图生图方案_2108350922186387458.json, 图片生成/图生图/Qwen Image 2.1加Vosr2加DLSS5角色定妆照文生图生工作流，角色设计图生图方案_2108349378183385089.json, 图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049.json, 图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107582359372656641.json, 图片生成/图生图/Qwen Image2.1+Vosr2+DLSS5角色定妆照｜文生图生写真双路线_2108011049596317697.json, 图片生成/图生图/Qwen image2.1加Vosr2加DLSS5角色定妆五视图 角色设定批量产出_2109709219686608898.json, 图片生成/图生图/Qwen image2.1零偏移单多图局部遮罩编辑重绘 精准控制改图_2109718676936155137.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5九宫格写真｜影楼级角色一致性套图｜分镜出图_2112096726160076801.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推｜反推提示词高清放大｜三模型强强联合_2112113920214388737.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照｜文生图生双模式高清_2111274477005918209.json, 图片生成/图生图/Qwen-image2.1加Vosr2加DLSS5，角色定妆照文生图图生图_2111522943825174530.json, 图片生成/图生图/qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2106921300936712193.json, 图片生成/图生图/分镜专用空镜有人无人两版，Qwein-image2.1场景道具出图_2112343437294002177.json, 视频生成/图生视频/qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2107987558692122626.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Qwein-image2.1分镜专用空镜｜有人无人两版任选｜场景道具分镜素材库_2112090371961475074.json、图片生成/图生图/Qwen Image 2.1加Vosr2加DLSS5角色定妆照文生图生工作流，角色一致性图生图方案_2108350922186387458.json、图片生成/图生图/Qwen Image 2.1加Vosr2加DLSS5角色定妆照文生图生工作流，角色设计图生图方案_2108349378183385089.json、图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049.json、图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107582359372656641.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WujiUpscaler2`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 14/15 个有
- `孤海注释` —— 14/15 个有
- `RH_Screenwriter` —— 12/15 个有
- `WujiImagePrompt` —— 12/15 个有
- `ClownsharKSampler_Beta` —— 11/15 个有
- `easy showAnything` —— 11/15 个有
- `ManualSigmas` —— 8/15 个有
- `QwenImage21SageAttentionT8` —— 8/15 个有
- `Fast Groups Bypasser (rgthree)` —— 7/15 个有
- `PreviewImage` —— 7/15 个有
- `ResolutionSelector` —— 7/15 个有
- `WujiPromptEditor` —— 7/15 个有
- `ConditioningKrea2Rebalance` —— 4/15 个有
- `RH_LLMAPI_NODE` —— 3/15 个有
- `WujiCleaner` —— 3/15 个有
- `Image Comparer (rgthree)` —— 2/15 个有
- `ImageScaleToTotalPixels` —— 2/15 个有
- `AutoCropFaces` —— 1/15 个有
- `ConditioningZeroOut` —— 1/15 个有
- `EmptyImage` —— 1/15 个有
- `QwenImage21EditTextEncode_EditUtils` —— 1/15 个有
- `easy imageSize` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（24/15 个样本）：Steps较低可能导致细节不足
