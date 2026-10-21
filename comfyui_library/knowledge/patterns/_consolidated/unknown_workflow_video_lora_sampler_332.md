---
name: unknown_workflow_video_lora_sampler_332
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.960286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/HoloCine模型+ComfyUI，轻松生成多镜头AI电影_1983436800045817857.json, 视频生成/文生视频/HoloCine电影分镜视频模型【Comfy版】_1984101340337078273.json, 视频生成/文生视频/Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505.json, 视频生成/文生视频/Holocine电影分镜工作流_1982118673722818561.json, 视频生成/文生视频/Holocine电影分镜工作流（含提示词样例）_1987110613501587458.json, 视频生成/文生视频/万相多镜头长视频-Wan22-T2V-A14B-HoloCine工作流_2039933550228672513.json, 视频生成/文生视频/人物一致性多角度多镜头ai电影短剧真人动漫角色一致性基于HoloCine模型工作流_1985019433603272705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_332

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/HoloCine模型+ComfyUI，轻松生成多镜头AI电影_1983436800045817857.json、视频生成/文生视频/HoloCine电影分镜视频模型【Comfy版】_1984101340337078273.json、视频生成/文生视频/Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505.json、视频生成/文生视频/Holocine电影分镜工作流_1982118673722818561.json、视频生成/文生视频/Holocine电影分镜工作流（含提示词样例）_1987110613501587458.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
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
- `INTConstant` —— 6/7 个有
- `ImageFromBatch+` —— 4/7 个有
- `ImageSharpen` —— 4/7 个有
- `TorchCompileModel` —— 3/7 个有
- `Label (rgthree)` —— 2/7 个有
- `CR Seed` —— 1/7 个有
- `CreateVideo` —— 1/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/7 个有
- `GIMMVFI_interpolate` —— 1/7 个有
- `PreViewVideo` —— 1/7 个有
- `SeargePromptText` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 20 | 7 | 65% |
| 采样算法 | 3.5 | 1 - 4 | 7 | 71% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 20，7 个样本
- 采样算法 中位数 3.5，观测区间 1 - 4，7 个样本
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
