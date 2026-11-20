---
name: image_to_image_sampler_clip_unet_40
type: Image To Image
frequency: 11
level: moderate
coverage: 0.874182
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/wan2.2 洗图工作流_1976841960134791170.json, 图片生成/图生图/wan2.2洗图工作流_1968904972467359746.json, 图片生成/图生图/图片精修 质感修复Texture Restoration Retouching_2098943295606059009.json, 图片生成/图生图/图片精修_质感修复Texture_Restoration_Retouching_2099340238937219074.json, 图片生成/图生图/图片精修_质感修复Texture_Restoration_Retouching_2099671834458419202.json, 图片生成/图生图/洗-通用_2029742240196730882.json, 图片生成/图生图/洗-通用_2110187075365593090.json, 图片生成/图生图/电商图生图增加人物皮肤真实感 MagicWan_1991442796139737090.json, 平台全量/产品的通用洗图_2003014787867000834.json, 平台全量/洗-人像_1959887316636610561.json, 平台全量/洗-通用_1959895812576849922.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/wan2.2 洗图工作流_1976841960134791170.json、图片生成/图生图/wan2.2洗图工作流_1968904972467359746.json、图片生成/图生图/图片精修 质感修复Texture Restoration Retouching_2098943295606059009.json、图片生成/图生图/图片精修_质感修复Texture_Restoration_Retouching_2099340238937219074.json、图片生成/图生图/图片精修_质感修复Texture_Restoration_Retouching_2099671834458419202.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 10/11 个有
- `LoraLoader` —— 10/11 个有
- `PathchSageAttentionKJ` —— 10/11 个有
- `easy imageScaleDownToSize` —— 8/11 个有
- `CFGZeroStarAndInit` —— 2/11 个有
- `Florence2ModelLoader` —— 2/11 个有
- `Florence2Run` —— 2/11 个有
- `ImageScaleBy` —— 1/11 个有
- `LayerUtility: ImageReel` —— 1/11 个有
- `LayerUtility: ImageReelComposit` —— 1/11 个有
- `StringFunction|pysssss` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.4 | 0.4 - 1 | 10 | 62% |
| LoRA 文本强度 | 0.4 | 0.4 - 1 | 10 | 62% |
| 采样步数 | 10 | 10 - 25 | 11 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | res_2m | - | 11 | 73% |
| 调度器 | beta | - | 11 | 73% |
| 重绘幅度 | 0.3 | 0.12 - 0.75 | 11 | 53% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.4，观测区间 0.4 - 1，10 个样本
- LoRA 文本强度 中位数 0.4，观测区间 0.4 - 1，10 个样本
- 采样步数 中位数 10，观测区间 10 - 25，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，11 个样本，一致性 73%
- 调度器 最常用 beta，11 个样本，一致性 73%
- 重绘幅度 中位数 0.3，观测区间 0.12 - 0.75，11 个样本
