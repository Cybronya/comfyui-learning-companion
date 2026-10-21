---
name: unknown_workflow_lora_sampler_clip_50
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.953143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, INTConstant, ImageFromBatch+, JWInteger, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Comfy挑战赛8（诡影映画）-1920S 黑白恐怖文生视频（主题扩写）_1983777752908242945.json, 视频生成/文生视频/Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970.json, 视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json, 视频生成/文生视频/（6+4步）Wan2.2 Smooth Mix V2同模型高动态文生视频V1（官方采样器）_1979857088648220673.json, 视频生成/文生视频/（6+4步）Wan2.2 Smooth Mix V2差异模型高动态文生视频V1（官方采样器）_1979868052277858305.json, 视频生成/文生视频/（自用）Smooth 2.2+Animated 文生视频V3（双模式）_1986673673375514625.json, 视频生成/文生视频/（自用）Smooth 2.2+Qwen3 VL自动文生视频V2_1982706970622869505.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/Comfy挑战赛8（诡影映画）-1920S 黑白恐怖文生视频（主题扩写）_1983777752908242945.json、视频生成/文生视频/Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970.json、视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json、视频生成/文生视频/（6+4步）Wan2.2 Smooth Mix V2同模型高动态文生视频V1（官方采样器）_1979857088648220673.json、视频生成/文生视频/（6+4步）Wan2.2 Smooth Mix V2差异模型高动态文生视频V1（官方采样器）_1979868052277858305.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `ImageFromBatch+`
- `JWInteger`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/7 个有
- `Qwen3_VQA` —— 5/7 个有
- `SDVN Any Show` —— 5/7 个有
- `TextConcat` —— 5/7 个有
- `VHS_VideoCombine` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `SaveImage` —— 4/7 个有
- `TT_img_enc` —— 4/7 个有
- `TT_img_enc_v2` —— 2/7 个有
- `ApplySageAttention` —— 1/7 个有
- `ConcatTextOfUtils` —— 1/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有
- `wanBlockSwap` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | uni_pc | - | 7 | 100% |
| 重绘幅度 | beta | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 uni_pc，7 个样本，一致性 100%
- 重绘幅度 最常用 beta，7 个样本，一致性 100%
