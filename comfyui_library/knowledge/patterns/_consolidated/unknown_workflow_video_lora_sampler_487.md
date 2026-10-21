---
name: unknown_workflow_video_lora_sampler_487
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.885
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), FloatConstant, INTConstant, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2033423743539748866.json, 视频生成/图生视频/2033423714901041154.json, 视频生成/图生视频/2030903801942642689.json, 视频生成/文生视频/B妮B妳_N_S_F_W_系列_Wan22-Remix_文生视频_2034652401642250242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_487

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2033423743539748866.json、视频生成/图生视频/2033423714901041154.json、视频生成/图生视频/2030903801942642689.json、视频生成/文生视频/B妮B妳_N_S_F_W_系列_Wan22-Remix_文生视频_2034652401642250242.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `FloatConstant`
- `INTConstant`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `LoadLatent` —— 3/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/4 个有
- `SaveLatent` —— 3/4 个有
- `WanVideoDecode` —— 3/4 个有
- `WanVideoVAELoader` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `WanFirstLastFrameToVideo` —— 2/4 个有
- `WanImageToVideo` —— 2/4 个有
- `EmptyHunyuanLatentVideo` —— 1/4 个有
- `Int` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 50% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
