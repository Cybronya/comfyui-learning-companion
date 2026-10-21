---
name: unknown_workflow_video_sampler_clip_123
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8538
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyHunyuanLatentVideo, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/1903492781292032002.json, 视频生成/文生视频/1892462560061657089.json, 视频生成/文生视频/1935331799620833282.json, 视频生成/文生视频/1879187801508929537.json, 视频生成/文生视频/1905450015412916226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_123

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/1903492781292032002.json、视频生成/文生视频/1892462560061657089.json、视频生成/文生视频/1935331799620833282.json、视频生成/文生视频/1879187801508929537.json、视频生成/文生视频/1905450015412916226.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyHunyuanLatentVideo`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 4/5 个有
- `ModelSamplingSD3` —— 4/5 个有
- `ApplyFirstBlockCachePatchAdvanced` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `HunyuanVideoLoraLoader` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `SaveWEBM` —— 1/5 个有
- `VAEDecode` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | double_blocks | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
