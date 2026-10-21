---
name: text_to_image_sampler_clip_unet_14
type: Text To Image
frequency: 18
level: weak
coverage: 0.893778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-瑶光版-适合人像创作_2102648327572647937.json, 图片生成/文生图/Z-Image基础简易文生图_2003471072429260801.json, 图片生成/文生图/Z-Image文生图基础工作流_1997889845496283138.json, 图片生成/文生图/Z-Image瑶光版文生图｜人像创作质感出片首选_2104572471079952385.json, 图片生成/文生图/Z-image Kook-写实文生图_2085557272251555841.json, 图片生成/文生图/Z-image Kook-写实文生图_2085561609514213377.json, 图片生成/文生图/Z-image Kook-写实文生图_2085563036080885761.json, 图片生成/文生图/image2.0文生图全能图像G_2086535340189380610.json, 图片生成/文生图/text to Image 2.0 RH性价比版全能图片G2文生图工作流_2088373457695363074.json, 图片生成/文生图/text to Image 2.0 RH性价比版文生图｜全能图片G2图片生成工作流_2088342587194302465.json, 图片生成/文生图/全能图片2.0文生图｜实用文字生成图片工具_2090819768029896706.json, 图片生成/文生图/全能图片G-2.0文生图｜低价渠道API专用快速出图_2096294843915005953.json, 图片生成/文生图/全能图片G2.5文生图 最强生图模型图片生成_2099905456335572994.json, 图片生成/文生图/场景道具图单图文生图（真实感）_2106398654545358849.json, 图片生成/文生图/场景道具图批量文生图｜布景陈设素材一键出全套_2103107503109263362.json, 图片生成/文生图/文生图AIGC Image 2.5九图工作流，高质量文本到图像生成方案_2107237308658446338.json, 图片生成/文生图/文生图全能直出｜G-2图片生成 电商平面设计利器_2089464781400002562.json, 图片生成/文生图/海报分镜低成本｜全能图片G-2.0文生图API专用版_2096552763491704833.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_14

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/Z-Image-瑶光版-适合人像创作_2102648327572647937.json、图片生成/文生图/Z-Image基础简易文生图_2003471072429260801.json、图片生成/文生图/Z-Image文生图基础工作流_1997889845496283138.json、图片生成/文生图/Z-Image瑶光版文生图｜人像创作质感出片首选_2104572471079952385.json、图片生成/文生图/Z-image Kook-写实文生图_2085557272251555841.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 17/18 个有
- `JjkText` —— 12/18 个有
- `solarL_SaveImagesToZip` —— 12/18 个有
- `孤海注释` —— 11/18 个有
- `RH_RhartImageG2TextToImage` —— 10/18 个有
- `CR Prompt Text` —— 5/18 个有
- `FastFilmGrain` —— 5/18 个有
- `LayerColor: BrightnessContrastV2` —— 5/18 个有
- `CR Text` —— 3/18 个有
- `ShowAnything|Mie` —— 2/18 个有
- `AnyAspectRatio` —— 1/18 个有
- `PreviewImage` —— 1/18 个有
- `RH_RhartImageG25SunburstTextToImage` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1280 | 18 | 0% |
| 高度 | 80 | 80 - 1920 | 18 | 0% |
| 采样步数 | 4 | 4 - 20 | 18 | 36% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 18 | 55% |
| 采样算法 | er_sde | - | 18 | 67% |
| 调度器 | beta | - | 18 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1280，18 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，18 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 20，18 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，18 个样本
- 采样算法 最常用 er_sde，18 个样本，一致性 67%
- 调度器 最常用 beta，18 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
