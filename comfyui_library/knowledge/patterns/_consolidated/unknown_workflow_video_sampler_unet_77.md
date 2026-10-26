---
name: unknown_workflow_video_sampler_unet_77
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [BasicGuider, BasicScheduler, CLIPVisionEncode, CLIPVisionLoader, ColorMatch, DualCLIPLoader, FluxGuidance, HunyuanImageToVideo, ImageFromBatch, KSamplerSelect, LoadImage, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, TeaCache, TextEncodeHunyuanVideo_ImageToVideo, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/混元VS通义万相图生视频，对比测试_1897863153332473857.json, 视频生成/图生视频/混元图生视频+TeaCache+放大_1897894399383425025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_77

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/混元VS通义万相图生视频，对比测试_1897863153332473857.json、视频生成/图生视频/混元图生视频+TeaCache+放大_1897894399383425025.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ColorMatch`
- `DualCLIPLoader`
- `FluxGuidance`
- `HunyuanImageToVideo`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TeaCache`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `String Literal` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `WanVideoTeaCacheKJ` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 1 | 100% |
| 采样算法 | uni_pc | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
