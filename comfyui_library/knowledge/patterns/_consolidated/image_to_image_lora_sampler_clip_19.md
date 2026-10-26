---
name: image_to_image_lora_sampler_clip_19
type: Image To Image
frequency: 10
level: strong
coverage: 0.9291
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/服装展示  电商服装  平铺转立体图_2070218753207529474.json, 图片生成/图生图/服装展示  电商服装  平铺转立体图_2070576319703896065.json, 图片生成/图生图/服装平铺图转立体图，服饰提取3D立体图_2057289672996507650.json, 图片生成/图生图/服装平面图提取生成电商白底图立体图_2065861601772789762.json, 图片生成/图生图/欧卡风格转换2_2098380331689795586.json, 图片生成/图生图/欧美Q版ui图标_2098773769652363266.json, 图片生成/图生图/电商服饰展示 服饰提取 平铺图转立体图 3D立体化隐形模特_2079807412177031169.json, 图片生成/图生图/电商服饰提取 3D立体图 挂拍_平铺图转立体图_2054016935746121729.json, 图片生成/图生图/老孙AI 全能溶图 溶图打光 图像无缝融合 光影无缝溶图_2085713360263405570.json, 图片生成/图生图/背景溶图+图像调整复式工作流（需要进入工作流调整产品大小）_2105624704458510338.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/服装展示  电商服装  平铺转立体图_2070218753207529474.json、图片生成/图生图/服装展示  电商服装  平铺转立体图_2070576319703896065.json、图片生成/图生图/服装平铺图转立体图，服饰提取3D立体图_2057289672996507650.json、图片生成/图生图/服装平面图提取生成电商白底图立体图_2065861601772789762.json、图片生成/图生图/欧卡风格转换2_2098380331689795586.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/10 个有
- `LayerUtility: FluxKontextImageScale` —— 6/10 个有
- `easy imageSize` —— 6/10 个有
- `GetImageSize` —— 4/10 个有
- `ColorMatch` —— 2/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `ConstrainImage|pysssss` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `孤海图像缩放按像素` —— 2/10 个有
- `FastCanvas` —— 1/10 个有
- `FastCanvasTool` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `RMBG` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 6 | 10 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 6，10 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
