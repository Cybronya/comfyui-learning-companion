---
name: text_to_image_controlnet_sampler_clip_7
type: Text To Image
frequency: 2
level: weak
coverage: 0.693
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Controlnet 控制 Z-image_2018207991035596801.json, 图片生成/文生图/Qwen image 2512文生图+CN控制汇总_2006971640961306626.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Controlnet 控制 Z-image_2018207991035596801.json、图片生成/文生图/Qwen image 2512文生图+CN控制汇总_2006971640961306626.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1408 | - | 2 | 91% |
| 高度 | 872 | - | 2 | 83% |
| 采样步数 | 8 | - | 2 | 75% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 3 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1408，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 高度 中位数 872，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
