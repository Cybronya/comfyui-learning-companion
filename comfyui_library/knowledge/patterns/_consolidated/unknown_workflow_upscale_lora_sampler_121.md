---
name: unknown_workflow_upscale_lora_sampler_121
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.707
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ImpactSwitch, Int, KOOK_ImageCompression, KOOK_SaveJPGImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RepeatLatentBatch, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text, UNETLoader, VAEDecode, VAELoader, easy saveText]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/墨幽-CCD-V2_2066866934032986114.json, 图片生成/文生图/墨幽-CCD氛围感_2066076741847834625.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_121

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/墨幽-CCD-V2_2066866934032986114.json、图片生成/文生图/墨幽-CCD氛围感_2066076741847834625.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ImpactSwitch`
- `Int`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RepeatLatentBatch`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 1/2 个有
- `String Literal` —— 1/2 个有
- `Text Concatenate (JPS)` —— 1/2 个有
- `easy positive` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | bong_tangent | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 bong_tangent，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
