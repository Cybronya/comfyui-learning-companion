---
name: image_to_image_controlnet_ipadapter_sampler_8
type: Image To Image
frequency: 2
level: weak
coverage: 0.8
common_nodes: [BNK_CLIPTextEncodeAdvanced, BrushNet, BrushNetLoader, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, Fast Groups Bypasser (rgthree), GrowMask, ICLightConditioning, IPAdapter, IPAdapterUnifiedLoader, InspyrenetRembg, InvertMask (segment anything), JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAndApplyICLightUnet, LoadImage, PreviewImage, RepeatLatentBatch, SaveImage, VAEDecode, VAEEncode, easy int]
problems: []
missing: []
members: [图片生成/图生图/ic-light 完美融合灯光｜一键生图系列_1917532493937836034.json, 图片生成/图生图/一句话换背景重打光｜一键生图系列_1908026376879022081.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ic-light 完美融合灯光｜一键生图系列_1917532493937836034.json、图片生成/图生图/一句话换背景重打光｜一键生图系列_1908026376879022081.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `BNK_CLIPTextEncodeAdvanced`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Fast Groups Bypasser (rgthree)`
- `GrowMask`
- `ICLightConditioning`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `InspyrenetRembg`
- `InvertMask (segment anything)`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.35 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
