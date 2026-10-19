---
name: unknown_workflow_sampler_clip_vae_32
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.773
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, JWInteger, KSampler, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, PresetTextSelector, PrimitiveStringMultiline, RHHiddenNodes, SaveImage, SeedVR2ExtraArgs, SeedVR2GGUF, ShowText|pysssss, VAEDecode, VAELoader, easy anythingIndexSwitch, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM V2, easy anythingIndexSwitch, easy promptConcat]
members: [图片生成/文生图/1976636559145476098.json, 图片生成/文生图/1981626710930137089.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_32

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1976636559145476098.json、图片生成/文生图/1981626710930137089.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `JWInteger`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `PresetTextSelector`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `ShowText|pysssss`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/2 个有
- `NunchakuQwenImageDiTLoader` —— 1/2 个有
- `NunchakuQwenImageLoraStack` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22 | - | 2 | 18% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | res_3m | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22，样本不足，未给区间，2 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 res_3m，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、easy anythingIndexSwitch、easy promptConcat
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
