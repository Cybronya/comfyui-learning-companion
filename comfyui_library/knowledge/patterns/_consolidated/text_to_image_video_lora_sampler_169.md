---
name: text_to_image_video_lora_sampler_169
type: Text To Image
frequency: 3
level: strong
coverage: 0.806667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetLatentSizeAndCount, GetNode, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3IntegrationAdapterGH, MiniMaxH3IntegrationGH, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelPreviewOverrideKJ, PreviewAny, SelfLiftH3Sampler, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy anythingIndexSwitch, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3加速全能开源免费版｜文生视频图生视频通吃_2111306895595237378.json, 视频生成/文生视频/MiniMax H3加速版全能版开源SelfLift双采视频处理工具_2101757446099390466.json, 视频生成/文生视频/海螺H3加速版全能版SelfLift双采高清放大视频处理工具_2101781913726967810.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_169

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3加速全能开源免费版｜文生视频图生视频通吃_2111306895595237378.json、视频生成/文生视频/MiniMax H3加速版全能版开源SelfLift双采视频处理工具_2101757446099390466.json、视频生成/文生视频/海螺H3加速版全能版SelfLift双采高清放大视频处理工具_2101781913726967810.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetLatentSizeAndCount`
- `GetNode`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3IntegrationAdapterGH`
- `MiniMaxH3IntegrationGH`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `SelfLiftH3Sampler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 2/3 个有
- `GH_AudioVideoMerger` —— 1/3 个有
- `GH_ImageVideoComparer` —— 1/3 个有
- `PDIMAGE_LongerSize` —— 1/3 个有
- `RH_DLSS5Enhance` —— 1/3 个有
- `VOSR2ModelLoader` —— 1/3 个有
- `VOSR2Upscale` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
