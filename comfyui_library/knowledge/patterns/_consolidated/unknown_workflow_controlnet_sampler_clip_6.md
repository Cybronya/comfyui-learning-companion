---
name: unknown_workflow_controlnet_sampler_clip_6
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8544
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, Florence2Run, FluxGuidance, GetImageSize, Image Comparer (rgthree), ImageScaleBy, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/FLUX Krea  人像放大｜Controlnet 控制_1951506259763736577.json, 图片生成/图生图/FLUX Krea  人像放大｜Controlnet 控制_1951596913177120770.json, 图片生成/图生图/放大2_2032029770183086081.json, 图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1839649528810000386.json, 图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1912846734618259458.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX Krea  人像放大｜Controlnet 控制_1951506259763736577.json、图片生成/图生图/FLUX Krea  人像放大｜Controlnet 控制_1951596913177120770.json、图片生成/图生图/放大2_2032029770183086081.json、图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1839649528810000386.json、图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1912846734618259458.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 4/5 个有
- `Float` —— 3/5 个有
- `LoraLoader` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `Florence2ModelLoader` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.7 | 0.63 - 0.7 | 5 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，观测区间 0.63 - 0.7，5 个样本，取值集中（一致性 96%）
