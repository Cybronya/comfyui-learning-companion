---
name: unknown_workflow_video_lora_sampler_622
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.808
common_nodes: [AILab_QwenVL_Advanced, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen3-VL反推视频提示词_1980889321597222913.json, 图片生成/反推提示词/Qwen3VL 图片_视频 反推提示词_1991461693213646850.json, 视频生成/文生视频/Qwen3-VL反推视频提示词WAN22生成视频_1988333023324233729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_622

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/Qwen3-VL反推视频提示词_1980889321597222913.json、图片生成/反推提示词/Qwen3VL 图片_视频 反推提示词_1991461693213646850.json、视频生成/文生视频/Qwen3-VL反推视频提示词WAN22生成视频_1988333023324233729.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL_Advanced`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoInfoLoaded` —— 2/3 个有
- `JoinStrings` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
