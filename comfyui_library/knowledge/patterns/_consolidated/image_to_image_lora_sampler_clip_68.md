---
name: image_to_image_lora_sampler_clip_68
type: Image To Image
frequency: 6
level: strong
coverage: 0.953167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/3D虚拟模特-服装展示-隐形模特-Klein_2040956278956101633.json, 平台全量/Flux-Klein-9B_平铺图转3D镂空平铺图_2054499457647038465.json, 平台全量/人物角色保持图像一致性 视频首尾帧图片生成  模特网红分镜洗图 Flux2-Klein-9B_2042128373140426754.json, 平台全量/换脸+换头  换脸pro 完美写实换脸换装 +写实人物一致性   4K版_2061992973981802498.json, 平台全量/电商服饰展示 3D立体虚拟模特 Flux 2 Klein 9B_2035533446818308098.json, 平台全量/电商服饰展示 服饰提取 3D立体虚拟模特 服装展示 隐形模特Flux 2 Klein 9B_2034097306227712002.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/3D虚拟模特-服装展示-隐形模特-Klein_2040956278956101633.json、平台全量/Flux-Klein-9B_平铺图转3D镂空平铺图_2054499457647038465.json、平台全量/人物角色保持图像一致性 视频首尾帧图片生成  模特网红分镜洗图 Flux2-Klein-9B_2042128373140426754.json、平台全量/换脸+换头  换脸pro 完美写实换脸换装 +写实人物一致性   4K版_2061992973981802498.json、平台全量/电商服饰展示 3D立体虚拟模特 Flux 2 Klein 9B_2035533446818308098.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
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
- `easy imageSize` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `ImageConcanate` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `LayerUtility: FluxKontextImageScale` —— 2/6 个有
- `AspectRatioSelect` —— 1/6 个有
- `ConstrainImage|pysssss` —— 1/6 个有
- `RH_RhartImageG2ImageToImage` —— 1/6 个有
- `SaveImageWebsocket` —— 1/6 个有
- `easy imageColorMatch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 5 | 6 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 5，6 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
