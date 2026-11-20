---
name: image_to_image_lora_sampler_clip_111
type: Image To Image
frequency: 3
level: strong
coverage: 0.835667
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/展示胸部_1996194183381762050.json, 图片生成/图生图/展示脚_1996210912619020289.json, 图片生成/文生图/【ComfyUI教程】Kontext透视纠正2.0，产品合成不再一眼假，节点逐一注释_2060600000048091137.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_111

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/展示胸部_1996194183381762050.json、图片生成/图生图/展示脚_1996210912619020289.json、图片生成/文生图/【ComfyUI教程】Kontext透视纠正2.0，产品合成不再一眼假，节点逐一注释_2060600000048091137.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `Text _O` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
