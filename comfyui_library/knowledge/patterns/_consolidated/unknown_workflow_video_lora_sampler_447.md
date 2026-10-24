---
name: unknown_workflow_video_lora_sampler_447
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9438
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ImageFromBatch+, ImageSharpen, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/HoloCine模型+ComfyUI，轻松生成多镜头AI电影_1983436800045817857.json, 视频生成/文生视频/HoloCine电影分镜视频模型【Comfy版】_1984101340337078273.json, 视频生成/文生视频/wan2.2官方优化版250928（添加最新4步加速lora）_1973561137847472129.json, 视频生成/文生视频/万相多镜头长视频-Wan22-T2V-A14B-HoloCine工作流_2039933550228672513.json, 视频生成/文生视频/人物一致性多角度多镜头ai电影短剧真人动漫角色一致性基于HoloCine模型工作流_1985019433603272705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_447

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/HoloCine模型+ComfyUI，轻松生成多镜头AI电影_1983436800045817857.json、视频生成/文生视频/HoloCine电影分镜视频模型【Comfy版】_1984101340337078273.json、视频生成/文生视频/wan2.2官方优化版250928（添加最新4步加速lora）_1973561137847472129.json、视频生成/文生视频/万相多镜头长视频-Wan22-T2V-A14B-HoloCine工作流_2039933550228672513.json、视频生成/文生视频/人物一致性多角度多镜头ai电影短剧真人动漫角色一致性基于HoloCine模型工作流_1985019433603272705.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
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
- `INTConstant` —— 4/5 个有
- `TorchCompileModel` —— 4/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/5 个有
- `GIMMVFI_interpolate` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `CR Seed` —— 1/5 个有
- `CreateVideo` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `PreViewVideo` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 5 | 100% |
| 采样算法 | 4 | 1 - 4 | 5 | 48% |
| 调度器 | euler | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 4，观测区间 1 - 4，5 个样本，取值分散，一致性仅 48%
- 调度器 最常用 euler，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
