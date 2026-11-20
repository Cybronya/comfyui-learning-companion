---
name: unknown_workflow_video_sampler_clip_240
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, JWInteger, KSamplerSelect, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewImage, RH_Translator, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoApplyNAG, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/唐装宠物的职场 “怒” 放时刻_1937427366010363905.json, 视频生成/文生视频/【AI由北】Labubu视频生成工作流_1935689445045956610.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_240

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/唐装宠物的职场 “怒” 放时刻_1937427366010363905.json、视频生成/文生视频/【AI由北】Labubu视频生成工作流_1935689445045956610.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `JWInteger`
- `KSamplerSelect`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewImage`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `CR Text Replace` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有
- `WanVideoBlockSwap` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |
| LoRA 模型强度 | 0.75 | - | 1 | 100% |
| LoRA 文本强度 | 0.75 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
