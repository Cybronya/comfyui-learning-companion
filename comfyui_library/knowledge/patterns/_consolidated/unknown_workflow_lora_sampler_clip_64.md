---
name: unknown_workflow_lora_sampler_clip_64
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9285
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2044137028534669313.json, 视频生成/图生视频/1952381519627259905.json, 视频生成/图生视频/2014030248010059777.json, 视频生成/图生视频/2042644418431291393.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2044137028534669313.json、视频生成/图生视频/1952381519627259905.json、视频生成/图生视频/2014030248010059777.json、视频生成/图生视频/2042644418431291393.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `TT_img_enc_v2` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `Int` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `ZML_SwitchOutput` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 7 | 6 - 8 | 4 | 86% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 50% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 8，4 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 50%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
