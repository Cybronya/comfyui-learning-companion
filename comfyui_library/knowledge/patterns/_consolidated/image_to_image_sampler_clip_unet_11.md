---
name: image_to_image_sampler_clip_unet_11
type: Image To Image
frequency: 17
level: moderate
coverage: 0.923118
common_nodes: [CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/lucas的一小步_1837523258856947713.json, 图片生成/图生图/zimag图生图_2019339994762059777.json, 图片生成/图生图/【一分钟换脸，要啥自行车】_2081619387710271490.json, 图片生成/图生图/一键挂拍_平铺图转立体图-电商服饰展示 服饰提取 3D立体图_2053737452044599298.json, 图片生成/图生图/保持图像一致性Flux2-Klein-9B-Consis-Lora（工作流示例）_2031294897893937154.json, 图片生成/图生图/保持图像一致性提示词换场景_2031770431706894338.json, 图片生成/图生图/平铺图转立体图 3D立体图_2086699823432028162.json, 图片生成/图生图/挂拍_平铺图生成立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2064913964567457794.json, 图片生成/图生图/挂拍_平铺图转立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2041123739076665345.json, 图片生成/图生图/挂拍_平铺图转立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2057332722913333250.json, 图片生成/图生图/挂拍_平铺图转立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2064652694303887361.json, 图片生成/图生图/挂拍_平铺图转立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2074044441094082561.json, 图片生成/图生图/挂拍_平铺图转立体图+隐形模特+电商服饰展示+服饰提取+3D立体图_2073971346475933697.json, 图片生成/图生图/挂拍_平铺图转立体图_隐形模特_电商服饰展示_服饰提取_3D立体图_2062419055998496770.json, 图片生成/图生图/挂拍_平铺图转立体图_隐形模特_电商服饰展示_服饰提取_3D立体图_2092893109830115330.json, 图片生成/图生图/挂拍_平铺图转立体图_隐形模特_电商服饰展示_服饰提取_3D立体图_2093501578065043458.json, 图片生成/图生图/超好用🔥挂拍_平铺图转纯色立体图-电商服饰展示-手残党专用_2062814563917189121.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/lucas的一小步_1837523258856947713.json、图片生成/图生图/zimag图生图_2019339994762059777.json、图片生成/图生图/【一分钟换脸，要啥自行车】_2081619387710271490.json、图片生成/图生图/一键挂拍_平铺图转立体图-电商服饰展示 服饰提取 3D立体图_2053737452044599298.json、图片生成/图生图/保持图像一致性Flux2-Klein-9B-Consis-Lora（工作流示例）_2031294897893937154.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 16/17 个有
- `Image Comparer (rgthree)` —— 16/17 个有
- `EmptyFlux2LatentImage` —— 15/17 个有
- `LoraLoaderModelOnly` —— 15/17 个有
- `ReferenceLatent` —— 15/17 个有
- `LayerUtility: FluxKontextImageScale` —— 12/17 个有
- `easy imageSize` —— 12/17 个有
- `ImageResizeKJv2` —— 3/17 个有
- `Fast Groups Bypasser (rgthree)` —— 2/17 个有
- `DualCLIPLoader` —— 1/17 个有
- `MemoryCleaner` —— 1/17 个有
- `PreviewImage` —— 1/17 个有
- `SeedVR2LoadDiTModel` —— 1/17 个有
- `SeedVR2LoadVAEModel` —— 1/17 个有
- `SeedVR2VideoUpscaler` —— 1/17 个有
- `TT_img_enc` —— 1/17 个有
- `scale` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 20 | 17 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.3 | 17 | 93% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 88% |
| 重绘幅度 | 1 | 0.3 - 1 | 17 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 20，17 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.3，17 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，17 个样本，取值集中（一致性 83%）
- 高发问题（20/17 个样本）：Steps较低可能导致细节不足
