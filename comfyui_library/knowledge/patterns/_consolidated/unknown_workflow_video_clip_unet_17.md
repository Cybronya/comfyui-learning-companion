---
name: unknown_workflow_video_clip_unet_17
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9076
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, EmptyHunyuanLatentVideo, ModelSamplingSD3, RH_Prompter, SimpleMath+, TextBox, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/1949825598320459778.json, 视频生成/文生视频/wan2.2-14B 文生视频，提示词优化_2012816369728888834.json, 视频生成/文生视频/1950745634997473282.json, 视频生成/文生视频/wan2.2-14B-rapid 文生视频-最新加速模型_1998656401134247938.json, 视频生成/文生视频/1960555137225883649.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/1949825598320459778.json、视频生成/文生视频/wan2.2-14B 文生视频，提示词优化_2012816369728888834.json、视频生成/文生视频/1950745634997473282.json、视频生成/文生视频/wan2.2-14B-rapid 文生视频-最新加速模型_1998656401134247938.json、视频生成/文生视频/1960555137225883649.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `RH_Prompter`
- `SimpleMath+`
- `TextBox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `easy imageSize` —— 4/5 个有
- `Int` —— 3/5 个有
- `KSamplerAdvanced` —— 3/5 个有
- `DF_Integer` —— 2/5 个有
- `KSampler` —— 2/5 个有
- `Wan_video_prompt_generator` —— 2/5 个有
- `CR Upscale Image` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 4 | 1 - 20 | 5 | 3% |
| 采样算法 | 3.5 | 1 - 3.5 | 3 | 56% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 20，5 个样本，取值分散，一致性仅 3%
- 采样算法 中位数 3.5，观测区间 1 - 3.5，3 个样本
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
