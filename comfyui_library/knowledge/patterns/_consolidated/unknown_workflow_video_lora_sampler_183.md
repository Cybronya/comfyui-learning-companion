---
name: unknown_workflow_video_lora_sampler_183
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.504
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, GetNode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/20秒长视频生成，一张图，5段辞令控制动作，稳定版_2030666773145587713.json, 视频生成/图生视频/SVI 2.0超强长视频生成-10秒版_2006030934327431170.json, 视频生成/图生视频/SVI 2.0超强长视频生成-10秒版_2008158274641731586.json, 视频生成/图生视频/SVI 2.0超强长视频生成（完美一致性）-10秒版_2005641613118504962.json, 视频生成/图生视频/SVI 2.0超强长视频生成（完美一致性）-20秒版_2005640178825920513.json, 视频生成/图生视频/SVI 2.0超强长视频生成（完美一致性）-20秒版_2006214807296413698.json, 视频生成/图生视频/SVI 2.0超强长视频生成（完美一致性）-20秒版_2017042085358080002.json, 视频生成/图生视频/SVI超强一致性图生视频_2042238422814822401.json, 视频生成/图生视频/wan2.2+SVI-PRO2.0循环长视频生成_2006663467071180801.json, 视频生成/图生视频/【Supermate】优化WAN2.2-SVI 2.0-全自动-单图文字5段采样长视频_2006611754909962242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_183

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/20秒长视频生成，一张图，5段辞令控制动作，稳定版_2030666773145587713.json、视频生成/图生视频/SVI 2.0超强长视频生成-10秒版_2006030934327431170.json、视频生成/图生视频/SVI 2.0超强长视频生成-10秒版_2008158274641731586.json、视频生成/图生视频/SVI 2.0超强长视频生成（完美一致性）-10秒版_2005641613118504962.json、视频生成/图生视频/SVI 2.0超强长视频生成（完美一致性）-20秒版_2005640178825920513.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 9/10 个有
- `ImageBatchExtendWithOverlap` —— 9/10 个有
- `PlaySound|pysssss` —— 7/10 个有
- `LoadAudio` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `CR Text Concatenate` —— 1/10 个有
- `MemoryCleaner` —— 1/10 个有
- `ModelSamplingSD3` —— 1/10 个有
- `Qwen3_VQA` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `SomethingToString` —— 1/10 个有
- `Split String` —— 1/10 个有
- `WanVideoNAG` —— 1/10 个有
- `easy forLoopEnd` —— 1/10 个有
- `easy forLoopStart` —— 1/10 个有
- `easy promptLine` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 100% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 10 | 92% |
| 采样算法 | 1.75 | 1 - 2.5 | 10 | 57% |
| 调度器 | euler | - | 10 | 90% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，10 个样本，取值集中（一致性 92%）
- 采样算法 中位数 1.75，观测区间 1 - 2.5，10 个样本
- 调度器 最常用 euler，10 个样本，一致性 90%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
