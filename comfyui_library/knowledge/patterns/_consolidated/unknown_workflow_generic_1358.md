---
name: unknown_workflow_generic_1358
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6625
common_nodes: [CustomAddLabel, Float, GuHaiAutoImageSplit, ImageLoader, ImageScaleToTotalPixels, JjkText, MultiTextConcatenate, PreviewImage, RH_RhartImageG2OfficialImageToImage, RH_RhartVideoSparkvideo20MultimodalVideo, RTXVideoSuperResolution, SaveImage, SaveVideo, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, easy cleanGpuUsed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, ttN concat]
problems: []
missing: []
members: [图片生成/图生图/G image2.0 一键生成专业影视分镜和TVC广告片_2058437554432729090.json, 视频生成/图生视频/G2.0 一键生成专业影视分镜及关键帧TVC广告片 V1.0_2058411561324208130.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1358

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/G image2.0 一键生成专业影视分镜和TVC广告片_2058437554432729090.json、视频生成/图生视频/G2.0 一键生成专业影视分镜及关键帧TVC广告片 V1.0_2058411561324208130.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CustomAddLabel`
- `Float`
- `GuHaiAutoImageSplit`
- `ImageLoader`
- `ImageScaleToTotalPixels`
- `JjkText`
- `MultiTextConcatenate`
- `PreviewImage`
- `RH_RhartImageG2OfficialImageToImage`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `RTXVideoSuperResolution`
- `SaveImage`
- `SaveVideo`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2ImageToImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
