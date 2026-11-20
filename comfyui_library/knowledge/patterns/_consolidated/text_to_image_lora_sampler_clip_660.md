---
name: text_to_image_lora_sampler_clip_660
type: Text To Image
frequency: 2
level: weak
coverage: 0.9535
common_nodes: [ApplyFBCacheOnModel, Automatic CFG, CLIPTextEncode, CR Combine Prompt, CR Prompt Text, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LayerUtility: PurgeVRAM, LoraLoader, ModelSamplingDiscrete, Note Plus (mtb), SaveImage, Seed Generator, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/白5-高允贞自用-酒馆_1922293504398262274.json, 图片生成/文生图/白5-高允贞自用_1894681872671113218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_660

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/白5-高允贞自用-酒馆_1922293504398262274.json、图片生成/文生图/白5-高允贞自用_1894681872671113218.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `Automatic CFG`
- `CLIPTextEncode`
- `CR Combine Prompt`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoraLoader`
- `ModelSamplingDiscrete`
- `Note Plus (mtb)`
- `SaveImage`
- `Seed Generator`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ACN_ControlNet++LoaderSingle` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ExpressionEditor` —— 1/2 个有
- `JWImageResizeByLongerSide` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.85 | - | 2 | 100% |
| LoRA 文本强度 | 0.7 | - | 2 | 100% |
| 宽度 | 1152 | - | 2 | 100% |
| 高度 | 896 | - | 2 | 100% |
| 采样步数 | 45 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 3.5 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.35 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 45，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
