---
name: unknown_workflow_video_lora_sampler_793
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8795
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2首尾帧_1955196269809602562.json, 视频生成/图生视频/Wan2.2官方加速版GGUF Q8首尾帧V1_1952087976358694913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_793

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WAN2.2首尾帧_1955196269809602562.json、视频生成/图生视频/Wan2.2官方加速版GGUF Q8首尾帧V1_1952087976358694913.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | increment | - | 2 | 50% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | uni_pc | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 increment，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 uni_pc，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
