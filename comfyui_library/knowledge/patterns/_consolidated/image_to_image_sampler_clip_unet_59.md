---
name: image_to_image_sampler_clip_unet_59
type: Image To Image
frequency: 9
level: strong
coverage: 0.901778
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/精修天花板Flux2-klein-万物精修_2017956716545056769.json, 图片生成/图生图/蒜香卡普-Klein-9b_ 扩图-亚秒级无缝扩图_2034222233765289986.json, 图片生成/图生图/豹豹喵呜：flux2-klein+z-image动漫转真人_2029883821256089602.json, 图片生成/图生图/超好用🔥挂拍_平铺图转纯色立体图-电商服饰展示-手残党专用_2062814563917189121.json, 图片生成/文生图/空白工作流_2085537334258393089.json, 平台全量/Flux-2-Klein-9B 万能产品修图  万物精修 产品渲染质感精修 电商产品商业级修复打光_2019298988133982209.json, 平台全量/Klein_扩图_2039629604201172993.json, 平台全量/万能扩图-Kelin  去油腻修复皮肤质感+高清放大修复_2074290314696810497.json, 平台全量/电商服饰展示 3D立体虚拟模特 平铺图转立体图 隐形模特  服饰提取_2053733785031716865.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_59

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/精修天花板Flux2-klein-万物精修_2017956716545056769.json、图片生成/图生图/蒜香卡普-Klein-9b_ 扩图-亚秒级无缝扩图_2034222233765289986.json、图片生成/图生图/豹豹喵呜：flux2-klein+z-image动漫转真人_2029883821256089602.json、图片生成/图生图/超好用🔥挂拍_平铺图转纯色立体图-电商服饰展示-手残党专用_2062814563917189121.json、图片生成/文生图/空白工作流_2085537334258393089.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `EmptyFlux2LatentImage` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `ColorMatch` —— 4/9 个有
- `ImagePadForOutpaint` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `FillMaskWithColor` —— 3/9 个有
- `FluxKontextImageScale` —— 2/9 个有
- `LayerUtility: FluxKontextImageScale` —— 2/9 个有
- `easy imageSize` —— 2/9 个有
- `DrawMaskOnImage` —— 1/9 个有
- `ImageScale` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 6 | 9 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 0.6 - 1 | 9 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 6，9 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，9 个样本，取值集中（一致性 87%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
