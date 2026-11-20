---
name: text_to_image_lora_sampler_clip_622
type: Text To Image
frequency: 2
level: weak
coverage: 0.92
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImageResize+, KSampler, LayerUtility: TextJoin, LoadImage, LoraLoader, ModelSamplingFlux, ReduxAdvanced, SDXLAspectRatioSelector, SaveImage, StyleModelLoader, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/3D人物玩具盲盒手办_1950483143755223042.json, 平台全量/照片转Q版手办盲盒带包装全能图片G-4o风格_1914220920028786689.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_622

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/3D人物玩具盲盒手办_1950483143755223042.json、平台全量/照片转Q版手办盲盒带包装全能图片G-4o风格_1914220920028786689.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImageResize+`
- `KSampler`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `ReduxAdvanced`
- `SDXLAspectRatioSelector`
- `SaveImage`
- `StyleModelLoader`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: LoadFlorence2Model` —— 1/2 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 832 | - | 2 | 100% |
| 高度 | 1216 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 832，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1216，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
