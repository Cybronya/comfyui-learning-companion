---
name: unknown_workflow_video_lora_sampler_646
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.609667
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, DWPreprocessor, GetNode, INTConstant, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, TorchCompileModel, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSoundImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/04-06-01-WAN2.2-数字人-S2V-原生_1991727262569541633.json, 数字人/数字人/S2V数字人（ComfyUI官方版全功能）楚门的AI世界_1961358409335508993.json, 数字人/数字人/【gen全能视频Si】s2v数字人（comfyui官方版全功能）_1967813991944826882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_646

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/04-06-01-WAN2.2-数字人-S2V-原生_1991727262569541633.json、数字人/数字人/S2V数字人（ComfyUI官方版全功能）楚门的AI世界_1961358409335508993.json、数字人/数字人/【gen全能视频Si】s2v数字人（comfyui官方版全功能）_1967813991944826882.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `DWPreprocessor`
- `GetNode`
- `INTConstant`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `TorchCompileModel`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSoundImageToVideo`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `ContextWindowsManual` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `JWIntegerToString` —— 1/3 个有
- `PreViewVideo` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 6 - 20 | 3 | 57% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 3 | 46% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 6 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，3 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
