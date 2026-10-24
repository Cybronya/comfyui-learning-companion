---
name: unknown_workflow_sampler_clip_unet_477
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.826
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, EasyCache, EmptyHunyuanVideo15Latent, KSamplerSelect, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v-混元Video1.5大模型——文生视频工作流_1994019108255629313.json, 视频生成/文生视频/混元Video1.5大模型——文生视频工作流_1993513786705379330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_477

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v-混元Video1.5大模型——文生视频工作流_1994019108255629313.json、视频生成/文生视频/混元Video1.5大模型——文生视频工作流_1993513786705379330.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `EasyCache`
- `EmptyHunyuanVideo15Latent`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `DisableNoise` —— 1/2 个有
- `HunyuanVideo15LatentUpscaleWithModel` —— 1/2 个有
- `HunyuanVideo15SuperResolution` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SplitSigmas` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
