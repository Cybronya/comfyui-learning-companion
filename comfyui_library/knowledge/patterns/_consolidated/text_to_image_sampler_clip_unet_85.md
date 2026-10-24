---
name: text_to_image_sampler_clip_unet_85
type: Text To Image
frequency: 7
level: strong
coverage: 0.943571
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext_智能图文编辑_2075118959145349121.json, 图片生成/图生图/kontext商业级印花提取工作流_2033184278510571521.json, 图片生成/图生图/kontext商业级印花提取工作流_2033521179331399681.json, 图片生成/图生图/【遇见AI】flux-kontext 多图编辑工作流_2050856956960747521.json, 图片生成/图生图/单图生成全景图_1916887048446480386.json, 图片生成/图生图/平铺服装加模特v1.0_1967477894467477505.json, 图片生成/图生图/新-kontext商业级印花提取工作流_2060922860222373890.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_85

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Kontext_智能图文编辑_2075118959145349121.json、图片生成/图生图/kontext商业级印花提取工作流_2033184278510571521.json、图片生成/图生图/kontext商业级印花提取工作流_2033521179331399681.json、图片生成/图生图/【遇见AI】flux-kontext 多图编辑工作流_2050856956960747521.json、图片生成/图生图/单图生成全景图_1916887048446480386.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `Get Image Size` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 7 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 512 - 1536 | 7 | 66% |
| 高度 | 1024 | 512 - 1024 | 7 | 73% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，7 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1536，7 个样本
- 高度 中位数 1024，观测区间 512 - 1024，7 个样本
