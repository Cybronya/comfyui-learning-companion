---
name: unknown_workflow_video_lora_sampler_259
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.551625
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetImageRangeFromBatch, GetNode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/1997866783497486337.json, 视频生成/图生视频/1992287754939854849.json, 视频生成/图生视频/1993579286244294658.json, 视频生成/图生视频/1993311257635782657.json, 视频生成/图生视频/1996195758498004994.json, 视频生成/图生视频/2018679573021462530.json, 视频生成/图生视频/2030310808810430466.json, 视频生成/文生视频/FFGO 多图组合生成动画视频，电影镜头 2025-12-08_2050153435672129537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_259

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1997866783497486337.json、视频生成/图生视频/1992287754939854849.json、视频生成/图生视频/1993579286244294658.json、视频生成/图生视频/1993311257635782657.json、视频生成/图生视频/1996195758498004994.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `RMBG` —— 7/8 个有
- `TrimVideoLatent` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `RIFE VFI` —— 2/8 个有
- `AILab_ImageStitch` —— 1/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `ForLoopClose` —— 1/8 个有
- `ForLoopOpen` —— 1/8 个有
- `ImageRotate` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `WanImageToVideo` —— 1/8 个有
- `easy batchAnything` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy promptConcat` —— 1/8 个有
- `llama_cpp_instruct_adv` —— 1/8 个有
- `llama_cpp_model_loader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | lcm | - | 8 | 88% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，8 个样本，一致性 88%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
