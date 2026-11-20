---
name: unknown_workflow_sampler_clip_unet_443
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.944667
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Latent Batch Size, DualCLIPLoader, Float, Florence2ModelLoader, Florence2Run, FluxGuidance, ImageResizeKJ, InstructPixToPixConditioning, Joy_caption_two, Joy_caption_two_load, KSampler, LayerUtility: TextJoin, LoadImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/PPT背景封面融合_1943115102511906818.json, 平台全量/PPPT、海报、网页背景封面融合_1922322679733374978.json, 平台全量/室内设计丨风格转换_1892477551116521473.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_443

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/PPT背景封面融合_1943115102511906818.json、平台全量/PPPT、海报、网页背景封面融合_1922322679733374978.json、平台全量/室内设计丨风格转换_1892477551116521473.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Latent Batch Size`
- `DualCLIPLoader`
- `Float`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `ImageResizeKJ`
- `InstructPixToPixConditioning`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LayerUtility: TextJoin`
- `LoadImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
