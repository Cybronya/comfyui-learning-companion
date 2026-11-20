---
name: unknown_workflow_video_lora_sampler_740
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8695
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Vace图生视频加速版V1_1950024322967584770.json, 视频生成/图生视频/Wan2.2 Vace图生视频加速版_1950473499028738049.json, 视频生成/图生视频/Wan2.2官方加速版GGUF Q8首尾帧V1_1952087976358694913.json, 视频生成/文生视频/Wan 2.2 Vace 文生视频加速版_1950023675070341122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_740

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Vace图生视频加速版V1_1950024322967584770.json、视频生成/图生视频/Wan2.2 Vace图生视频加速版_1950473499028738049.json、视频生成/图生视频/Wan2.2官方加速版GGUF Q8首尾帧V1_1952087976358694913.json、视频生成/文生视频/Wan 2.2 Vace 文生视频加速版_1950023675070341122.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `ImageFromBatch+` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `TrimVideoLatent` —— 3/4 个有
- `WanVaceToVideo` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `SDVN Image Repeat` —— 2/4 个有
- `WanFirstLastFrameToVideo` —— 1/4 个有
- `wanBlockSwap` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | lcm | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
