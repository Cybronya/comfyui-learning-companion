---
name: text_to_image_lora_sampler_clip_358
type: Text To Image
frequency: 6
level: moderate
coverage: 0.949667
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/去除模糊_1963855888765390850.json, 平台全量/图片转360度全景VR_1955159903296897025.json, 平台全量/护肤品精修_1965721997336576001.json, 平台全量/模特手持产品展示_商品替换_1964240555079290882.json, 平台全量/电商产品图融合打光_1956538942852136961.json, 平台全量/都市幻夜：ComfyUI灯光视觉艺术_1978290599981899778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_358

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/去除模糊_1963855888765390850.json、平台全量/图片转360度全景VR_1955159903296897025.json、平台全量/护肤品精修_1965721997336576001.json、平台全量/模特手持产品展示_商品替换_1964240555079290882.json、平台全量/电商产品图融合打光_1956538942852136961.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
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
- `FluxKontextImageScale` —— 3/6 个有
- `GetImageSize` —— 3/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `Text` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 2304 | 6 | 27% |
| 高度 | 512 | 512 - 1536 | 6 | 48% |
| 采样步数 | 30 | 20 - 30 | 6 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 2304，6 个样本，取值分散，一致性仅 27%
- 高度 中位数 512，观测区间 512 - 1536，6 个样本，取值分散，一致性仅 48%
- 采样步数 中位数 30，观测区间 20 - 30，6 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
