---
name: image_to_image_inpaint_sampler_clip_4
type: Image To Image
frequency: 4
level: strong
coverage: 0.86925
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageComposite+, InpaintModelConditioning, Int, KSampler, LayerColor: AutoAdjustV2, LayerMask: SegformerClothesPipelineLoader, LayerMask: SegformerUltraV2, LoadImage, MaskFastGrow, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/AI染发_可指定任意发色（Flux版）_1991799729250054146.json, 平台全量/AI换发色_看看你适合哪款颜色发型吧_1938967305957072898.json, 平台全量/AI染发_可指定任意发色（Flux版）_1938970923166785537.json, 平台全量/染发工作流_1995757992945520642.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI染发_可指定任意发色（Flux版）_1991799729250054146.json、平台全量/AI换发色_看看你适合哪款颜色发型吧_1938967305957072898.json、平台全量/AI染发_可指定任意发色（Flux版）_1938970923166785537.json、平台全量/染发工作流_1995757992945520642.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageComposite+`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerColor: AutoAdjustV2`
- `LayerMask: SegformerClothesPipelineLoader`
- `LayerMask: SegformerUltraV2`
- `LoadImage`
- `MaskFastGrow`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `HfImageToRGB` —— 3/4 个有
- `ImageResizeKJ` —— 3/4 个有
- `PMRF` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `FL_ColorPicker` —— 2/4 个有
- `GrowMask` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LayerUtility: RGB Value` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ttN text` —— 2/4 个有
- `ConvertRGBNode` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
