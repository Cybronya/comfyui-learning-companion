---
name: unknown_workflow_lora_sampler_clip_30
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.967455
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, INTConstant, JWInteger, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Comfy挑战赛8（诡影映画）-1920S 黑白恐怖文生视频（主题扩写）_1983777752908242945.json, 视频生成/文生视频/Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970.json, 视频生成/文生视频/Wan2.2 Dyno+Remix 新模型1.0文生视频V2（官方采样器）_1975847969142517762.json, 视频生成/文生视频/Wan2.2 Dyno+Remix文生视频V1_1974792612945244161.json, 视频生成/文生视频/Wan2.2 lightx2v 1217文生视频V1_2001672195485122562.json, 视频生成/文生视频/wan2.2官方文生视频+Smooth 2.2动态优化+Qwen3 VL提示词优化_1983330102350114818.json, 视频生成/文生视频/（6+4步）Wan2.2 Smooth Mix V2同模型高动态文生视频V1（官方采样器）_1979857088648220673.json, 视频生成/文生视频/（6+4步）Wan2.2 Smooth Mix V2差异模型高动态文生视频V1（官方采样器）_1979868052277858305.json, 视频生成/文生视频/（6+6步）Wan2.2 Smooth Mix高动态文生视频V1（官方采样器）_1978740895153541121.json, 视频生成/文生视频/（自用）Smooth 2.2+Animated 文生视频V3（双模式）_1986673673375514625.json, 视频生成/文生视频/（自用）Smooth 2.2+Qwen3 VL自动文生视频V2_1982706970622869505.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/Comfy挑战赛8（诡影映画）-1920S 黑白恐怖文生视频（主题扩写）_1983777752908242945.json、视频生成/文生视频/Smooth 2.2+Qwen3 VL自动文生视频V1_1982722479758163970.json、视频生成/文生视频/Wan2.2 Dyno+Remix 新模型1.0文生视频V2（官方采样器）_1975847969142517762.json、视频生成/文生视频/Wan2.2 Dyno+Remix文生视频V1_1974792612945244161.json、视频生成/文生视频/Wan2.2 lightx2v 1217文生视频V1_2001672195485122562.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `JWInteger`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch+` —— 10/11 个有
- `VHS_VideoCombine` —— 9/11 个有
- `SaveImage` —— 8/11 个有
- `TT_img_enc` —— 8/11 个有
- `CR Prompt Text` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `Qwen3_VQA` —— 5/11 个有
- `SDVN Any Show` —— 5/11 个有
- `TextConcat` —— 5/11 个有
- `TT_img_enc_v2` —— 2/11 个有
- `ApplySageAttention` —— 1/11 个有
- `ConcatTextOfUtils` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `easy anythingIndexSwitch` —— 1/11 个有
- `easy seed` —— 1/11 个有
- `wanBlockSwap` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 11 | 100% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | uni_pc | - | 11 | 73% |
| 重绘幅度 | beta | - | 11 | 73% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，11 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 uni_pc，11 个样本，一致性 73%
- 重绘幅度 最常用 beta，11 个样本，一致性 73%
