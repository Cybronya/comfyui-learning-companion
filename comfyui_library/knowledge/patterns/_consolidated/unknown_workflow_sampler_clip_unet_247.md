---
name: unknown_workflow_sampler_clip_unet_247
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.98
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RTXVideoSuperResolution, SaveVideo, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/97-tssp_2057689859363524610.json, 图片生成/反推提示词/tsv1.0_2045799468322263042.json, 图片生成/反推提示词/wsv1_2045509297991323649.json, 图片生成/反推提示词/wsv1_2045797882959241217.json, 图片生成/图生图/tsv1.0_2045428841375600641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_247

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/97-tssp_2057689859363524610.json、图片生成/反推提示词/tsv1.0_2045799468322263042.json、图片生成/反推提示词/wsv1_2045509297991323649.json、图片生成/反推提示词/wsv1_2045797882959241217.json、图片生成/图生图/tsv1.0_2045428841375600641.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RTXVideoSuperResolution`
- `SaveVideo`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 3/5 个有
- `CLIPVisionLoader` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `WanImageToVideo` —— 3/5 个有
- `EmptyHunyuanLatentVideo` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
