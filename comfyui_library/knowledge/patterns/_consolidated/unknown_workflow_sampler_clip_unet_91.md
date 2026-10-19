---
name: unknown_workflow_sampler_clip_unet_91
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.869
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, EasyCache, EmptyHunyuanVideo15Latent, JWInteger, KSamplerSelect, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/HunyuanVideo 1.5 480P 50步 VS LighgtX2V 8步文生视频_1993022077519282177.json, 视频生成/文生视频/HunyuanVideo 1.5 480P 8步LightX2V文生视频加速版V1_1992951299952099329.json, 视频生成/文生视频/HunyuanVideo 1.5 720P 20步优化版文生视频_1992813591025831937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_91

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/HunyuanVideo 1.5 480P 50步 VS LighgtX2V 8步文生视频_1993022077519282177.json、视频生成/文生视频/HunyuanVideo 1.5 480P 8步LightX2V文生视频加速版V1_1992951299952099329.json、视频生成/文生视频/HunyuanVideo 1.5 720P 20步优化版文生视频_1992813591025831937.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `EasyCache`
- `EmptyHunyuanVideo15Latent`
- `JWInteger`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `AddLabel` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
