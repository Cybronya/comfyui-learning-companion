---
name: unknown_workflow_video_lora_sampler_555
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.6125
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetNode, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/文生视频/video_wan2_2_14B_QwenVL-自动提示词_1981726042085826562.json, 视频生成/文生视频/video_wan2_2_14B_Smooth Mix_1980199127709552641.json, 视频生成/文生视频/video_wan2_2_14B_holocine_1984147805432414210.json, 视频生成/文生视频/video_wan2_2_14B_qwenvl-prompt-generate_1981270580760576001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_555

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/video_wan2_2_14B_QwenVL-自动提示词_1981726042085826562.json、视频生成/文生视频/video_wan2_2_14B_Smooth Mix_1980199127709552641.json、视频生成/文生视频/video_wan2_2_14B_holocine_1984147805432414210.json、视频生成/文生视频/video_wan2_2_14B_qwenvl-prompt-generate_1981270580760576001.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `CR Text Replace` —— 1/4 个有
- `Int` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `TextBox` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 50% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 4 | 88% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，4 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
