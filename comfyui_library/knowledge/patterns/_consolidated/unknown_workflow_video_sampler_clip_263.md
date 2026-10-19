---
name: unknown_workflow_video_sampler_clip_263
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9645
common_nodes: [CLIPLoader, CLIPTextEncode, ClipLoaderGGUF, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, KSamplerAdvanced, Label (rgthree), LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingSD3, PainterI2VAdvanced, PainterVRAM, PathchSageAttentionKJ, ShowText|pysssss, TextInput_, UNETLoader, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanVideoNAG, easy cleanGpuUsed, image_scale_pixel_v2, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Remix 3.0+Z-Image Turbo文到视频_2036368662243844097.json, 视频生成/文生视频/Remix 3.0图到视频_2036428488873353218.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_263

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Remix 3.0+Z-Image Turbo文到视频_2036368662243844097.json、视频生成/文生视频/Remix 3.0图到视频_2036428488873353218.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ClipLoaderGGUF`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `KSamplerAdvanced`
- `Label (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PainterI2VAdvanced`
- `PainterVRAM`
- `PathchSageAttentionKJ`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`
- `easy cleanGpuUsed`
- `image_scale_pixel_v2`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
