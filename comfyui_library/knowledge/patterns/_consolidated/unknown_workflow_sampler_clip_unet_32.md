---
name: unknown_workflow_sampler_clip_unet_32
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.967
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2041411003677679618.json, 视频生成/图生视频/2076552090461229058.json, 视频生成/图生视频/2000831805769084930.json, 视频生成/图生视频/1968555612659437570.json, 视频生成/图生视频/2034620365376331777.json, 视频生成/文生视频/1968491886845546497.json, 视频生成/文生视频/1967793949974867969.json, 视频生成/文生视频/1967560743048581122.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_32

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2041411003677679618.json、视频生成/图生视频/2076552090461229058.json、视频生成/图生视频/2000831805769084930.json、视频生成/图生视频/1968555612659437570.json、视频生成/图生视频/2034620365376331777.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `VAEDecode` —— 7/8 个有
- `WanFirstLastFrameToVideo` —— 5/8 个有
- `EmptyHunyuanLatentVideo` —— 3/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `ModelPatchTorchSettings` —— 2/8 个有
- `ImpactFloat` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `VAEDecodeTiled` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 75% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 8 | 12% |
| 采样算法 | 1 | 1 - 4 | 8 | 28% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，8 个样本，取值分散，一致性仅 12%
- 采样算法 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
