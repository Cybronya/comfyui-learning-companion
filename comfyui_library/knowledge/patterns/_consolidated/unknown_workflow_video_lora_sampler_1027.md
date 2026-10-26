---
name: unknown_workflow_video_lora_sampler_1027
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9515
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ImageFromBatch+, ImageSharpen, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/万相多镜头长视频-Wan22-T2V-A14B-HoloCine工作流_2039933550228672513.json, 视频生成/文生视频/人物一致性多角度多镜头ai电影短剧真人动漫角色一致性基于HoloCine模型工作流_1985019433603272705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1027

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/万相多镜头长视频-Wan22-T2V-A14B-HoloCine工作流_2039933550228672513.json、视频生成/文生视频/人物一致性多角度多镜头ai电影短剧真人动漫角色一致性基于HoloCine模型工作流_1985019433603272705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ImageFromBatch+`
- `ImageSharpen`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Seed` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `TorchCompileModel` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 100% |
| 采样算法 | 2.5 | - | 2 | 40% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
