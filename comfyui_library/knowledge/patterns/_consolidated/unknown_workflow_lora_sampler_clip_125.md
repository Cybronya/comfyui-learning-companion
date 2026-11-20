---
name: unknown_workflow_lora_sampler_clip_125
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9344
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyHunyuanLatentVideo, INTConstant, ImageFromBatch+, JWInteger, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, Qwen3_VQA, SDVN Any Show, TextConcat, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/Comfy挑战赛8（诡影映画）-1920S 黑白恐怖文生视频（主题扩写）_1983777752908242945.json, 视频生成/文生视频/Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970.json, 视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json, 视频生成/文生视频/（自用）Smooth 2.2+Animated 文生视频V3（双模式）_1986673673375514625.json, 视频生成/文生视频/（自用）Smooth 2.2+Qwen3 VL自动文生视频V2_1982706970622869505.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_125

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Comfy挑战赛8（诡影映画）-1920S 黑白恐怖文生视频（主题扩写）_1983777752908242945.json、视频生成/文生视频/Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970.json、视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json、视频生成/文生视频/（自用）Smooth 2.2+Animated 文生视频V3（双模式）_1986673673375514625.json、视频生成/文生视频/（自用）Smooth 2.2+Qwen3 VL自动文生视频V2_1982706970622869505.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `ImageFromBatch+`
- `JWInteger`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `SDVN Any Show`
- `TextConcat`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 3/5 个有
- `SaveImage` —— 2/5 个有
- `TT_img_enc` —— 2/5 个有
- `TT_img_enc_v2` —— 2/5 个有
- `ApplySageAttention` —— 1/5 个有
- `ConcatTextOfUtils` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有
- `wanBlockSwap` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | uni_pc | - | 5 | 100% |
| 重绘幅度 | beta | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 uni_pc，5 个样本，一致性 100%
- 重绘幅度 最常用 beta，5 个样本，一致性 100%
