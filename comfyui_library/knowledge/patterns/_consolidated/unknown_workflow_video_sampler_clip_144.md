---
name: unknown_workflow_video_sampler_clip_144
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9666
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy int]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2-14B-文生视频 (8步加速) + 提示词扩写_2064263911179898881.json, 视频生成/文生视频/Wan2.2-T2V-250928-dyno-动效丝滑+速度提升-强烈推荐_1975738907180576770.json, 视频生成/文生视频/Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_1952277100332003330.json, 视频生成/文生视频/Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_2063800321012494337.json, 视频生成/文生视频/wan2.2万相文生视频_1987538580979519489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_144

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Wan2.2-14B-文生视频 (8步加速) + 提示词扩写_2064263911179898881.json、视频生成/文生视频/Wan2.2-T2V-250928-dyno-动效丝滑+速度提升-强烈推荐_1975738907180576770.json、视频生成/文生视频/Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_1952277100332003330.json、视频生成/文生视频/Wan2.2_14B_文生视频 (8步加速) + 提示词扩写_2063800321012494337.json、视频生成/文生视频/wan2.2万相文生视频_1987538580979519489.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 3/5 个有
- `QwenLoader` —— 3/5 个有
- `TextBox` —— 3/5 个有
- `WanVideoPromptExtender` —— 3/5 个有
- `CM_IntToFloat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 8 | 6 - 20 | 5 | 49% |
| 采样算法 | 1 | 1 - 3.5 | 5 | 33% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 20，5 个样本，取值分散，一致性仅 49%
- 采样算法 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
