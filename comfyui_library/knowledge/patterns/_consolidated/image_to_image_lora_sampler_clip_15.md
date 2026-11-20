---
name: image_to_image_lora_sampler_clip_15
type: Image To Image
frequency: 12
level: strong
coverage: 0.733583
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-Kontext 人像换脸_1978745605067575298.json, 图片生成/图生图/Kontext dev 多彩活力插画_1941691114552455170.json, 图片生成/图生图/Kontext换脸100%相同脸型电商换脸工作流_1958510941182783489.json, 图片生成/图生图/flux-kontext 高精度换脸工作流_1965603567757312002.json, 图片生成/图生图/kontext 高精度换脸（默认自动，可选手动）_1957260449853140994.json, 图片生成/图生图/tonnie-kontext换脸（面部对齐+place it）效果不错_1993749173929525249.json, 图片生成/图生图/换脸丨最强一致性换脸丨Kontext换脸丨100%电商换脸工作流！！_1980521213351120897.json, 图片生成/图生图/换脸丨最强一致性换脸丨Kontext换脸丨100%电商换脸工作流！！_2032681757337718786.json, 图片生成/图生图/最强换脸工作流-完美换脸_1986002608529842178.json, 图片生成/图生图/生图-图换脸换头-flux-kontext_1983732617906429954.json, 图片生成/文生图/flux-kontext 高精度+高清修复换脸 无需提示词工作流_1969302778873061378.json, 平台全量/flux-kontext 高精度换脸_1958075054401662977.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Flux-Kontext 人像换脸_1978745605067575298.json、图片生成/图生图/Kontext dev 多彩活力插画_1941691114552455170.json、图片生成/图生图/Kontext换脸100%相同脸型电商换脸工作流_1958510941182783489.json、图片生成/图生图/flux-kontext 高精度换脸工作流_1965603567757312002.json、图片生成/图生图/kontext 高精度换脸（默认自动，可选手动）_1957260449853140994.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TeaCache` —— 11/12 个有
- `AutoCropFaces` —— 10/12 个有
- `FaceAlign` —— 10/12 个有
- `FaceAnalysisModels` —— 10/12 个有
- `Image Paste Crop` —— 10/12 个有
- `ImageStitch` —— 9/12 个有
- `GetNode` —— 5/12 个有
- `SetNode` —— 5/12 个有
- `Image Comparer (rgthree)` —— 4/12 个有
- `ImageConcatMulti` —— 2/12 个有
- `ImageConcanate` —— 1/12 个有
- `ImpactInt` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `RepeatLatentBatch` —— 1/12 个有
- `SUPIR_Upscale` —— 1/12 个有
- `easy imageSwitch` —— 1/12 个有
- `easy seed` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
