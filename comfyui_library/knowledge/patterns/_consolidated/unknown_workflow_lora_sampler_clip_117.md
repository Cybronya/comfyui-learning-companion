---
name: unknown_workflow_lora_sampler_clip_117
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9572
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2高低频首尾帧生视频低配电脑可下载本地部署_2076552090461229058.json, 视频生成/图生视频/wan首尾帧加速版_2000831805769084930.json, 视频生成/图生视频/【官版】Wan2.2 14B Fun Inp首尾帧_1956634658516471809.json, 视频生成/图生视频/【老金驿站】Wan2.2Fun-Inp首尾帧原生Comfyui工作流_1956152665396969474.json, 视频生成/图生视频/【阡陌】SageAttention+wan2.2首尾帧生视频加速版_1968555612659437570.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_117

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/wan2.2高低频首尾帧生视频低配电脑可下载本地部署_2076552090461229058.json、视频生成/图生视频/wan首尾帧加速版_2000831805769084930.json、视频生成/图生视频/【官版】Wan2.2 14B Fun Inp首尾帧_1956634658516471809.json、视频生成/图生视频/【老金驿站】Wan2.2Fun-Inp首尾帧原生Comfyui工作流_1956152665396969474.json、视频生成/图生视频/【阡陌】SageAttention+wan2.2首尾帧生视频加速版_1968555612659437570.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `WanFirstLastFrameToVideo` —— 3/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `WanFunInpaintToVideo` —— 2/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `VHS_VideoCombine` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 60% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 5 | 11% |
| 采样算法 | 1 | 1 - 3.5 | 5 | 33% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，5 个样本，取值分散，一致性仅 11%
- 采样算法 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
