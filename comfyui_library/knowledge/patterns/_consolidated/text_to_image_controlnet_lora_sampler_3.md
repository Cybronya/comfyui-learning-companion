---
name: text_to_image_controlnet_lora_sampler_3
type: Text To Image
frequency: 2
level: weak
coverage: 0.8715
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, Int, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy int]
members: [图片生成/文生图/1978359834733076482.json, 图片生成/文生图/闽粤纹样-线稿-文生图-纹样模型v3-48G_2022360002404552705.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1978359834733076482.json、图片生成/文生图/闽粤纹样-线稿-文生图-纹样模型v3-48G_2022360002404552705.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `Textbox` —— 1/2 个有
- `easy int` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `ttN text` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.875 | - | 2 | 86% |
| 宽度 | 796 | - | 2 | 64% |
| 高度 | 1216 | - | 2 | 42% |
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.75 | - | 2 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.875，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 宽度 中位数 796，样本不足，未给区间，2 个样本
- 高度 中位数 1216，样本不足，未给区间，2 个样本，取值分散，一致性仅 42%
- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy int
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
