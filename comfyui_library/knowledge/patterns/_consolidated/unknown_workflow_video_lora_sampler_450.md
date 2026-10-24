---
name: unknown_workflow_video_lora_sampler_450
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9826
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/QwenVL视频反推提示词_文生视频_Comfyui官方流_1983421247163932674.json, 视频生成/文生视频/WAN2.2文生视频_1954184197437059073.json, 视频生成/文生视频/Wan 2.2 文生视频工作流_1950002171104419841.json, 视频生成/文生视频/Wan2.2 文生视频（lightx2v加速）工作流_1966437512258498562.json, 视频生成/文生视频/wan2.2官方修改版 2分钟出视频文生视频工作流_1950151381917327361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_450

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/QwenVL视频反推提示词_文生视频_Comfyui官方流_1983421247163932674.json、视频生成/文生视频/WAN2.2文生视频_1954184197437059073.json、视频生成/文生视频/Wan 2.2 文生视频工作流_1950002171104419841.json、视频生成/文生视频/Wan2.2 文生视频（lightx2v加速）工作流_1966437512258498562.json、视频生成/文生视频/wan2.2官方修改版 2分钟出视频文生视频工作流_1950151381917327361.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 4/5 个有
- `VAEDecode` —— 4/5 个有
- `CFGZeroStarAndInit` —— 1/5 个有
- `Image_Upscaletile` —— 1/5 个有
- `MultiplePathsInput` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `VAEDecodeTiled` —— 1/5 个有
- `VideoLoader` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 8 | 8 - 14 | 5 | 74% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 14，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
