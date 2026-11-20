---
name: unknown_workflow_inpaint_sampler_clip_62
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.86975
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【电商】fluxfill+redux服饰迁移_1900584857087680513.json, 平台全量/【阡陌】Flux redux ACE++万物迁移工作流_1951296258856136705.json, 平台全量/【阡陌】Flux redux ACE++超级换装工作流_1951284627325530113.json, 平台全量/【阡陌】Nunchaku 加速flux redux万物迁移工作流_1951245965376233474.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【电商】fluxfill+redux服饰迁移_1900584857087680513.json、平台全量/【阡陌】Flux redux ACE++万物迁移工作流_1951296258856136705.json、平台全量/【阡陌】Flux redux ACE++超级换装工作流_1951284627325530113.json、平台全量/【阡陌】Nunchaku 加速flux redux万物迁移工作流_1951245965376233474.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `easy imageInsetCrop` —— 3/4 个有
- `NunchakuFluxDiTLoader` —— 2/4 个有
- `NunchakuTextEncoderLoaderV2` —— 2/4 个有
- `ReduxAdvanced` —— 2/4 个有
- `ReduxPromptStyler` —— 2/4 个有
- `easy imageRemBg` —— 2/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `ImageCrop+` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/4 个有
- `TeaCache` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
