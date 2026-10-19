---
name: unknown_workflow_video_lora_sampler_536
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7905
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, ImageFromBatch, ImageScale, KSampler, KSamplerSelect, LoadAudio, LoraLoader, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelSamplingAuraFlow, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/九宫格动态视频_2097982356224307201.json, 视频生成/图生视频/几何色窗动态海报_2098589237993107457.json, 视频生成/图生视频/动态头像_2098349606944993281.json, 视频生成/文生视频/Z-Image角色_MiniMaxH3原生节点MV_LoRA版1分钟版_2095424931935899650.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_536

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/九宫格动态视频_2097982356224307201.json、视频生成/图生视频/几何色窗动态海报_2098589237993107457.json、视频生成/图生视频/动态头像_2098349606944993281.json、视频生成/文生视频/Z-Image角色_MiniMaxH3原生节点MV_LoRA版1分钟版_2095424931935899650.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `ImageFromBatch`
- `ImageScale`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `SeedVR2` —— 2/4 个有
- `SeedVR2BlockSwap` —— 2/4 个有
- `SeedVR2ExtraArgs` —— 2/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `StringConcatenate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_multistep | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.6 | 0.6 - 0.6 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.6，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
