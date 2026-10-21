---
name: unknown_workflow_lora_sampler_clip_152
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.833
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CR Text, EmptyHunyuanLatentVideo, Image Comparer (rgthree), Int, KSampler, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, SeedVR2BlockSwap, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, LayerUtility: PurgeVRAM V2, easy anythingIndexSwitch, easy promptConcat]
members: [图片生成/文生图/1947568847031361537.json, 图片生成/文生图/1957310097770868738.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_152

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1947568847031361537.json、图片生成/文生图/1957310097770868738.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyHunyuanLatentVideo`
- `Image Comparer (rgthree)`
- `Int`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_TextToStringAndSeed` —— 1/2 个有
- `CFGNorm` —— 1/2 个有
- `PresetTextSelector` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.675 | - | 2 | 52% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.675，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: PurgeVRAM V2、easy anythingIndexSwitch、easy promptConcat
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
