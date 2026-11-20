---
name: unknown_workflow_video_sampler_clip_175
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.99
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, ModelSamplingSD3, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/文生视频/SmoothMix 文生视频_1987864773482229761.json, 视频生成/文生视频/Smoothmix-T2v-V30-文生视频_2035692395118989313.json, 视频生成/文生视频/Smoothmix-T2v-V30-自动提示词-文生视频_2035699401913536513.json, 视频生成/文生视频/Wan2.2-Remix-文生视频_1988221036900605954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_175

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/SmoothMix 文生视频_1987864773482229761.json、视频生成/文生视频/Smoothmix-T2v-V30-文生视频_2035692395118989313.json、视频生成/文生视频/Smoothmix-T2v-V30-自动提示词-文生视频_2035699401913536513.json、视频生成/文生视频/Wan2.2-Remix-文生视频_1988221036900605954.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ModelPatchTorchSettings` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `Wan22PromptSelector` —— 3/4 个有
- `LayerUtility: TextJoin` —— 2/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | beta | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 beta，4 个样本，一致性 100%
